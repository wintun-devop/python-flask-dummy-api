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
from sqlalchemy import exc,or_


from server.resources.apis import USER_LOGIN
from server.resources.apis import REFRESH_TOKEN
from server.resources.apis import USER_LOGOUT

#login blue print
auth_login_bp = Blueprint('auth_login', __name__,url_prefix=USER_LOGIN)
@auth_login_bp.route('/',methods=["POST"])
def login_user():
    req_body = request.get_json()
    try:
        user_email = req_body['username']
        user_password = req_body['password']
        check_email_exist=Users.query.filter_by(email=user_email).first()
        if check_email_exist is not None:
            hash_password = check_email_exist.password
            isPasswordCorrect = bcrypt.check_password_hash(hash_password,user_password)
            # print("passwordCorrect email",isPasswordCorrect)
            if isPasswordCorrect:
                # create the jwt and go make response
                token_attributes={"id":check_email_exist.id,"username":check_email_exist.username,"email":check_email_exist.email}
                access_token = create_access_token(identity=token_attributes,fresh=True)
                refresh_token = create_refresh_token(identity=token_attributes)
                response=jsonify({**token_attributes,"access_token": access_token,"refresh_token": refresh_token,"authenticated":True})
                # optional cookies usage
                set_access_cookies(response, access_token)
                set_refresh_cookies(response, refresh_token)
                return (response,200)
        check_id_exist=Users.query.filter_by(username=user_email).first()
        if check_id_exist is not None:
            hash_password = check_id_exist.password
            isPasswordCorrect = bcrypt.check_password_hash(hash_password,user_password)
            # print("passwordCorrect id",isPasswordCorrect)
            if isPasswordCorrect:
                # create the jwt and go make response
                token_attributes={"id":check_id_exist.id,"username":check_id_exist.username,"email":check_id_exist.email}
                access_token = create_access_token(identity=token_attributes,fresh=True)
                refresh_token = create_refresh_token(identity=token_attributes)
                response=jsonify({**token_attributes,"access_token": access_token,"refresh_token": refresh_token,"authenticated":True})
                # optional cookies usage
                set_access_cookies(response, access_token)
                set_refresh_cookies(response, refresh_token)
                return (response,200)
        else:
            return make_response(jsonify({'status':'error','msg':'user id or password incorrect.'}),400)
    except exc.SQLAlchemyError as e:
        print("error",e)
        return make_response(jsonify({"status":"error","msg":"Internal Server Error"}),500)


#refresh token 
auth_refresh_bp = Blueprint('auth_refresh', __name__,url_prefix=REFRESH_TOKEN)
@auth_refresh_bp.route('/', methods=['POST'])
@jwt_required(refresh=True)  #Require a valid refresh token for this route
def refresh():
    # Set the JWT access cookie in the response
    try:
        current_user = get_jwt_identity()
        # print("referse attribute",current_user)
        access_token = create_access_token(identity=current_user,fresh=False)
        refresh_token = create_refresh_token(identity=current_user)
        respone = jsonify({'refresh': True,'access_token':access_token,'refresh_token':refresh_token,**current_user})
        set_access_cookies(respone, access_token)
        set_refresh_cookies(respone,refresh_token)
        return make_response(respone, 200)
    except:
        return make_response(jsonify({"status":"Login expired!","msg":"Login Again!"}),400)


auth_logout_bp = Blueprint('auth_logout', __name__,url_prefix=USER_LOGOUT)
@auth_logout_bp.route('/', methods=['DELETE'])
@jwt_required()  #Require a valid access token for this route
def logout():
    respone = jsonify({"authenticated": False})
    unset_jwt_cookies(respone)
    return respone, 200