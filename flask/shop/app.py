from flask import Flask, render_template
from flask_smorest import Api
from flask_jwt_extended import JWTManager
from database import db
from flask_migrate import Migrate
from route.jwt.jwt_utils import configure_jwt
from route.user import user_blp
import yaml

app = Flask(__name__, static_url_path='/static')

# load .yaml
with open('shop/db.yaml') as f:
    db_info = yaml.full_load(f)

# database connection
app.config['SQLALCHEMY_DATABASE_URI'] = f"mysql+pymysql://{db_info['user']}:{db_info['password']}@{db_info['host']}/{db_info['db']}"
# 객체가 바뀔때마다 트래킹 할지 유무
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Flask-Smorest 설정 추가
# OpenAPI관련 설정
app.config['API_TITLE'] = 'TODO API'
app.config['API_VERSION'] = 'v1'
app.config['OPENAPI_VERSION'] = '3.1.3'
app.config['OPENAPI_URL_PREFIX'] = "/"
# swagger 적용
app.config['OPENAPI_SWAGGER_UI_PATH'] = "/swagger-ui"
app.config['OPENAPI_SWAGGER_UI_URL'] = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"

# db와 app 연결
db.init_app(app)
migrate = Migrate(app, db)

# jwt setting 
configure_jwt(app, db_info['key'])
api = Api(app)

# 블루프린트 등록
api.register_blueprint(user_blp)

@app.route("/")
def index():
    return render_template("index.html")

if __name__ == "__main__":
    # with app.app_context():
        # db.create_all()
    app.run(debug = True)

