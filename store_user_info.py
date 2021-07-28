import pymysql

def store_user_info(info):
    print(info)
    #db연동
    stock_db = pymysql.connect(
        user='root',
        passwd='root',
        host='localhost',#localhost
        db='stock',
        charset='utf8'
    )
    cursor = stock_db.cursor(pymysql.cursors.DictCursor)

    #db에 회원가입정보(아이디,비밀번호)를 저장함
    sql = 'INSERT INTO members (id, password) VALUES (%s, %s);' #insert쿼리

    cursor.execute(sql,(info['user_ID'],info['user_PW']))#쿼리실행
    stock_db.commit()#db에 반영

    stock_db.close()


