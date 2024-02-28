from flask_smorest import Blueprint
from flask import request, jsonify
from flask.views import MethodView
from db import db
from models import Board

board_blp = Blueprint("Boards", __name__, description = "Operations on board", url_prefix='/board')

# /board/
# 전체 게시글을 가져오는 api
# 게시글 작성
@board_blp.route("/")
class BoardList(MethodView):
    def get(self):
        boards = Board.query.all()
        # for board in boards:
            # print("id :", board.id)
            # print("title :", board.title)
            # print("content :", board.content)
            # print("user_id:", board.user_id)
            # print(board.author) -> <User 1> 쿼리셋의 형태로 표현됨
            # print("author :", board.author.name)

        return jsonify([{"id": board.id, 
                         'title':board.title, 
                         "content": board.content, 
                         "author": board.author.name, 
                         "user_id": board.author.id} 
                        for board in boards])

    def post(self):
        # 유저로부터 post할 내용을 받는다 -> json형태로 변환
        data = request.json
        #게시글 작성을 위해서 보드 모델 자체를 가져온다
        new_post = Board(title = data['title'], content = data['content'], user_id = data['user_id'])
        # db에 객체 데이터 추가
        db.session.add(new_post)
        # 데이터베이스에 커밋(db 반영)
        db.session.commit()

        return jsonify({'msg': 'new post has been created successfully'}), 201
    

# /board/board_id
# 하나의 게시글 불러오기
# 특정 게시글 수정하기
# 특정 게시글 삭제하기
@board_blp.route("/<int:board_id>")
class TheBoard(MethodView):
    def get(self, board_id):
        post = Board.query.get_or_404(board_id)
        return jsonify({"id": post.id, 
                        'title':post.title, 
                        "content": post.content, 
                        "author": post.author.name, 
                        "user_id": post.author.id})

    def put(self, board_id):
        # 업데이트할 포스트 불러오기
        post = Board.query.get_or_404(board_id)
        # 사용자로부터 업데이트할 내용 얻기 -> json
        data = request.json
        # 내용 업데이트
        post.title = data['title']
        post.content = data['content']

        # db에 반영
        db.session.commit()

        return jsonify({'msg': 'post has been updated successfully.'}), 201

    def delete(self, board_id):
        # 삭제할 포스트 불러오기
        post = Board.query.get_or_404(board_id, description="post not found, please try another post id")

        # 삭제
        db.session.delete(post)
        db.session.commit()

        return jsonify({'msg': f'post {board_id} has been deleted successfully!'}), 204

