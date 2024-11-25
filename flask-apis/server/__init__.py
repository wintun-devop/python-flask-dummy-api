#import to creat app instance
from flask import Flask
#import to configre cors
from flask_cors import CORS
#import server configuration
from . import server_config


def create_app():
    app = Flask(__name__)
    #config app secret
    app.config['SECRET_KEY']=server_config.SERVER_SECRET_KEY
    #configure cors
    CORS(app, resources={r"/*": {"origins": "*"}})
    return app