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
    empty_cameras=['00002.00865', '00002.00635', '00002.00268', '00002.00823', '00001.09800', '00002.00338', '00001.04427', '00001.08853', '00002.00829', '00002.00876', '00001.07303', '00002.00252', '00002.00336', '00002.00851', '00002.00390', '00002.00607', '00002.00335', '00002.00827', '00002.00810', '00002.00878', '00001.09714', '00001.07304', '00002.00854', '00002.00107', '00001.04683', '00002.00254', '00001.04527', '00002.00262', '00001.03668', '00002.00858', '00001.09731', '00002.00347', '00002.00826', '00002.00884', '00001.02431', '00001.08301', '00001.01436', '00001.08955', '00002.00637', '00002.00114', '00001.07302', '00002.00821', '00002.00634', '00002.00110', '00002.00104', '00001.03805', '00002.00621', '00002.00626', '00002.00883', '00002.00877', '00002.00631', '00002.00860', '00001.06605', '00002.00619', '00002.00102', '00002.00327', '00001.01607', '00001.07251', '00002.00450', '00002.00863', '00001.06744', '00001.07315', '00002.00850', '00001.06751', '00001.03769', '00002.00378', '00002.00333', '00002.00332', '00001.07313', '00002.00633', '00002.00624', '00002.00636', '00002.00857', '00002.00830', '00002.00638', '00002.00101', '00002.00337', '00002.00869', '00002.00822', '00002.00831', '00001.07320', '00002.00115', '00002.00856', '00001.04518', '00002.00348', '00001.03488', '00002.00882', '00001.03553', '00002.00632', '00002.00116', '00001.03766', '00002.00868', '00002.00629', '00002.00403', '00002.00342', '00001.07314', '00002.00859', '00001.09057']
    while True:
        for camera in cameras:
            if camera['name'] not in empty_cameras:
                count_person(camera)

run()
