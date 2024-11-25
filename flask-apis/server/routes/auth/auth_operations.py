from flask import Blueprint,jsonify,make_response,request

#import token services
from flask_jwt_extended import (
                                jwt_required,
                                create_access_token,
                                create_refresh_token,
                                get_jwt_identity,
                                unset_jwt_cookies,
                                set_access_cookies,
                                set_refresh_cookies
                                )
#import bcrypt from server __init__ module
from server import bcrypt
#import database and model from models
from server.models import db,Users
#error handling
from sqlalchemy import exc
import json

from server.resources.apis import USER_LOGIN
from server.resources.apis import REFRESH_TOKEN
from server.resources.apis import USER_LOGOUT

#login blue print
auth_login_bp = Blueprint('auth_login', __name__,url_prefix=USER_LOGIN)
@auth_login_bp.route('/',methods=["POST"])
def login_user():
    req_body = request.get_json()
    try:
        user_email = req_body['user_email']
        user_password = req_body['user_password']
        check_exist=Users.query.filter_by(email=user_email).first()
        # print("check email exist",check_exist)
        if check_exist is None:
            return make_response(jsonify({'status':'fail','msg':'email or password incorrect.'}),400)
        hash_password = check_exist.password
        # print("hash_password",hash_password)
        isPasswordCorrect = bcrypt.check_password_hash(hash_password,user_password)
        print("passwordCorrect",isPasswordCorrect)
        if isPasswordCorrect:
            # create the jwt and go make response
            token_attributes={"id":check_exist.id,"name":check_exist.name,"email":check_exist.email}
            access_token = create_access_token(identity=token_attributes,fresh=True)
            refresh_token = create_refresh_token(identity=token_attributes)
            print(access_token)
            response=jsonify({**token_attributes,"access_token": access_token,"refresh_token": refresh_token,"authenticated":True})
            # optional cookies usage
            # a = jsonify()
            # set_access_cookies(response, access_token)
            # set_refresh_cookies(response, refresh_token)
            # set_access_cookies(response=response,encoded_access_token="eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmcmVzaCI6dHJ1ZSwiaWF0IjoxNzMyNTQwNjMyLCJqdGkiOiI5N2U2NjE0ZS04NDY1LTRmMzYtYjFjNC1lNzgwNzk4MDU0MzgiLCJ0eXBlIjoiYWNjZXNzIiwic3ViIjp7ImlkIjoiNWQxNzhkOTktNGI5MC00M2RiLTg5NTktMmZkZjk2NjYwODAwIiwibmFtZSI6IldpbnR1biIsImVtYWlsIjoid2ludHVuMTAxQGdtYWlsLmNvbSJ9LCJuYmYiOjE3MzI1NDA2MzIsImNzcmYiOiIzNDRlYjdlOS1kYzk5LTQwNWUtYTdlNi02ZWYzY2YxYjljODIiLCJleHAiOjE3MzI1NzY2MzJ9.hwic1OfD9H-28CNaJLz3PI5ozh6MPmaYxk6Kd1NLsTc")
            # set_refresh_cookies(jsonify({"login":True}),"eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmcmVzaCI6dHJ1ZSwiaWF0IjoxNzMyNTQwNzkwLCJqdGkiOiIyZWFlMmRmMi1hMDdmLTRhNzktOWVjMS04YzgyNWEyNzQ0ZWEiLCJ0eXBlIjoiYWNjZXNzIiwic3ViIjp7ImlkIjoiNWQxNzhkOTktNGI5MC00M2RiLTg5NTktMmZkZjk2NjYwODAwIiwibmFtZSI6IldpbnR1biIsImVtYWlsIjoid2ludHVuMTAxQGdtYWlsLmNvbSJ9LCJuYmYiOjE3MzI1NDA3OTAsImNzcmYiOiIxOWI1NzU2Ny0wN2U4LTQ1ZTItYWE3ZS0wNTMxYmI3ODRlNmMiLCJleHAiOjE3MzI1NzY3OTB9.ytJm45vtcodc_95lxuYemsv3u2pHtwMoDFWoEU6Ybj0") 
            return (response,200)
        else:
            return make_response(jsonify({'status':'fail','msg':'email or password incorrect.'}),400)
    except exc.SQLAlchemyError as e:
        print("error",e)
        return make_response(jsonify({"status":"failed","msg":"Internal Server Error"}),500)


#refresh token 
auth_refresh_bp = Blueprint('auth_refresh', __name__,url_prefix=REFRESH_TOKEN)
@auth_refresh_bp.route('/', methods=['GET'])
@jwt_required(refresh=True)  #Require a valid refresh token for this route
def refresh():
    print("refresh")
    # Set the JWT access cookie in the response
    try:
        current_user = get_jwt_identity()
        print("referse attribute",current_user)
        access_token = create_access_token(identity=current_user,fresh=False)
        refresh_token = create_refresh_token(identity=current_user)
        respone = jsonify({'refresh': True,'access_token':access_token,'refresh_token':refresh_token,**current_user})
        """ set_access_cookies(respone, access_token.encode('utf-8'))
        set_refresh_cookies(respone,refresh_token.encode('utf-8')) """
        return make_response(respone, 200)
    except:
        return make_response(jsonify({"status":"Login expired!","msg":"Login Again!"}),400)


auth_logout_bp = Blueprint('auth_logout', __name__,url_prefix=USER_LOGOUT)
@auth_logout_bp.route('/', methods=['DELETE'])
@jwt_required()  #Require a valid access token for this route
def logout():
    respone = jsonify({'logout': True})
    # unset_jwt_cookies(respone)
    return respone, 200