import pymysql
import json

file_dir = 'kream/data/item.json'
# load json data
with open(file_dir, 'r') as f:
    data = json.load(f)

# print(data[:10])
    
#connect to MySQL
connection = pymysql.connect(
    host = 'localhost',
    user = 'root',
    password = 'kr14021428',
    db = 'kream',
    charset = 'utf8mb4',
    cursorclass = pymysql.cursors.DictCursor
)

with connection.cursor() as cursor:
    cursor.execute("show tables")
    tables = cursor.fetchall()

    # check if 'product' table exists or not
    if 'product' not in tables[0]['Tables_in_kream']:
        sql = '''
                create table product (product_id varchar(15) primary key, category varchar(15), brand varchar(50), 
                title varchar(225), price int, sales int, wish int, review int, img text, product_link text, review_detail text)
                '''
        cursor.execute(sql)
        connection.commit()


    for idx, item in enumerate(data):
        # insert data into product table
        sql = '''
            INSERT INTO product(product_id, category, brand, title, price, sales, wish, review, img, product_link, review_detail)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            '''
        
        try:
            cursor.execute(sql, (item['product_id'], item['category'], item['brand'], item['title'], item['price'], item['sales'],item['wish'],
                                item['review'], item['img'], item['product_link'], item['review_detail']))
            connection.commit()
            print("Insertion has been completed")
        except:
            print("problem in {}:".format(idx))

    connection.close()

for idx, row in enumerate(data):
    if not row['price']:
        print(idx)
