import pymysql
import json

with open('jlpt5.json', encoding='utf-8') as f:
    data = json.load(f)

conn = pymysql.connect(
    host='dev.kr', 
    user='hello', 
    password='password',
    db='nihongo8', 
    charset='utf8')
 
curs = conn.cursor()
sql = '''
    insert into tbl_core(level, type, kanji, hiragana, katakana, hangul, user_id, regist_date, modify_id, modify_date)
    values (%s, %s, %s, %s, %s, %s, 1, now(), null, null)
'''

for n in data:
    curs.execute(sql, (5, n['type'], n['kanji'], n['hiragana'], n['katakana'], n['hangul']))

conn.commit() 
conn.close()