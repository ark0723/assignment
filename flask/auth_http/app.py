from flask import Flask, jsonify, render_template
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash

# https://flask-httpauth.readthedocs.io/en/latest/

app = Flask(__name__)
auth = HTTPBasicAuth()

users = {
    'admin': generate_password_hash("secret"),
    'guest': generate_password_hash("guest")
}

@app.route("/")
def index():
    return render_template('index.html')

@auth.verify_password
def verify_password(username, password):
    if username in users and check_password_hash(users.get(username), password):
        return username
    
@app.route("/protected")
@auth.login_required
def protected():
    return render_template("secret.html")

if __name__ == "__main__":
    app.run(debug=True)