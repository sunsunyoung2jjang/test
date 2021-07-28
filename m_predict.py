import pymysql

def m_predict(name):
    stock_name=name
    # db연동
    stock_db = pymysql.connect(
        user='root',
        passwd='root',
        host='localhost',#localhost
        db='stock',
        charset='utf8'
    )
    cursor = stock_db.cursor(pymysql.cursors.DictCursor)
    sql="SELECT * FROM stock_info WHERE name=%s;" #디비에 이미 예측결과들이 저장되어있기 때문에 가져오기만 하면됨
    cursor.execute(sql,stock_name)
    result = [cursor.fetchone()]
    #print(result)
    return result

    stock_db.close()