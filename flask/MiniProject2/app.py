from flask import Flask
from user_routes import register_route

app = Flask(__name__)

register_route(app)

if __name__=="__main__":
    app.run(debug = True)

