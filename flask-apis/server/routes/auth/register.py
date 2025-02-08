from flask import Blueprint,jsonify,make_response,request
from server.resources.apis import USER_REGISER
#import bcrypt from server __init__ module
from server import bcrypt
#import database and model from models
from server.models import db,Users
from server.utils.helper import uuid_string

#error handling
from sqlalchemy import exc

#register blue print
user_register_bp = Blueprint('register', __name__,url_prefix=USER_REGISER)
@user_register_bp.route('/',methods=["POST"])
def register_user():
    req_body = request.get_json()
    try:
        user_email = req_body['email']
        user_password = req_body['password']
        user_name = req_body['username']
        is_email_exist=Users.query.filter_by(email=user_email).first()
        print("check email exist",is_email_exist)
        if is_email_exist is not None:
            return make_response(jsonify({'status':'fail','msg':'email already exist'}),400)
        is_id_exist=Users.query.filter_by(username=user_name).first()
        print("check id exist",is_id_exist)
        if is_id_exist is not None:
            return make_response(jsonify({'status':'fail','msg':'username already exist'}),400)
        hash_password = bcrypt.generate_password_hash(user_password).decode('utf-8')
        # insert
        print(hash_password)
        new_user = Users(id=uuid_string(),username=user_name,email=user_email,password=hash_password)
        db.session.add(new_user)
        db.session.commit()
        user=Users.query.filter_by(email=user_email).first() 
        # response={"name":user_name,"email":user_email,"customId":user_custom_id,"has":hash_password}
        response={
            "id":user.id,
                  "username":user.username,
                  "email":user.email,
                  "profile":user.profile,
                  "permission":user.permission,
                  "createdAt":user.created_at
                }
        return make_response(jsonify(response),201)
    except exc.SQLAlchemyError as e:
        print("error",e)
        return make_response(jsonify({"status":"failed","msg":"Internal Server Error"}),500)
