from flask import Blueprint,jsonify,make_response

api_test_bp = Blueprint('test', __name__)

@api_test_bp.route('/',methods=["GET"])
def index():
    response = {
        "status":"success",
        "message":"API Server is working well!"
    }
    return make_response(jsonify(response))