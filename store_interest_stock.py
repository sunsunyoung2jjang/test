import pymysql

def store_interest_stock(info,user_id):
    info = info.getlist('stock_name')
    #db연동
    stock_db = pymysql.connect(
        user='root',
        passwd='root',
        host='localhost',#localhost
        db='stock',
        charset='utf8'
    )
    cursor = stock_db.cursor(pymysql.cursors.DictCursor)
    for i in range(len(info)):
        #db에 (아이디,주식종목이름)->mimi,삼성전자 이런 형식으로 저장됨
        sql = 'INSERT INTO interest_list (user_id, interest_stock) VALUES (%s, %s);'

        cursor.execute(sql,(user_id,info[i]))
        stock_db.commit()#db에 반영

    stock_db.close()
    return True


