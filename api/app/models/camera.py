from app.helpers.app_context import AppContext as AC
from collections import namedtuple
from datetime import datetime


db = AC().db


class Camera:
    __col__ = db['cameras']
    name = ""
    position = []
    street = ""
    counts = []
    count = ""
    update_time = ""

    def insert(self):
        self.update_time = datetime.now()
        id = self.__col__.insert_one(self.__dict__)
        return str(id.inserted_id)

    def update(self, new_values_query):
        query = {"name": self.name}
        self.__col__.update_one(query, new_values_query)

    def add_count(self, count):
        update_time = datetime.now()
        new_values_query = {"$push":
                                {
                                    "counts": {
                                        "count": count,
                                        "update_time": update_time
                                    }
                                }
                            }
        self.update(new_values_query)
        another_query = {"$set":{
            "count":count,
            "update_time":update_time
        }}
        self.update(another_query)
    
    def as_dict(self):
        result = self.__dict__
        return result

    @staticmethod
    def get(query=None,fields=None):
        results = Camera.__col__.find(query,fields)
        cameras= [Camera.dict_to_object(result) for result in results]
        return cameras

    @staticmethod
    def delete(query):
        Camera.__col__.delete_many(query)
    
    @staticmethod
    def dict_to_object(obj_dict):
        camera = Camera()
        for key in obj_dict:
            if key == "_id":
                continue
            setattr(camera,key,obj_dict[key])
        return camera
