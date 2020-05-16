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

    def __init__(self, name, position, street, counts):
        self.name = name
        self.position = position
        self.street = street
        self.counts = counts

    def insert(self):
        self.update_time = datetime.now()
        id = self.__col__.insert_one(self.__dict__)
        return id

    def update(self, new_values_query):
        query = {"name": self.name}
        self.__col__.update_one(query, new_values_query)

    def add_count(self, count):
        update_time = datetime.now()
        new_values_query = {"$push":
                                {
                                    "counts": {
                                        "count": count,
                                        "time": update_time
                                    }
                                }
                            }
        self.update(new_values_query)
        new_values_query = {"$set":{
            "latest_count":count,
            "update_time":update_time
        }}
        self.update(new_values_query)

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
        camera = Camera(dict['name'],dict['position'],dict['street'],dict['counts'])
        return camera
