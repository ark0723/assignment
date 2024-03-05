from db import db 
from werkzeug.security import generate_password_hash, check_password_hash

# User:Todo = 1: N 
class User(db.Model):
    __tablename__="users"
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(30), nullable = False)
    password_hash = db.Column(db.String(300))
    # User객체를 참조하는 참조변수: 특정 사용자가 작성한 모든 todo list 목록
    work_to_do = db.relationship("TODO", back_populates = 'author', lazy = 'dynamic') 

    # encode password
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    # decode password
    def check_password(self, password):
        return check_password_hash(self.password_hash, password)
        

class TODO(db.Model):
    __tablename__="todoList"
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(100), nullable = False)
    completed = db.Column(db.Boolean, default = False)
    # 외래키 참조
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable = False)
    author = db.relationship("User", back_populates = "work_to_do")

