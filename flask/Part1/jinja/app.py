from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    data = {
        'title': 'Flask Jinja Template',
        'user': 'Ara',
        'is_admin': True,
        'items': ['item1', 'item2','item3']
    }
    # 1. rendering할 html 파일명 , html로 넘겨줄 데이터 입력
    return render_template('index.html', title = data['title'], user = data['user'], is_admin = data['is_admin'], items = data['items'])

if __name__ == '__main__':
    app.run(host = '127.0.0.1', port = '8080', debug = True)