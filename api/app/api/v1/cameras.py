from app.api.v1 import api_v1
from app.helpers import Messages, Responses
from app.helpers.utility import res, parse_int, get_page_from_args
from flask import jsonify, request
from app.models import Camera
import os
from datetime import datetime


@api_v1.route('/cameras', methods=['GET'])
def get_cameras():
    items = Camera.get(None, {'name': 1, 'position': 1, 'count':1,'update_time': 1})
    return res([item.as_dict() for item in items])


@api_v1.route('/TLBBTEUqVE', methods=['GET'])
def get_cameras_full():
    items = Camera.get()
    return res([item.as_dict() for item in items])


@api_v1.route('/cameras/<string:pin>', methods=['POST'])
def add_cameras(pin):
    if pin != os.getenv('PIN'):
        return res("", "wrong pin", 403)
    json_dict = request.json
    query = {"name": json_dict['name']}
    cameras = Camera.get(query)
    if len(cameras) <= 0:
        camera = Camera()
        camera.name = json_dict['name']
        camera.position = json_dict['position']
        camera.street = json_dict['street']
        camera.counts=[{"count": json_dict['count'], "update_time":datetime.now()}]
        camera.count = json_dict['count']
        camera.update_time = datetime.now()
        return res(camera.insert())
    camera=cameras[0]
    camera.add_count(json_dict['count'])
    return res()
