from flask.views import MethodView
from flask_smorest import Blueprint, abort
from schemas import BookSchema


blp = Blueprint('books', 'books', url_prefix = "/books", description = "Operations on books")

# 데이터 저장
books = []

#{"title":"sapiens”, "author":"Yuval Noah Harari" ,"publish": "2011-02-10"}
#{"title”:”animal farm”, "author”:”George Orwell” ,"publish": “1945-08-17”}


# 'ItemList' 클래스 - GET 및 POST 요청을 처리
@blp.route("/")
class BookList(MethodView):
    @blp.response(200, BookSchema(many=True))
    def get(self):
        return books
    
    @blp.arguments(BookSchema)
    @blp.response(201, description="Add a new book")
    def post(self, new_book):
        # id: 1,2,3,....
        new_book['id'] = len(books) + 1
        books.append(new_book)
        return new_book
    
@blp.route("/<int:id>")
class Book(MethodView):
    @blp.response(200)
    def get(self, id):
        book = next((book for book in books if book['id'] == id), None)

        if not book:
            abort(404, message = "Book not found")
        
        print(dir(book))
        print(type(book))
        return book
    
    @blp.arguments(BookSchema)
    @blp.response(200, description= "Book info updated")
    def put(self, new_data, id):
        book = next((book for book in books if book['id'] == id), None)
        print(book)
        if not book:
            abort(404, message = "book not found")
        book.update(new_data)

        return book
    
    def delete(self, id):
        global books

        if not any(book for book in books if book['id'] == id):
            abort(404, message = "Book not found")
        
        books = [book for book in books if book['id'] != id]
        return ""
