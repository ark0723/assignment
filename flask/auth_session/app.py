from flask import Flask, render_template, request, redirect, session, flash
from datetime import timedelta

app = Flask(__name__)

# 실제 배포시에는 .env 또는 yaml에 저장해야함
app.secret_key = 'sYaOhzN1tt'
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(days=1)

# admin user
users = {
    'john':"pw123",
    'leo':'pw123'
}

@app.route("/")
def index():
    return render_template('login.html')

@app.route("/login", methods = ['POST'])
def login():
    # 사용자로부터 폼데이터 받음
    username = request.form['username']
    password = request.form['password']

    if username in users and (password == users[username]):
        # 로그인 성공시, 세션 만들기
        session['username'] = username
        session.permanent = True # 세션 유지기간을 활성화

        return redirect('/secret')
    
    else: #로그인 실패
        # 로그인 실패 메시지창 출력
        flash("Invalid username or password!", )
        return redirect('/')

@app.route("/secret")
def secret():
    if 'username' in session:
        return render_template('secret.html')
    else:
        return redirect("/")
    

# 로그아웃
@app.route("/logout")
def logout():
    session.pop('username', None)
    session.clear()
    return redirect("/")

if __name__=='__main__':
    app.run(debug=True)