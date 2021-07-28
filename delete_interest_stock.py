import pymysql

def delete_interest_stock(info,user_id):
    info = info.getlist('interest_stock_name')
    #db연동
    stock_db = pymysql.connect(
        user='root',
        passwd='root',
        host='localhost',#localhost
        db='stock',
        charset='utf8'
    )
    cursor = stock_db.cursor(pymysql.cursors.DictCursor)
    for i in range(len(info)): #사용자와 삭제하고싶은 종목의 이름이 둘다 일치하는걸 삭제함
        sql = 'DELETE FROM interest_list WHERE user_id=%s AND interest_stock=%s;'
        cursor.execute(sql,(user_id,info[i]))#쿼리실행
        stock_db.commit()#db에 반영

    stock_db.close()
    return True


