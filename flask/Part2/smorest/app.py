# pip install flask-smorest
# REST API를 쉽게 작성할 수 있도록 도와주는 flask library
# Flask-RESTful보다 더 많은 기능과 OpenAPI(Swagger)문서 자동 생성 기능을 제공

from flask import Flask
from flask_smorest import Api
from api import blp


app = Flask(__name__)

# OpenAPI관련 설정
app.config['API_TITLE'] = "My API"
app.config['API_VERSION'] = "v1"
app.config['OPENAPI_VERSION'] = "3.1.3"
app.config['OPENAPI_URL_PREFIX'] = "/"
app.config['OPENAPI_SWAGGER_UI_PATH'] = "/swagger-ui"
app.config['OPENAPI_SWAGGER_UI_URL'] = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"

api = Api(app)
api.register_blueprint(blp)

if __name__ == "__main__":
    app.run(host = "127.0.0.1", port = "8080", debug=True)
