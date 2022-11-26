import pymysql

db = pymysql.connect(host='127.0.0.1', user='root', database='class', password='wxj120056918', charset='utf8')

cur = db.cursor()
cursor = db.cursor()
cursor.execute("SELECT DATA FROM note_data")
fout = open('image.png','wb')
fout.write(cursor.fetchone()[0])
fout.close()
cursor.close()
db.close()