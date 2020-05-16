from flask import Flask
import pymongo
from app.helpers.app_context import AppContext as AC
import os


def create_app(config_object):
    """
    create_app   creates an instance of the flask app

    Args:
        config_object (string): config file

    """
    app = Flask(__name__)

    # Load config profile
    app.config.from_object(config_object)

    # initiate plugins
    ac = AC()
    load_configs_to_environ(app,["MONGO_URI","PIN"])
    db = pymongo.MongoClient(os.getenv('MONGO_URI'))
    ac.db= db["distance-london"]
    
    # register blueprints
    from app.api import API
    for name in API:
        BP = API[name]
        app.register_blueprint(
            BP['route'], url_prefix=BP['url_prefix'])
    return app

def load_configs_to_environ(app,configs):
    for config in configs:
        if(len(app.config[config]))>0:
            os.environ[config]=app.config[config]