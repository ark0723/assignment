from flask import request,render_template
from user_model import users, add_user, add_post, get_posts, like_post, delete_post, delete_user

def register_route(app):
    @app.route("/")
    def index():
        return render_template('index.html')

    @app.route("/users", methods = ['GET', 'POST'])
    def show_users():
        # 전체 사용자 조회
        if request.method == "GET":
            return users
        
        # 사용자 추가
        else:
            new_user_data = request.get_json()
            return add_user(new_user_data)
        
    @app.route("/post/<string:username>", methods = ['GET'])
    def getPosts(username):
        return get_posts(username)
    
    @app.route("/post/<string:username>", methods = ['POST'])
    def addPosts(username):
        new_post_data = request.get_json()
        return add_post(username, new_post_data)
    
    @app.route("/post/<string:username>/<string:title>", methods = ['DELETE'])
    def deletePost(username, title):
        return delete_post(username, title)
    
    @app.route("/post/like/<string:username>/<string:title>", methods = ["PUT"])
    def addLike(username, title):
        return like_post(username, title)
    
    @app.route("/users/<string:username>", methods = ['DELETE'])
    def deleteUser(username):
        return delete_user(username)
