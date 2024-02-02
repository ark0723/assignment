import pymysql

# 1. db connection
connection = pymysql.connect(
    host = 'localhost',
    user = 'root',
    password = 'kr14021428',
    db = 'classicmodels',
    charset = 'utf8mb4',
    cursorclass = pymysql.cursors.DictCursor #dict 형태로 data 받아옴
)

try: 
    #커서 생성
    with connection.cursor() as cursor:     
        # 1. select 쿼리 실행
        sql = "select * from customers"
        cursor.execute(sql)

        # 결과 받아오기
        result = cursor.fetchall()
        print("SELECT문 연산결과:")
        for record in result:
            print(record)
            print("="*20)

    with connection.cursor() as cursor:
        # 2. insert into
        sql = "insert into customers(customerNumber, customerName) values (%s, %s)"
        cursor.execute(sql, (497, 'KBshop'))
    # 변경 사항 실제 DB 저장 및 반영
    connection.commit()
    print('INSERT연산 수행완료!')

    with connection.cursor() as cursor:
        # update 
        sql = "update customers set customerName = %s where customerNumber = %s"
        cursor.execute(sql, ('Ara', 497))
    # 변경사항 실제 db저장 및 반영
    connection. commit()
    print('UPDATE연산 수행완료!')

    with connection.cursor() as cursor:
        # delete
        sql = "delete from customers where customerNumber = %s"
        cursor.execute(sql, (497, ))
    # 변경사항 실제 db저장 및 반영
    connection. commit()
    print('DELETE연산 수행완료!')
 

finally:
    # 데이터베이스 연결 종료
    connection.close()