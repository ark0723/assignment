from flask import Flask
from flask_login import LoginManager
from models import User
from routes import configure_route

app = Flask(__name__)
app.secret_key = 'YoNC2yXanHTKd2xbgiZY'

# 로그인매니저 초기화
login_manager = LoginManager()
login_manager.init_app(app)
# 로그인 화면의 이름 지정
login_manager.login_view = 'login'
configure_route(app)

# 세션에 저장된 유저 ID 로부터 유저객체를 다시 로드하는데 쓰임
@login_manager.user_loader
def load_user(user_id):
    return User.get(user_id)

if __name__ == "__main__":
    app.run(debug= True)