import pymysql

db = pymysql.connect(host='127.0.0.1', user='root', database='class', password='wxj120056918', charset='utf8')

cur = db.cursor()

img_name = 'still'
img_path = 'still.png'
with open(img_path, 'rb') as fd:
    data = fd.read()
sql = "insert into note_data values(%s,%s, %s,%s);"

cur.execute(sql, ['1', img_name, img_path, data])
db.commit()

cur.close()
db.close()
