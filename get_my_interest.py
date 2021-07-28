import pymysql

def get_my_interest(user_id):
    #db연동
    stock_db = pymysql.connect(
        user='root',
        passwd='root',
        host='localhost',#localhost
        db='stock',
        charset='utf8'
    )
    cursor = stock_db.cursor(pymysql.cursors.DictCursor)
    sql = "SELECT DISTINCT interest_stock FROM interest_list WHERE user_id=%s;"  #현재사용자가 mimi이면 그 사용자의 관심종목들을 가져와야함
    cursor.execute(sql,user_id)
    result = cursor.fetchall()
    stock_db.close()
    return result #사용자의 관심종목리스트를 return

