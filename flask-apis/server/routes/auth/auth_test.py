from flask import Blueprint,jsonify,make_response
from server.resources.apis import AUTH_API_LINK_TEST
from flask_jwt_extended import (
    jwt_required
    )
auth_test_bp = Blueprint('auth_test', __name__,url_prefix=AUTH_API_LINK_TEST)
@auth_test_bp.route('/',methods=["GET"])
@jwt_required()
def index():
    response = {
        "status":"success",
        "message":"Auth Test is success!"
    }
    return make_response(jsonify(response))