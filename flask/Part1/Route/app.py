from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

@app.route("/")
def main():
    return "<h1>Hello, This is my webpage!</h1>"

# alt + shift + 화살표 위/아래
@app.route("/about")
def about():
    return "<h1>This is Main Page</h1>"

# 동적으로 URL 파라미터 값을 받아서 처리해준다
@app.route("/user/<username>")
def user_profile(username):
    return f'User Name : {username}'

# 숫자를 파라미터로 받고싶다면, 데이터타입 지정 필요
@app.route("/userID/<int: number>")
def user_profile(number):
    return f'User Name : {number}'

# post 요청 날리는 법
# (1) postman
# (2) requests # pip install requests
@app.route("/test")
def test():
    url = 'http://127.0.0.1:8080/submit'
    data = 'test data'
    res = requests.post(url = url, data = data).status_code

    return jsonify(res)

@app.route("/submit", methods = ['GET', 'POST', "PUT", 'DELETE'])
def submit():
    if request.method == "GET":
        # request.args.get()
        print("GET method")

    elif request.method == "POST":
        # request.form("")
        print("POST method")

    elif request.method =="PUT":
        print("PUT method", request.data)

    else: 
        print("Delete Method")
    
    return ""
    
if __name__=="__main__":
    app.run(host = "127.0.0.1", port = "8080", debug = True)
