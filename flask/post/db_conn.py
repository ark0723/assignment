import pymysql
import yaml


db = yaml.load(open('post/db.yaml'), Loader=yaml.FullLoader)

# connect to mysql
conn = pymysql.connect(
    host = db['mysql_host'],
    user = db['mysql_user'],
    password = db['mysql_password'],
    db = db['mysql_db'],
    charset = 'utf8mb4',
    cursorclass=pymysql.cursors.DictCursor
)

def conn_mysql():
    # conn.open: check if mysql connection is valid or not
    if not conn.open: # if disconnected
        #reconnect
        conn.ping(reconnect=True)
    return conn