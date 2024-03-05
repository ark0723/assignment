from flask import request, jsonify
from flask_smorest import Blueprint
from flask_jwt_extended import create_access_token
from model import User
from werkzeug.security import check_password_hash

auth_blp = Blueprint("auth", __name__, url_prefix = '/login', description = 'Operation on user authentication')

@auth_blp.route("/", methods = ['POST'])
def login():
    if not request.is_json:
        print(request.is_json)
        return jsonify({"msg": "missing json in request"}), 400
    
    username = request.json.get("name", None)
    password = request.json.get("password", None)
    if not username or not password:
        return jsonify({"msg": "Missing User Name or password"}), 400
    
    user = User.query.filter_by(name = username).first()
    print('user: ', user)
    print('check pw: ', check_password_hash(user.password_hash, password))

    if user and check_password_hash(user.password_hash, password):
        access_token = create_access_token(identity=username)
        print('access token: ', access_token)
        return jsonify(access_token = access_token)
    
    else:
        return jsonify({"msg": "Invalid username or password"}), 401