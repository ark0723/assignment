from flask_smorest import Blueprint, abort
from flask import request, jsonify
from flask.views import MethodView
from marshmallow import Schema, fields
from db import db
from models import User

# 블루프린트 생성
usr_blp = Blueprint("users", __name__, url_prefix = "/usr", description = "operations on users")

# 스키마 정의
class UserSchema(Schema):
    id = fields.Int(dump_only = True)
    name = fields.Str(required=True)
    email = fields.Str(required=True)

@usr_blp.route("/")
class UserList(MethodView):
    # 데이터 구조 검증: schema사용
    @usr_blp.response(200, UserSchema(many = True))
    def get(self):
         # 전체 유저 데이터 조회
        usrs = User.query.all()
        print(usrs)
        return jsonify([{'id': usr.id, 'name':usr.name, 'email':usr.email, 'posts': [post.id for post in usr.boards]} 
                        for usr in usrs])

    # 유저 생성
    @usr_blp.arguments(UserSchema)
    @usr_blp.response(201, UserSchema)
    def post(self):
        # get data from user
        user_info = request.json
        new_user = User(name = user_info['name'], email = user_info['email'])
        # register new user as object in db
        db.session.add(new_user)
        db.session.commit()
        return jsonify({"msg": f"New User(email: {user_info['email']}) has been created"}), 201
    
# 특정 유저 조회
# 특정 유저 정보 변경
# 유저 탈퇴
@usr_blp.route("/<int:user_id>")
class TheUser(MethodView):
    @usr_blp.response(200, UserSchema)
    def get(self, user_id):
        usr = User.query.get_or_404(user_id)
        print(type(usr)) # QuerySet
        return jsonify({'id': usr.id, 'name': usr.name, 'email':usr.email, 'posts': [i.id for i in usr.boards]})
    
    @usr_blp.arguments(UserSchema)
    @usr_blp.response(200, UserSchema)
    def put(self, user_id):
        usr = User.query.get_or_404(user_id)
        # 유저로부터 유저정보 수정할 내용 받아오기
        usr_info = request.json
        # 내용 수정
        usr.name = usr_info['name']
        usr.email = usr_info['email']
        # 수정내용 DB반영
        db.session.commit()
        return jsonify({"msg": "user information has been successfully updated!"}), 201
    
    @usr_blp.response(204)
    def delete(self, user_id):
        # double check
        checked = input("Are you sure to delete your user info (please say yes(Y) or no(N))? ")
        checked = checked.lower()
        if checked in ['y', 'yes']:
            usr = User.query.get_or_404(user_id)
            # usr객체 삭제
            db.session.delete(usr)
            # 삭제 내역 db반영
            db.session.commit()
            return jsonify({"msg": f"User ID {user_id} has been successfully deleted!"}), 204

        else:
            return ""




