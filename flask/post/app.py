from flask import Flask, render_template
from flask_smorest import Api
from routes import create_posts_blueprint

app = Flask(__name__)

# blueprint 설정 및 등록
app.config['API_TITLE'] = 'My API'
app.config['API_VERSION'] = '1.0.0'
app.config['OPENAPI_VERSION'] = '3.1.3'
app.config['OPENAPI_URL_PREFIX'] = "/"
app.config['OPENAPI_SWAGGER_UI_PATH'] = "/swagger-ui"
app.config['OPENAPI_SWAGGER_UI_URL'] = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"
app.config['JSON_AS_ASCII'] = False

api = Api(app)
post_blp = create_posts_blueprint()
api.register_blueprint(post_blp)

@app.route("/")
def index():
    return render_template("posts.html")

if __name__ == "__main__":
    app.run(host = '127.0.0.1', port = '8080', debug = True)
