from flask import Flask
from flask_smorest import Api
from api import blp

app = Flask(__name__)

# Flask-Smorest 설정 추가
# OpenAPI관련 설정
app.config['API_TITLE'] = "Book API"
app.config['API_VERSION'] = "v1"
app.config['OPENAPI_VERSION'] = "3.1.3"
app.config['OPENAPI_URL_PREFIX'] = "/"
app.config['OPENAPI_SWAGGER_UI_PATH'] = "/swagger-ui"
app.config['OPENAPI_SWAGGER_UI_URL'] = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"

api = Api(app)
api.register_blueprint(blp)

if __name__ == "__main__":
    app.run(host = "127.0.0.1", port = '8080', debug = True)


# https://copyprogramming.com/howto/error-installing-mysqldb-could-not-find-a-version-that-satisfies-the-requirement-flask-mysqldb
