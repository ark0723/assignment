import pymysql
import cryptography

def execute_query(connection, sql, *args):
    with connection.cursor() as cursor:
        cursor.execute(sql, args)
        # if 'select' statement
        if sql.strip().upper().startswith('SELECT'): 
            return cursor.fetchall()
        else: #insert, update, delete
            # change woul be applied to db 
            connection.commit()

def main():
    connection = pymysql.connect(
        host = 'localhost',
        user = 'root',
        password = 'kr14021428',
        db = 'classicmodels',
        charset = 'utf8mb4',
        cursorclass = pymysql.cursors.DictCursor #dict 형태로 data 받아옴
        )

    try: 
    
        # 1. select
        sql = "select * from customers"
        records = execute_query(connection, sql)
        for record in records:
            print(record)

        # 2. insert
        sql = "insert into customers(customerNumber, customerName) values (%s, %s)"
        # value = (497, 'KBshop')
        execute_query(connection, sql, 497, 'kbshop')
        print("insertion has been completed")

    
        #3. update
        sql = "update customers set customerName = %s where customerNumber = %s"
        # value = ('Ara', 497)
        execute_query(connection, sql, 'Ara', 497)
        print('UPDATE연산 수행완료!')

        sql = "delete from customers where customerNumber = %s"
        # value = 497
        execute_query(connection, sql, 497)
        print('DELETE연산 수행완료!')
        

    finally:
        # cloase db connection
        connection.close()


if __name__ == "__main__":
    main()