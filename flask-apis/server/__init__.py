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
#authentication and authorization for jwt
from flask_jwt_extended import JWTManager
from datetime import timedelta

#declare bcrypt global instance
bcrypt = Bcrypt()

def create_app():
    app = Flask(__name__)
    #config app secret
    app.config['SECRET_KEY']=server_config.SERVER_SECRET_KEY
    #configure cors
    CORS(app, resources={r"/*": {"origins": "*"}})
     #configure jwt
    app.config['JWT_SECRET_KEY'] = server_config.JWT_SECRET_KEY
    app.config['JWT_ACCESS_TOKEN_EXPIRES'] = timedelta(hours=10)  # Adjust as needed
    app.config['JWT_REFRESH_TOKEN_EXPIRES'] = timedelta(days=30)  # Adjust as needed
    app.config['JWT_CSRF_IN_COOKIES']=True
    app.config['JWT_REFRESH_TOKEN_ENABLED'] = True
    JWTManager(app)
    #database config
    app.config['SQLALCHEMY_DATABASE_URI'] = server_config.DATABASE_LINK
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)
    migrate = Migrate(app, db)
    bcrypt.init_app(app)
    return app