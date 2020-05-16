import requests
from imageai.Detection import ObjectDetection
import time
import os
import logging
import json

tfl_api = 'https://api.tfl.gov.uk/Place/Type/JamCam'

detector = ObjectDetection()
detector.setModelTypeAsTinyYOLOv3()
detector.setModelPath("models/yolo-tiny.h5")
detector.loadModel()
custom_objects = detector.CustomObjects(person=True)


def get_cameras(api):
    print("loading camera list")
    r = requests.get(api)
    if r.status_code != 200:
        return []
    results = r.json()
    cameras = []
    for result in results:
        camera = {}
        camera['image'] = result['additionalProperties'][1]['value']
        camera['lat'] = result['lat']
        camera['lon'] = result['lon']
        camera['id'] = camera['image'].split("/")[-1].split(".jpg")[0]
        cameras.append(camera)
    return cameras


def get_cameras_images(cameras):
    results = []
    i = 0
    for camera in cameras:
        if i >= 20:
            break
        print("loading camera", camera['id'])
        image = requests.get(camera['image'])
        open("/root/a.jpg", "wb").write(image.content)
        print("counting camera:", camera['id'], camera['lat'], camera['lon'])
        count = count_person(image)
        print("count:", count)
        results.append({"id": camera['id'], "count": count, "position": [
                       camera['lat'], camera['lon']]})
        i += 1
    return results


def count_person(image):
    detections = detector.detectCustomObjectsFromImage(
        custom_objects=custom_objects, input_image="/root/a.jpg", output_image_path="/root/b.jpg", minimum_percentage_probability=60)
    return len(detections)


def send_to_db(camera):
    url = os.getenv('api', "localhost")
    ok_flag = False
    attepmt = 10
    while not ok_flag and attepmt <= 10:
        response = requests.post(url, timeout=50, json=json.dumps(camera))
        if response.status_code == 200:
            logging.info("item sent to db: " + str(camera))
            ok_flag = True
        logging.info("sending to db failed, attempt: ", attepmt)
        attepmt += 1
        time.sleep(15)


print(get_cameras_images(get_cameras(tfl_api)))