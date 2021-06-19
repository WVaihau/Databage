# -*- coding: utf-8 -*-
"""
Created on Fri Jun 18 20:45:37 2021

@author: vwork
"""

from model import paths, urls
import os

if os.name=='nt':
    os.system('pip install wget')
    import wget

for path in paths.values():
    if not os.path.exists(path):
        if os.name == 'nt':
            os.system('mkdir ' + path)

if not os.path.exists(os.path.join(paths['APIMODEL_PATH'], 'research', 'object_detection')):
    os.system(f"git clone {urls['tsf_model']} {paths['APIMODEL_PATH']}")

if len(os.listdir(paths['PROTOC_PATH'])) == 0:
    wget.download(urls['protoc'])
    
    os.system('move protoc-3.15.6-win64.zip ' + paths['PROTOC_PATH'])
    
    os.system(f"cd {paths['PROTOC_PATH']} && tar -xf protoc-3.15.6-win64.zip")

    os.environ['PATH'] += os.pathsep + os.path.abspath(os.path.join(
        paths['PROTOC_PATH'], 'bin'))

    research_folder = os.path.join(paths['APIMODEL_PATH'], 'research')
    slim_fold = os.path.join(research_folder, 'slim')
    
    os.system(f"cd {research_folder} && protoc object_detection/protos/*.proto --python_out=. && copy object_detection\\packages\\tf2\\setup.py setup.py && python setup.py build && python setup.py install")
    
    os.system(f"cd {slim_fold} && pip install -e .")