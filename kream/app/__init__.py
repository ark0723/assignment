from flask import Flask, render_template
import pymysql

app = Flask(__name__)

conn = pymysql.connect(
    host = '127.0.0.1',
    user = 'root',
    password = 'kr14021428',
    db = 'kream',
    charset = 'utf8mb4',
    cursorclass = pymysql.cursors.DictCursor
)

cursor = conn.cursor()
sql = 'select * from product'
cursor.execute(sql)

kream_item_list = cursor.fetchall()

@app.route("/")
def index():
    return render_template('index.html', data_list = kream_item_list)

# https://codingstatus.com/how-to-display-data-from-mysql-database-table-in-node-js/

if __name__=="__main__":
    app.run(host = '127.0.0.1', port = '8080', debug = True)