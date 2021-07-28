import pymysql

def m_recommend():
    result_arr=[]
    # db연동
    stock_db = pymysql.connect(
        user='root',
        passwd='root',
        host='localhost',#localhost
        db='stock',
        charset='utf8'
    )
    cursor = stock_db.cursor(pymysql.cursors.DictCursor)
    sql="SELECT name,pre_price,tom_price,percent FROM stock_info ORDER BY percent DESC;"#percent를 내림차순으로 정렬한후 top3인 주식종목 정보만 가져옴
    cursor.execute(sql)
    for i in range(3):
        result = cursor.fetchone()
        result_arr.append(result)
    #print(result_arr)
    return result_arr

    stock_db.close()