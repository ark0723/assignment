from flask import request, make_response, jsonify
import json
from flask_smorest import Blueprint, abort
from db_conn import conn_mysql

def create_posts_blueprint():
    # db coneection
    conn = conn_mysql()

    post_blp = Blueprint("post", __name__, url_prefix = "/post", description = "posts api")

    @post_blp.route("/", methods = ['GET', "POST"])
    def posts():
        cursor = conn.cursor()
        
        # 전체 게시글 조회
        if request.method == 'GET':
            sql = "SELECT * FROM post"
            cursor.execute(sql)

            posts = cursor.fetchall()

            # post_list = [post for post in posts]

            # return make_response(json.dumps(post_list, ensure_ascii= False, indent = 4, default = str))
            return posts
        
        # 게시글 생성
        elif request.method == "POST":
            title = request.json.get("title")
            content = request.json.get("content")

            if not title or not content: 
                abort(400, message = "title 또는 content가 없습니다.")

            sql = "INSERT INTO post(title, content) VALUES(%s, %s)"
            cursor.execute(sql, (title, content))
            conn.commit()

            return jsonify({"message": "success"}), 201
        
    # 특정 게시글 조회, 수정, 삭제
    @post_blp.route("/<int:id>", methods = ["GET", "PUT", "DELETE"])
    def post(id):
        cursor = conn.cursor()

        if request.method == 'GET':
            sql = "SELECT * FROM post WHERE id=%s"
            cursor.execute(sql, (id,))
            post = cursor.fetchone()

            if not post:
                abort(400, message = "해당 게시글이 없습니다.")
            
            return post
        
        elif request.method == "PUT":
            # data = request.json
            # title = data['title']
            title = request.json.get("title")
            content = request.json.get("content")

            if not title or not content:
                abort(400, message = "title 또는 content가 없습니다.")

            sql = "SELECT * FROM posts WHERE id=%s"
            cursor.execute(sql, (id,))
            post = cursor.fetchone()

            if not post:
                abort(404, message="해당 게시글이 없습니다.")

            sql = "UPDATE posts SET title=%s, content=%s WHERE id=%s"
            cursor.execute(sql, (title, content, id))
            conn.commit()

            return jsonify({"message": "Successfully updated title & content"})
        
        elif request.method == "DELETE":
            sql = "SELECT * FROM posts WHERE id=%s"
            cursor.execute(sql, (id,))
            post = cursor.fetchone()

            if not post:
                abort(404, message="해당 게시글이 없습니다.")

            sql = "DELETE FROM posts WHERE id=%s"
            cursor.execute(sql, (id,))
            conn.commit()

            return jsonify({"message": "Successfully deleted post"})

    return post_blp


        


