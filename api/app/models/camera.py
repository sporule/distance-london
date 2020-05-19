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

    def __init__(self, name, position, street, counts,count,update_time):
        self.name = name
        self.position = position
        self.street = street
        self.counts = counts
        self.count=count
        self.update_time = update_time

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
        result.pop('counts', None)
        return result
    
    def as_dict_full(self):
        result = self.__dict__
        return result

    @staticmethod
    def get(query):
        results = Camera.__col__.find(query)
        cameras= [Camera.dict_to_object(result) for result in results]
        return cameras

    @staticmethod
    def delete(query):
        Camera.__col__.delete_many(query)
    
    @staticmethod
    def dict_to_object(dict):
        camera = Camera(dict['name'],dict['position'],dict['street'],dict['counts'],dict['count'],dict['update_time'])
        return camera
