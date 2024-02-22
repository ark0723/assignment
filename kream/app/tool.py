from flask_paginate import Pagination, get_page_args
# from product_db.mysql_db import conn_mysql

def makePage(total_count, per_page = 10):
    # return(page, per_page, offset)
    # page: current page(default: 1) -> 페이지 링크 누르면 2, 3, 4, ...
    # offset: page에 따라 몇번째 데이터부터 보여줄지
    page, _, offset = get_page_args(per_page = per_page)

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

    return pagination, offset

def sorting(input_sql, sortby):
    # price ascending order
    if sortby == "0": # 
        sql = input_sql + " order by price"
    # price descending order
    elif sortby == "1":
        sql = input_sql + " order by price desc"
    # 상품명 오름차순
    elif sortby == "2":
        sql = input_sql + " order by title"
    # 상품명 내림차순
    elif sortby == "3":
        sql = input_sql + " order by title desc"
    # 리뷰 많은 순
    elif sortby == "4":
        sql = input_sql + " order by review desc"
    # 거래 많은 순 
    elif sortby == "5":
        sql = input_sql + " order by sales desc"
    else:
        sql = input_sql

    return sql

def writeSQL(category = None, keyword = None, sortby = None):
    base = "select * from product"
    # base_c = base.replace("*", "count(*)")
    
    if category:
        sql = base + " where category = '" + str(category) + "' and (locate('" + str(keyword)+"', brand) > 0 or locate('" + keyword +"', title) > 0)"
    else:
        if keyword:
            sql = base + " where locate('" +str(keyword) +"', brand) > 0 or (locate('" + str(keyword) +"', title) > 0)"
        else:
             sql = base   

    if sortby:
        sql = sorting(sql, sortby)
        return sql

    return sql



