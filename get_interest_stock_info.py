import pymysql
from operator import itemgetter
def get_interest_stock_info(interest_list):
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
    for i in range(len(interest_list)):
        sql="SELECT * FROM stock_info WHERE name=%s;"
        cursor.execute(sql,(interest_list[i]['interest_stock']))
        result = cursor.fetchone()
        result_arr.append(result)
    result=sorted(result_arr, key=itemgetter('name'))
    stock_db.close()

    return result #사용자의 관심종목들과 일치하는 종목들의 세부정보를 return해줌

