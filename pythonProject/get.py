import pymysql

db = pymysql.connect(host='127.0.0.1', user='root', database='hackathon2022', password='123456', charset='utf8')

cur = db.cursor()
cursor = db.cursor()
cursor.execute("SELECT DATA FROM notehub_note")
fout = open('image.png','wb')
fout.write(cursor.fetchone()[0])
fout.close()
cursor.close()
db.close()