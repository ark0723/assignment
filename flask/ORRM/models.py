# 모델을 만든다 -> 테이블을 만든다
# 게시글: board
# 유저: user
from db import db

class Board(db.Model):
    __tablename__="boards"
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(100), nullable = False)
    content = db.Column(db.String(300))
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable = False)
    author = db.relationship('User', back_populates = 'boards')

# 테이블관의 관계: https://jammdev.tistory.com/187

class User(db.Model):
    # 테이블 이름
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(30), nullable = False)
    email = db.Column(db.String(100), unique=True, nullable = False)
    # 특정 사용자(Board모델의 author필드와 연결)가 작성한 모든 게시글의 목록
    # lazy ='dynamic': 해당 관계를 나타내는 쿼리셋 반환
    # 쿼리셋은 db로부터 데이터를 즉시 가져오는 것이 아니라 필요할때 해당 쿼리를 실행하여 데이터 로드
    boards = db.relationship('Board', back_populates = 'author', lazy = 'dynamic')


