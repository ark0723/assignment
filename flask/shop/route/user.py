from flask import request, jsonify, redirect
from flask_smorest import Blueprint
from flask_jwt_extended import create_access_token, create_refresh_token, jwt_required, get_jwt_identity, get_jwt

from werkzeug.security import check_password_hash
from jwt.blocklist import add_to_blocklist
from models import User, db
import re

# check password validation 
def regex_password(pw):
    # 최소한 하나의 영문자 포함(대문자 소문자)
    # 최소한 하나의 숫자 포함
    # @!%*#?& 특수문자 포함
    # 8~16글자 
    # ^는 문자열의 시작을 의미합니다.
    # ?=.*[A-Za-z]는 대문자, 소문자 최소한의 하나 이상의 영문자를 검색하는 부분입니다.
    # ?=.*\d는 최소한 하나의 숫자를 포함하는지를 검색하는 부분입니다. \d는 숫자를 의미합니다.( 0 ~ 9 )
    # ?=.*[@$!%*#?&]는 [] 안에 있는 특수문자가 존재하는지 검색하는 부분입니다.
    # (?!.*(ABC|BCD|CDE|123|234)) 순차적인 숫자, 문자가 포함되는 않는지 검색
    # [A-Za-z\d@$!%*#?&]{8,16}$ 부분은 총 최소 8글자 최대 16글자로 되어있는지 체크하는 부분입니다.
    pattern = r'^(?=.*[A-Za-z])(?=.*\d)(?=.*[@$!%*#?&])(?!.*(ABC|BCD|CDE|123|234))[A-Za-z\d@$!%*#?&]{8,16}$'
    if re.match(pattern, pw):
        return True
    return False


user_blp = Blueprint("user", __name__, url_prefix = "/user", description = "User API")

@user_blp.route("/mypage", methods = ["GET"])
@jwt_required()
def show_my_page():
    # 현재 로그인된 유저 이름 확인
    # Access the identity of the current user with get_jwt_identity
    username = get_jwt_identity()
    user = User.query.filter_by(username = username).first()
    return jsonify({'id': user.id, 'username': user.username}), 200

@user_blp.route("/login", methods =['POST'])
@jwt_required()
def login():    
    username = request.form['username']
    password = request.form['password']

    if not username or (not password):
        # return jsonify({"msg": "Missing User Name or Password!"}), 400
        return redirect("/")

    # load User instance from username, password
    user = User.query.filter_by(username = username).first()

    # if user object exists and password is identical to the user's password in db.
    if user and check_password_hash(user.password_hash, password):
        access_token = create_access_token(identity = username)
        refresh_token = create_refresh_token(identity = username)
        return jsonify(access_token = access_token, refresh_token = refresh_token)
    else:
        return redirect("/")

@user_blp.route("/logout", methods = ['POST'])
@jwt_required()
def logout():
    jti = get_jwt()['jti']
    add_to_blocklist(jti)
    return jsonify({"msg": "Log Out"}), 200

@user_blp.route("/register", methods =['POST'])
def register(): # 회원가입
    data = request.get_json()

    # 데이터 전부 있는지 체크
    if 'username' not in data or ('password' not in data):
        return jsonify({"msg": "missing username or password!"})
    
    # password 유효성 검사 
    if not regex_password(data['password']):
        return jsonify({"msg": "password must include at least (8 characters long, 1 alphabet letter, 1 number, one of (@$!%*#?&), and three consecutive characters are not allowed)"})

    # save user data in database
    new_user = User(username = data['username'], password_hash = User.set_password(db['password']))


@user_blp.route("/delete-account", methods = ['DELETE'])
@jwt_required()
def delete_account():
    username = get_jwt_identity()
    user = User.query.filter_by(username = username).first()
    db.session.delete(user)
    db.session.commit()

    return jsonify({"msg": "your account has been deleted successfully", "User Name": username}), 400

    


