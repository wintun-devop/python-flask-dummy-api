#import to creat app instance
from flask import Flask
#import to configre cors
from flask_cors import CORS
#import server configuration
from . import server_config
#for database setting
from flask_migrate import Migrate
from server.models import db
#bcrypt for password hasing
from flask_bcrypt import Bcrypt

#declare bcrypt global instance
bcrypt = Bcrypt()

def create_app():
    app = Flask(__name__)
    #config app secret
    app.config['SECRET_KEY']=server_config.SERVER_SECRET_KEY
    #configure cors
    CORS(app, resources={r"/*": {"origins": "*"}})
    #database config
    app.config['SQLALCHEMY_DATABASE_URI'] = server_config.DATABASE_LINK
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)
    migrate = Migrate(app, db)
    bcrypt.init_app(app)
    return app