from flask import Flask
from flask_smorest import Api
from db import db
from models import User, Board
from routes.board import board_blp
from routes.users import usr_blp

app = Flask(__name__)

# 데이터베이스연결설정
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:kr14021428@localhost/post'
# 객체가 바뀔때마다 트래킹 할지 유무
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

#DB와 app객체 연결
db.init_app(app)

# Flask-Smorest 설정 추가
# OpenAPI관련 설정
app.config['API_TITLE'] = 'MY API'
app.config['API_VERSION'] = 'v1'
app.config['OPENAPI_VERSION'] = '3.1.3'
app.config['OPENAPI_URL_PREFIX'] = "/"
# swagger 적용
app.config['OPENAPI_SWAGGER_UI_PATH'] = "/swagger-ui"
app.config['OPENAPI_SWAGGER_UI_URL'] = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"


api = Api(app)
# 블루프린트 등록
api.register_blueprint(board_blp)
api.register_blueprint(usr_blp)

from flask import render_template
@app.route("/manage-boards")
def manage_board():
    return render_template('board.html')

@app.route("/manage-users")
def manage_users():
    return render_template('user.html')

if __name__ == "__main__":
    # crate table schema in the db
    with app.app_context():
        db.create_all()
    app.run(host='127.0.0.1', port = '8080', debug = True)

