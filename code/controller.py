# -*- coding: utf-8 -*-
"""
    Controller : this code contains all the functions to manage the application
    
    PUBLIC
        analyze_image()
    
    PRIVATE
        __save_uploadedfile()
"""

import os
from model import paths, files, names, PROJECT_PATH


from object_detection.utils import label_map_util
from object_detection.utils import visualization_utils as viz_utils
from object_detection.utils import config_util
from object_detection.builders import model_builder
import tensorflow as tf

import cv2 
import numpy as np
from matplotlib import pyplot as plt

from PIL import Image



#PUBLIC
def analyze_image(img):
    #Enregistre l'image dans un dossier tampon
    __save_uploadedfile(img)
    
    #Détecte les déchets
    __detect_from_image(img.name, detection_model)
    
    return Image.open(files['OUT_IMG']) 
    

#PRIVATE
def __save_uploadedfile(uploadedfile, directory = paths['TAMPON_FOLDER_PATH']):
    img_path = os.path.join(directory, uploadedfile.name)
    if not os.path.exists(img_path):
        with open(img_path, 'wb') as f:
             f.write(uploadedfile.getbuffer())

    
@tf.function
def __detect_fn(image, detection_model):
    image, shapes = detection_model.preprocess(image)
    prediction_dict = detection_model.predict(image, shapes)
    detections = detection_model.postprocess(prediction_dict, shapes)
    return detections

def __detect_from_image(img_name, detection_model):
    category_index = label_map_util.create_category_index_from_labelmap(files['LABELMAP'])
    
    os.chdir(os.path.join(paths['TAMPON_FOLDER_PATH']))
    
    img = cv2.imread(img_name)
    image_np = np.array(img)
    
    input_tensor = tf.convert_to_tensor(np.expand_dims(image_np, 0), 
                                        dtype=tf.float32)
    detections = __detect_fn(input_tensor, detection_model)
    
    num_detections = int(detections.pop('num_detections'))
    detections = {key: value[0, :num_detections].numpy()
                  for key, value in detections.items()}
    detections['num_detections'] = num_detections
    
    # detection_classes should be ints.
    detections['detection_classes'] = detections['detection_classes'].astype(np.int64)
    
    label_id_offset = 1
    image_np_with_detections = image_np.copy()
    
    viz_utils.visualize_boxes_and_labels_on_image_array(
                image_np_with_detections,
                detections['detection_boxes'],
                detections['detection_classes']+label_id_offset,
                detections['detection_scores'],
                category_index,
                use_normalized_coordinates=True,
                max_boxes_to_draw=5,
                min_score_thresh=.8,
                agnostic_mode=False)
    
    cv2.imwrite(names['OUTPUT_IMG_FILE_NAME'], image_np_with_detections)
    plt.imshow(cv2.cvtColor(image_np_with_detections, cv2.COLOR_BGR2RGB))
    
    os.chdir(PROJECT_PATH)

def __get_last_ckpt():
    ckpt = [elt for elt in os.listdir(paths['CHECKPOINT_PATH']) if 'ckpt' in elt and 'index' in elt]
    list_ckpt = [elt.split('.')[0] for elt in ckpt]
    
    last_record = list_ckpt[0]
    last_record_id = int(list_ckpt[0].split('-')[1])
    
    for i in range(len(list_ckpt)):
        if int(list_ckpt[i].split('-')[1]) > last_record_id:
            last_record_id = int(list_ckpt[i].split('-')[1])
            last_record = list_ckpt[i]

    return last_record


# Load pipeline config and build a detection model
configs = config_util.get_configs_from_pipeline_file(files['PIPELINE_CONFIG'])
detection_model = model_builder.build(model_config=configs['model'], 
                                      is_training=False)

# Restore checkpoint
ckpt = tf.compat.v2.train.Checkpoint(model=detection_model)
ckpt.restore(os.path.join(paths['CHECKPOINT_PATH'], 
                          __get_last_ckpt())).expect_partial()