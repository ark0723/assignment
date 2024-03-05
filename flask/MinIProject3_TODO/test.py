from db import db
from app import app
from model import User

with app.app_context():
    new_user = User(name='newuser')
    new_user.set_password('user123') # 비밀번호를 해쉬화하는 부분이 추가되어야 함.
    db.session.add(new_user)
    db.session.commit()
    user = User.query.filter_by(name='newuser').first()
    print(user)