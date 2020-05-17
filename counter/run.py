import requests
from imageai.Detection import ObjectDetection
import time
import os
import datetime
import json
import numpy as np
import cv2
import wget
import logging

logging.basicConfig()
logging.root.setLevel(logging.INFO)

tfl_api = 'https://api.tfl.gov.uk/Place/Type/JamCam'
model_url='https://github.com/OlafenwaMoses/ImageAI/releases/download/1.0/yolo.h5'

detector = ObjectDetection()
detector.setModelTypeAsYOLOv3()
model_path = os.getenv('model_path', 'models/yolo.h5')
while not os.path.exists(model_path):
    wget.download('https://github.com/OlafenwaMoses/ImageAI/releases/download/1.0/yolo.h5',out=model_path)
detector.setModelPath(model_path)
detector.loadModel()
custom_objects = detector.CustomObjects(person=True)


def get_cameras(api):
    logging.info(str(datetime.datetime.now())+'Loading camera list')
    r = requests.get(api)
    if r.status_code != 200:
        return []
    results = r.json()
    cameras = [{'name': result['additionalProperties'][1]['value'].split('/')[-1].split('.jpg')[0], 'image':result['additionalProperties'][1]['value'], 'position':[
        result['lat'], result['lon']], 'street':result['commonName']} for result in results]
    return cameras


def count_person(camera):
    res = requests.get(camera['image'], stream=True).raw
    image = np.asarray(bytearray(res.read()), dtype='uint8')
    image = cv2.imdecode(image, cv2.IMREAD_COLOR)
    _, detections = detector.detectCustomObjectsFromImage(
        custom_objects=custom_objects, input_image=image, input_type='array', output_type='array', minimum_percentage_probability=50)
    count = len(detections)
    result = {'name': camera['name'], 'count': count, 'position':
                camera['position'], 'street': camera['street']}
    send_to_db(result)


def send_to_db(camera):
    url = os.getenv('api', 'http://127.0.0.1:5000/cameras/1234')
    attepmt = 0
    while True and attepmt <= 10:
        response = requests.post(url, timeout=50, json=camera)
        if response.status_code == 200:
            logging.info(str(datetime.datetime.now())+ 'item sent to db: ' + str(camera))
            break
        logging.info(str(datetime.datetime.now())+ 'sending to db failed, attempt: ' + str(attepmt))
        attepmt += 1
        time.sleep(15)


def run():
    cameras = get_cameras(tfl_api)
    while True:
        for camera in cameras:
            count_person(camera)

run()