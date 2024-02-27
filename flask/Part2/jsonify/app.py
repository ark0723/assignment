from flask import Flask, jsonify, request, render_template

app = Flask(__name__)

feeds = {'result': "success", 'data': {1:'data1', 2:'data2'}}

data = [{"items":[{'name':"item1", 'price': 10}]}]

# 전체 게시글 불러오는 api
@app.route("/api/v1/feeds", methods = ['GET'])
def show_all_feeds():    
    return feeds

# 특정 게시글 불러오는 api
@app.route('/api/v1/feeds/<int:feed_id>', methods = ['GET'])
def show_one_feeds(feed_id):
    return feeds['data'][feed_id]

# 게시글 작성
@app.route("/api/v1/feeds", methods =['POST'])
def create_one_feed():
    name = request.form['name']
    age = request.form['age']
    print(name, age)
    return jsonify({'result':'success'})

@app.route("/")
def index():
    return render_template('index.html')

@app.route('/data', methods = ['GET'])
def get_data():
    return {'data': data}

@app.route('/data', methods = ['POST'])
def create_data():
    request_data = request.get_json()
    # key값에 items 없으면, 빈 리스트 추가
    new_data = {"items":request_data.get("items", [])}
    data.append(new_data)
    return new_data, 201

if __name__ == '__main__':
    app.run(debug = True)