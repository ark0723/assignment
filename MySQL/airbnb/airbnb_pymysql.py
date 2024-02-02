import pymysql


# create 'airbnb' db if 'airbnb' does not exist
try: 
    connection = pymysql.connect(
    host = 'localhost',
    user = 'root',
    password = 'kr14021428',
    charset = 'utf8mb4',
    )

    with connection.cursor() as cursor:
        cursor.execute("create database airbnb")
        connection.commit()
        connection.close()
except: 
    pass


# airbnb 접속
connection = pymysql.connect(
host = 'localhost',
user = 'root',
password = 'kr14021428',
db = 'airbnb',
charset = 'utf8mb4',
cursorclass = pymysql.cursors.DictCursor
)

# Q1: Products table: new data insertion(Python Book, $29.99)
with connection.cursor() as cursor:
    sql = "insert into Products(productName, price, stockQuantity) values (%s, %s, %s)"
    val = ("Python Book", 29.99, 10)
    cursor.execute(sql, val)
    connection.commit()

# Q2: show all customer's data from Customers
with connection.cursor() as cursor:
    sql = "select * from Customers"
    cursor.execute(sql)
    result = cursor.fetchall()
    for customer in result:
        print(customer)
    
# Q3: whenever order made, update quantity column of 'Products' table  
with connection.cursor() as cursor:
    # update stock quantity
    sql = "update Products set stockQuantity = stockQuantity - %s where productID = %s"
    cursor.execute(sql, (1, 5))
    connection.commit()

# Q4: caclulate the total order amounts per customer from Orders table
with connection.cursor() as cursor:
    sql = "select customerID, sum(totalAmount) as total from Orders group by customerID"
    cursor.execute(sql)
    result = cursor.fetchall()
    for row in result:
        print(row)

# Q5: update email address - input: customer's id
with connection.cursor() as cursor:
    sql = "update Customers set email = %s where customerID = %s"
    cursor.execute(sql, ('kbbank@gmail.com', 4))
    connection.commit()

# Q6: Order cancellation
with connection.cursor() as cursor:
    sql = "delete from Orders where orderID = %s"
    cursor.execute(sql, 10)
    connection.commit()

# Q7: search for a certain product by product name
with connection.cursor() as cursor:
    sql = "select * from Products where productName = %s"
    cursor.execute(sql, "Data Role")
    result = cursor.fetchone()
    print(result)
# Q8: query for all orders made by a certain customer 
with connection.cursor() as cursor:
    sql = "select * from Orders where customerID = %s"
    cursor.execute(sql, 2)
    result = cursor.fetchall()
    for record in result:
        print(record)
# Q9: find the customer have made the largest order.
with connection.cursor() as cursor:
    sql = """
    select c.customerID, c.customerName, sum(o.totalAmount) as total 
    from Customers as c join Orders as o
    on c.customerID = o.customerID
    group by c.customerID
    order by total desc
    limit 1
    """
    cursor.execute(sql)
    result = cursor.fetchone()
    print(result)
