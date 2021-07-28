import pymysql

def m_stock_item():
    # db연동
    stock_db = pymysql.connect(
         user='root',
        passwd='root',
        host='localhost',#localhost
        db='stock',
        charset='utf8'
    )
    cursor = stock_db.cursor(pymysql.cursors.DictCursor)
    sql="SELECT * FROM stock_item;"
    cursor.execute(sql)
    result = cursor.fetchall()
    #print(result)
    return result#모든 주식이름,주식코드를 return

    stock_db.close()