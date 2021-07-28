import pymysql
from operator import itemgetter
def get_stock_info():
    # db연동
    stock_db = pymysql.connect(
        user='root',
        passwd='root',
        host='localhost',#localhost
        db='stock',
        charset='utf8'
    )
    cursor = stock_db.cursor(pymysql.cursors.DictCursor)
    sql="SELECT * FROM stock_info;" #모든 주식종목들을 다 가져옴
    cursor.execute(sql)
    result = cursor.fetchall()
    result=sorted(result, key=itemgetter('name')) #종목들을 이름순으로 정렬
    return result #디비에서 꺼낸 정보들을 return해줌

    stock_db.close()