# -*- coding: utf-8 -*-
"""
Created on Fri Jun 18 15:22:00 2021

@author: vwork
"""

import os
import app, app2, app3, app4

PROJECT_PATH = os.path.join(os.path.split(os.path.dirname(__file__))[0])

PAGES = {
    "Accueil": app,
    "Détéction": app2,
    "Cartographie": app3,
    "Rapport": app4
}

names = {
    'MODEL_NAME' : 'my_ssd_mobnet',
    'LABEL_MAP_NAME' : 'label_map.pbtxt',
    'OUTPUT_IMG_FILE_NAME': 'img_analyzed.jpg',
    'DATA_NAME' : 'data.csv'
    }

paths = {
    'TAMPON_FOLDER_PATH' : os.path.join(PROJECT_PATH,'documents', 'images'),
    'CHECKPOINT_PATH': os.path.join(PROJECT_PATH, 'documents', 'models',
                                    names['MODEL_NAME']),
    'ANNOTATION_PATH': os.path.join(PROJECT_PATH, 'documents', 'models',
                                    names['MODEL_NAME'], 'annotation'),
    'API' : os.path.join(PROJECT_PATH,'documents', 'Tensorflow_API'),
    'PROTOC_PATH': os.path.join(PROJECT_PATH,'documents', 'Tensorflow_API', 
                                'protoc'),
    'APIMODEL_PATH': os.path.join(PROJECT_PATH,'documents', 'Tensorflow_API', 
                                'models'),
    'CODE_PATH': os.path.join(PROJECT_PATH, 'code')
    
    }

urls = {
        'protoc' : "https://github.com/protocolbuffers/protobuf/releases/download/v3.15.6/protoc-3.15.6-win64.zip",
        'tsf_model' : "https://github.com/tensorflow/models"
        }

files = {
    'PIPELINE_CONFIG':os.path.join(paths['CHECKPOINT_PATH'], 'pipeline.config'),
    'LABELMAP': os.path.join(paths['ANNOTATION_PATH'], names['LABEL_MAP_NAME']),
    'OUT_IMG' : os.path.join(paths['TAMPON_FOLDER_PATH'], 
                             names['OUTPUT_IMG_FILE_NAME']),
    'data' : os.path.join(paths['CODE_PATH'], names['DATA_NAME'])
    
}

