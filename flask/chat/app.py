from flask import Flask, render_template
from flask_socketio import SocketIO

app = Flask(__name__)
app.config['SECRET_KEY'] = "MySecret"
socket = SocketIO(app)
# 라우팅
# 채팅 기능 실험위한 html
@app.route("/")
def index():
    return render_template('index.html')

def msg_received(methods = ['GET', 'POST']):
    print("CALLBACK : msg received")
    #DB connection - > save


# 소켓 연결: 클라이언트 - 서버
@socket.on('my event')
def handle_chat_event(json, methods = ['GET', 'POST']):
    print(f'데이터 수신 완료: {json}')
    socket.emit('my response', json, callback =msg_received)



if __name__=="__main__":
    socket.run(app, host = '127.0.0.1', port = "8080", debug = True)
