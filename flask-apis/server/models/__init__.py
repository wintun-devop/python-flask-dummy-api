from flask_sqlalchemy import SQLAlchemy
import uuid,datetime

db = SQLAlchemy()

class Users(db.Model):
    __tablename__ = 'ems_user'
    id = db.Column(db.String(), primary_key=True, default=str(uuid.uuid4()))
    email = db.Column(db.String(255), unique=True, nullable=False)
    username =  db.Column(db.String(255), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    profile = db.Column(db.String(255),nullable=True,default=str("profile.png"))
    permission = db.Column(db.String(255),nullable=True,default=str("customer"))
    created_at = db.Column(db.DateTime,default=datetime.datetime.utcnow())
    update_at = db.Column(db.DateTime,onupdate=datetime.datetime.utcnow())

class Products(db.Model):
    __tablename__ = 'ems_product'
    id = db.Column(db.String(), primary_key=True, default=str(uuid.uuid4()))
    name =  db.Column(db.String(255),nullable=False)
    model_no = db.Column(db.String(), unique=True, nullable=False)
    price = db.Column(db.Float,nullable=False,default=0)
    qty = db.Column(db.Integer,nullable=False,default=0)
    description = db.Column(db.Text,nullable=True)
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())
    updated_at = db.Column(db.DateTime, default=db.func.current_timestamp(), onupdate=db.func.current_timestamp())
