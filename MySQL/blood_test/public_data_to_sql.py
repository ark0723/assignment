import chardet
import pandas as pd
import pymysql
import json
import csv

# 1. check encoding - format 
rawdata = open("blood_test/nationalBloodTest.csv", "rb").read()
result = chardet.detect(rawdata)
check_encode = result['encoding']
print(check_encode)

def check_encode(val):
    if val!=None:
        if type(val) is not str:
            return str(val).encode('utf-8')
        else: 
            return val

### 2. make a list of dictionary
# first method: with csv library 
with open('blood_test/nationalBloodTest.csv', 'r', newline = '',encoding = 'utf-8') as f: 
    reader = csv.DictReader(f)
    data = [row for row in reader]
    print(len(data)) #10000

# second method : with pandas (read as dataframe -> to_dict)
df = pd.read_csv('blood_test/nationalBloodTest.csv', header = 0, encoding='ascii')
df.head(5)

# list of dictionary
dict_list = df.to_dict('records')
print(len(dict_list))

### 3. write a file in json format: dump from json library
save_ = 'blood_test/nationalBloodTest.json'
with open(save_, 'w') as f:
    json.dump(dict_list, f)

### 4. connect to MySQL
connection = pymysql.connect(
    host = 'localhost',
    user = 'root',
    password = 'kr14021428',
    db = 'blood',
    charset = 'utf8',
    cursorclass = pymysql.cursors.DictCursor #dict 형태로 data 받아옴
)

print(len(dict_list)) # 1,000,000

# datatype - SEX,AGE_G,TCHOL,TG,HDL,ANE,IHD,STK : int, HGB: float
with connection.cursor() as cursor:
    for i in range(10000): # insert 100 record per one loop (like mini-batch) 
        for idx, record in enumerate(dict_list[i:100*(i+1)]):
            # sex = check_encode(record['SEX'])
            sex = record['SEX']
            age = record['AGE_G']
            hgb = record['HGB']
            chol = record['TCHOL']
            tg = record['TG']
            hdl = record['HDL']
            ane = record['ANE']
            ihd = record['IHD']
            stk = record['STK']

            sql = '''
                    INSERT INTO nationalBloodTest(SEX, AGE_G, HGB, TCHOL, TG, HDL, ANE, IHD, STK)
                    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
                    '''
            cursor.execute(sql, (sex, age, hgb, chol, tg, hdl, ane, ihd, stk)) 
        connection.commit()
    connection.close()

    
