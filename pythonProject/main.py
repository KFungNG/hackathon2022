import pymysql

db = pymysql.connect(host='127.0.0.1', user='root', database='hackathon2022', password='123456', charset='utf8')

cur = db.cursor()

img_name = 'image'
img_path = 'image.png'
with open(img_path, 'rb') as fd:
    data = fd.read()
sql = "insert into notehub_note values(%s,%s, %s,%s);"

cur.execute(sql, ['1', img_name, img_path, data])
db.commit()

cur.close()
db.close()
