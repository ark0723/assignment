from flask import Flask, render_template, url_for, request, redirect

app = Flask(__name__)

# 사용자 데이터
users = [
    {"username": "traveler", "name": "Alex"},
    {"username": "photographer", "name": "Sam"},
    {"username": "gourmet", "name": "Chris"}
]

@app.route("/")
def index():
    return render_template("index.html", users = users)

@app.route("/add", methods = ['GET', 'POST'])
def add_user():
    if request.method == 'POST':
        username = request.form['username']
        name = request.form['name']
        users.append({'username': username, "name":name})
        return redirect(url_for('index'))
    return render_template('add_user.html')

@app.route("/edit/<username>", methods = ['GET', 'POST'])
def edit_user(username):
    user = next((user for user in users if user['username'] == username),None)
    if not user:
        return redirect("/")
    
    if request.method == 'POST':
        user['name'] = request.form['name']
        return redirect(url_for('index'))
    
    return render_template('edit_user.html', user = user)

@app.route("/delete/<username>")
def delete_user(username):
    for user in users:
        if user['username']==username:
            users.remove(user)
    return redirect(url_for('index'))

if __name__ == "__main__":
    app.run(debug = True)