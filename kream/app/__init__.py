from flask import Flask, render_template, request
from product_db.mysql_db import conn_mysql
from flask_paginate import Pagination
from flask_cors import CORS
from tool import makePage, writeSQL


app = Flask(__name__, static_url_path="/static")
# 모든 경로에 대해 CORS설정을 허용
CORS(app)


category_dict = {'0': None, '1':"outer", "2": "top", "3":"bottom", "4": "shoes", "5": "bag", "6":"wallet", "7":"watch", "8":"accessory"}

# how many product list would be diplayed on a page?
per_page = 6

# pagination 참조
# https://stackoverflow.com/questions/74520043/flask-pagination-without-sqlalchemy
# https://panda5176.tistory.com/12


# mysql db
conn = conn_mysql()
cursor = conn.cursor()


# methods = ['GET']
@app.route('/')
def index(cursor = cursor):

    # sql query
    sql = writeSQL()
    count_sql = sql.replace("*", "count(*)")
        
    # 전체 데이터가 총 몇개인지 체크
    cursor.execute(count_sql)
    total_count = cursor.fetchone()['count(*)']
    
    #pagination 객체 생성
    pagination, offset = makePage(total_count = total_count, per_page = per_page)

    # 한 페이지에 보여줄 데이터를 가져온다
    sql += " limit %s offset %s"
    cursor.execute(sql, (per_page, offset))
    items_per_page = cursor.fetchall()
    

    # search: 페이지 검색 기능, bs_version: bootstrap 사용시 이를 활용할 수 있게 버전을 알려줌
    return render_template('index.html', data_list = items_per_page, 
                           pagination = pagination, search = True, bs_version = 5.3, show_single_page = True)

@app.route("/filter", methods = ['GET'])
def filter(cursor = cursor):
    # get: paramters
    category_id  = request.args.get('category')
    # [None, "outer", "top", "bottom", etc ...]
    category = category_dict[category_id] 
    keyword = request.args.get('keyword')
    sortID = request.args.get("sortID")
    print(sortID)

    # sql query
    sql = writeSQL(category = category, keyword = keyword, sortby = sortID)
    count_sql = sql.replace("*", "count(*)")

    # 필터링 된 전체 데이터가 총 몇개인지 체크
    cursor.execute(count_sql)
    total_count = cursor.fetchone()['count(*)']
    
    #pagination 객체 생성
    pagination, offset = makePage(total_count = total_count, per_page = per_page)

    # 한 페이지에 보여줄 데이터를 가져온다
    sql += " limit %s offset %s"
    cursor.execute(sql, (per_page, offset))
    items_per_page = cursor.fetchall()

    return render_template('index.html', data_list = items_per_page, 
                           pagination = pagination, search = True, bs_version = 5.3, show_single_page = True)
    


if __name__=="__main__":
    app.run(host = '0.0.0.0', port = '8080', debug = True)