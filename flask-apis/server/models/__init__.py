from flask_sqlalchemy import SQLAlchemy
import uuid,datetime

db = SQLAlchemy()

class Users(db.Model):
    __tablename__ = 'ems_user'
    id = db.Column(db.String(), primary_key=True, default=uuid.uuid4)
    email = db.Column(db.String(255), unique=True, nullable=False)
    username =  db.Column(db.String(255), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    profile = db.Column(db.String(255),nullable=True,default=str("profile.png"))
    permission = db.Column(db.String(255),nullable=True,default=str("customer"))
    created_at = db.Column(db.DateTime,default=datetime.datetime.utcnow())
    update_at = db.Column(db.DateTime,onupdate=datetime.datetime.utcnow())
    # Relationship to orders
    orders = db.relationship('Orders', backref='user_order', lazy=True)

class Products(db.Model):
    __tablename__ = 'ems_product'
    id = db.Column(db.String(), primary_key=True, default=uuid.uuid4)
    name =  db.Column(db.String(255),nullable=False)
    model_no = db.Column(db.String(), unique=True, nullable=False)
    price = db.Column(db.Float,nullable=False,default=0)
    qty = db.Column(db.Integer,nullable=False,default=0)
    description = db.Column(db.Text,nullable=True)
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())
    updated_at = db.Column(db.DateTime, default=db.func.current_timestamp(), onupdate=db.func.current_timestamp())
    # Relationship to orders
    orderitems = db.relationship('OrderItems', backref='product_orderitem', lazy=True)

class Orders(db.Model):
    __tablename__ = 'esm_order'
    id = db.Column(db.String(), primary_key=True, default=uuid.uuid4)
    user_id = db.Column(db.String(), db.ForeignKey('ems_user.id'))
    status = db.Column(db.String(50),nullable=False,default='pending')
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())
    updated_at = db.Column(db.DateTime, default=db.func.current_timestamp(), onupdate=db.func.current_timestamp())
    # Relationship to orderItem
    orderitems = db.relationship('OrderItems', backref='order_orderitem', lazy=True)
    
class OrderItems(db.Model):
    __tablename__ = 'esm_orderitem'
    id = db.Column(db.String(), primary_key=True, default=uuid.uuid4)
    order_id = db.Column(db.String(), db.ForeignKey('esm_order.id'))
    product_id = db.Column(db.String(), db.ForeignKey('ems_product.id'))
    prices_at_order =  db.Column(db.Float,nullable=False)
    order_qty = db.Column(db.Integer,nullable=False)
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())
    updated_at = db.Column(db.DateTime, default=db.func.current_timestamp(), onupdate=db.func.current_timestamp())

    
