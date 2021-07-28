from flask import Flask,render_template,request,flash,session, redirect
from prediction import prediction
from m_recommend import m_recommend
from m_predict import m_predict
from m_stock_item import m_stock_item
from store_user_info import store_user_info
from duplicate_id_check import duplicate_id_check
from login import login
from get_stock_info import get_stock_info
from store_interest_stock import store_interest_stock
from get_my_interest import get_my_interest
from get_interest_stock_info import get_interest_stock_info
from delete_interest_stock import delete_interest_stock

app = Flask(__name__)
app.config["SECRET_KEY"]='678' #session을 사용하려면 필요 '678'같이 아무 숫자 넣어도 됨

@app.route('/') #flask를 실행하면 나오는 ip주소에 접속하면 맨 처음 실행되는라우터 (로그인화면)
def main_page():
    return render_template('main.html')

@app.route('/join') #회원가입화면
def join_page():
    return render_template('join.html')

@app.route('/store_meminfo',methods=['GET', 'POST']) #가입정보저장
def store_meminfo():
    info=request.form #form에 저장된 회원가입정보들은 받음
    store_user_info(info)
    return render_template('success_join.html')#회원가입성공화면으로 넘어감

@app.route('/duplicate_id',methods=['GET', 'POST']) #아이디중복확인
def duplicate_id():
    info=request.form #form에 저장된 아이디정보를 받음
    if duplicate_id_check(info):#True=중복아님
        flash("사용할 수 있는 아이디입니다.")
    else:
        flash("중복된 아이디입니다.")

    return render_template('alert_msg.html') #팝업알림창.html

@app.route('/login',methods=['GET', 'POST']) #로그인화면
def user_login():
    info=request.form #로그인정보를 받음
    if login(info): #true=로그인성공
        session['user_id']=info['user_id']#로그인성공시 아이디를 session에 저장해 페이지 이동시 같이 이동할수 있게함
        #session['user_id']
        return redirect('/menu')#메뉴화면으로 넘어감
    else:#로그인실패
        flash("아이디,비밀번호가 일치하지 않습니다.")
        return render_template('main.html')#로그인페이지로 돌아감

@app.route('/menu') #로그인성공시 url 전환
def menu():
    return render_template('menu.html',user_id=session['user_id'])

@app.route('/logout') #로그아웃
def logout():
    return render_template('main.html')

@app.route('/stock_list') #종목리스트
def list_page():
    stocks_info=get_stock_info() #get_stock_info()를 실행해 주식종목들을 디비에서 받아옴
    return render_template('print_stocklist.html',stocks_info=stocks_info,user_id=session['user_id'])#print_stocklist.html화면으로 넘어감

@app.route('/store_interest',methods=['GET', 'POST']) #관심목록등록
def store_interest():
    info = request.form #관심목록으로 등록하고 싶은 종목들의 정보를 받음
    if store_interest_stock(info,session['user_id']):#정보들을 파라미터로 ,store_interest_stock()를 실행
        flash("관심목록으로 등록됐습니다.")
        return redirect('/stock_list')#/stock_list라우터로 redirect해줌

@app.route('/my_interestlist') #관심목록출력
def my_interestlist():
    interest_list=get_my_interest(session['user_id'])#사용자 아아디를 가지고 그 사용자의 관심목록을 디비에서 받아옴
    stock_info=get_interest_stock_info(interest_list)#사용자의 관심종목들의 세부정보를 디비에서 받아옴
    return render_template('print_interestlist.html', stock_info=stock_info, user_id=session['user_id'])

@app.route('/delete_interest',methods=['GET', 'POST']) #관심목록삭제
def delete_interest():
    info = request.form #삭제하고싶은 종목들의 정보를 받음
    if delete_interest_stock(info,session['user_id']):#delete_interest_stock()실행
        flash("관심목록에서 삭제되었습니다.")
        return redirect('/my_interestlist') #/my_interestlist 라우터로 redirect


@app.route('/predict')
def predict_page():
    item_arr=m_stock_item()#m_stock_item()실행해서 모든 주식종목들을 가져옴
    return render_template('predict.html',result=item_arr,user_id=session['user_id'])

@app.route('/predict/<target>')
def predict_print_page(target):
    predict_result=m_predict(target) #target에 저장되어있는 특정 주식종목이름을 가지고 예측한 결과 디비에서 가져옴
    return render_template('predict_print.html',result=predict_result[0],user_id=session['user_id'])

@app.route('/recommend')
def recommend_page():
    rec_arr = m_recommend() #주식종목추천 모듈
    return render_template('recommend.html',result=rec_arr,user_id=session['user_id'])

if __name__ == '__main__': #flask를 처음 실행하면 여기부터 실행됨
    prediction() #주식예측코드실행 예측실행전 stock_item 디비에 주식종목이름,코드가 저장되어있어야함!
    app.run(host='0.0.0.0',
            debug=True,use_reloader=False)