from flask import Flask, Blueprint, request, render_template, redirect, url_for
from product_db.mysql_db import conn_mysql

app = Flask(__name__, static_url_path="/static")

@app.route("/")
def index():
    conn = conn_mysql()
    cursor = conn.cursor()
    sql = 'select * from product'
    cursor.execute(sql)
    kream_item_list = cursor.fetchall()
    return render_template('index.html', data_list = kream_item_list)

category_dict = {'1':"outer", "2": "top", "3":"bottom", "4": "shoes", "5": "bag", "6":"wallet", "7":"watch", "8":"accessory"}


# 사용자로부터 이메일 받아서 MySql DB에 저장
@app.route("/filter", methods = ['GET'])
def filter():
    category_id  = request.args.get('category')
    keyword = request.args.get('keyword')
    print(category_id, keyword)

    # sql db
    conn = conn_mysql()
    cursor = conn.cursor()

    if category_id != "0": 
        cursor.execute("select * from product where category = %s and (locate(%s, brand) > 0 or locate(%s, title) > 0)", 
                        (category_dict[category_id], keyword, keyword))
        kream_item_list = cursor.fetchall()
        return render_template('index.html', data_list = kream_item_list)

    else: 
        if keyword:
            cursor.execute("select * from product where locate(%s, brand) > 0 or (locate(%s, title) > 0)", (keyword, keyword))
            kream_item_list = cursor.fetchall()
            return render_template('index.html', data_list = kream_item_list)
        else: # keyword == ""
            return redirect("/")


if __name__=="__main__":
    app.run(host = '0.0.0.0', port = '8080', debug = True)