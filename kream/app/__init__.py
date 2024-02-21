from flask import Flask, Blueprint, request, render_template, redirect, url_for
from product_db.mysql_db import conn_mysql
from flask_paginate import Pagination, get_page_args


app = Flask(__name__, static_url_path="/static")

category_dict = {'0': None, '1':"outer", "2": "top", "3":"bottom", "4": "shoes", "5": "bag", "6":"wallet", "7":"watch", "8":"accessory"}

# how many product list would be diplayed on a page?
per_page = 6

def filter_sql(category = None, keyword = ""):
    sql = "select * from product"
    count_sql = "select count(*) from product"

    if category != None:
        add = " where category = %s and (locate(%s, brand) > 0 or locate(%s, title) > 0)"
        sql += add
        count_sql += add
    else:
        if keyword:
            add = " where locate(%s, brand) > 0 or (locate(%s, title) > 0)"
        else:
            return count_sql, sql
        sql += add
        count_sql += add
    
    return count_sql, sql

def sort_sql(sql, price = ''):
    limit = " limit %s offset %s"

    if price == None:
        sql += limit

    elif price == '0':
        sql += ' order by price' + limit

    else: 
        sql += ' order by price desc' + limit

    return sql

# pagination 참조
# https://stackoverflow.com/questions/74520043/flask-pagination-without-sqlalchemy
# https://panda5176.tistory.com/12


# methods = ['GET']
@app.route('/', methods = ['GET'])
def index():
    # 아이템 10개씩 페이지에 보여주기
    # return(page, per_page, offset)
    page, _, offset = get_page_args(per_page = per_page)
    price = request.args.get("price")
    # page: current page(default: 1) -> 페이지 링크 누르면 2, 3, 4, ...
    # offset: page에 따라 몇번째 데이터부터 보여줄지

    conn = conn_mysql()
    cursor = conn.cursor()
 
    count_sql, sql = filter_sql(category = None, keyword = "")
    print(count_sql)
    print(sql)
    sql = sort_sql(sql, price = price)
    print(sql)
    # 전체 데이터가 총 몇개인지 체크
    cursor.execute(count_sql)
    total_count = cursor.fetchone()['count(*)']

    # 한 페이지에 보여줄 데이터를 가져온다
    cursor.execute(sql, (per_page, offset))
    kream_item_list = cursor.fetchall()
    
    # flask의 pagination 객체 생성
    # https://pythonhosted.org/Flask-paginate/
    pagination = Pagination(
        page = page, # 현재 페이지 
        total = total_count, # 총 몇개의 데이터가 있는지
        per_page = per_page, # 한 페이지당 몇개 데이터를 보여줄지
        # prev_label = "<<", # 전 페이지로 가는 링크의 버튼 모양 지정
        # next_label = ">>", # 후 페이지로 가는 링크의 버튼 모양 지정
        format_total = True # 총 데이터 중 몇 개의 데이터를 보여주고 있는지 시각화
    )
    # search: 페이지 검색 기능, bs_version: bootstrap 사용시 이를 활용할 수 있게 버전을 알려줌
    return render_template('index.html', data_list = kream_item_list, 
                           pagination = pagination, search = True, bs_version = 5.3, show_single_page = True)

@app.route("/filter", methods = ['GET'])
def filter():
    # get parameter
    page, _, offset = get_page_args(per_page = per_page)
    category_id  = request.args.get('category')
    keyword = request.args.get('keyword')
    price = request.args.get("price")

    # mysql db
    conn = conn_mysql()
    cursor = conn.cursor()

    if category_id != '0': 

        count_sql, sql = filter_sql(category = category_dict[category_id], keyword = keyword)
        sql = sort_sql(sql, price = price)
        # 필터링된 데이터가 총 몇개인지 체크
        cursor.execute(count_sql, 
                        (category_dict[category_id], keyword, keyword))
        total_count = cursor.fetchone()['count(*)']

        # 페이지당 보여줄 데이터 불러오기
        cursor.execute(sql, 
                (category_dict[category_id], keyword, keyword, per_page, offset))
        kream_item_list = cursor.fetchall()

        pagination = Pagination(
        page = page, # 현재 페이지 
        total = total_count, # 총 몇개의 데이터가 있는지
        per_page = per_page, # 한 페이지당 몇개 데이터를 보여줄지
        format_total = True # 총 데이터 중 몇 개의 데이터를 보여주고 있는지 시각화
        )
        return render_template('index.html', data_list = kream_item_list, 
                               pagination = pagination, search = True, bs_version = 5.3, show_single_page = True)

    else: 
        if keyword:
            count_sql, sql = filter_sql(category = None, keyword = keyword)
            sql = sort_sql(sql, price = price)
            # 필터링된 데이터가 총 몇개인지 체크
            cursor.execute(count_sql, 
                           (keyword, keyword))
            total_count = cursor.fetchone()['count(*)']

            # 페이지당 보여줄 데이터 불러오기
            cursor.execute(sql, 
                           (keyword, keyword, per_page, offset))
            kream_item_list = cursor.fetchall()

            pagination = Pagination(
            page = page, # 현재 페이지 
            total = total_count, # 총 몇개의 데이터가 있는지
            per_page = per_page, # 한 페이지당 몇개 데이터를 보여줄지
            format_total = True # 총 데이터 중 몇 개의 데이터를 보여주고 있는지 시각화
            )  
            return render_template('index.html', data_list = kream_item_list, 
                                pagination = pagination, search = True, bs_version = 5.3, show_single_page = True)
        else: # keyword == ""
            return redirect("/")

if __name__=="__main__":
    app.run(host = '0.0.0.0', port = '8080', debug = True)