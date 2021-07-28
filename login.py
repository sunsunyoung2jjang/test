import pymysql

def login(info):
    #db연동
    stock_db = pymysql.connect(
        user='root',
        passwd='root',
        host='localhost',#localhost
        db='stock',
        charset='utf8'
    )
    cursor = stock_db.cursor(pymysql.cursors.DictCursor)
    sql = "SELECT * FROM members WHERE id=%s AND password=%s;"  #로그인정보와 디비에 저장된정보가 일치하는지 확인
    cursor.execute(sql,(info['user_id'],info['user_pw']))
    result = cursor.fetchall()  # 원래코드
    stock_db.close()

    if result:
        return True #로그인성공
    else:
        return False #로그인실패

