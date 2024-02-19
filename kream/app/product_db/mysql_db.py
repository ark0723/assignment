import pymysql

# connect to mysql
conn = pymysql.connect(
    host = 'localhost',
    user = 'root',
    password ='kr14021428',
    db = 'kream',
    charset = 'utf8mb4',
    cursorclass=pymysql.cursors.DictCursor
)

def conn_mysql():
    # conn.open: check if mysql connection is valid or not
    if not conn.open: # if disconnected
        #reconnect
        conn.ping(reconnect=True)
    return conn
