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
    insert into problem_word(level, type, kanji, hiragana, katakana, hangul, user_id, created_at, updated_at)
    values (%s, %s, %s, %s, %s, %s, null, now(), null)
'''

for n in data:
    if n['type'] == '명사':
        type = 'N'
    elif n['type'] == '동사':
        type = 'V'
    elif n['type'] == '형용사':
        type = 'ADJI'
    elif n['type'] == '형용동사':
        type = 'ADJN'
    elif n['type'] == '부사':
        type = 'ADV'
    else:
        type = 'ETC'
    curs.execute(sql, ('N5', type, n['kanji'], n['hiragana'], n['katakana'], n['hangul']))

conn.commit() 
conn.close()