from flask import Flask, jsonify, Blueprint, redirect, request, render_template,send_from_directory, session, url_for, flash
from flask_mysqldb import MySQL
import pymysql
import pandas as pd
# from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import LoginManager, login_user, logout_user, login_required, UserMixin, current_user
from flask_sqlalchemy import SQLAlchemy
from flask_paginate import Pagination, get_page_parameter
import secrets

# render_template: 동적 template directory 로 이동 // send_from_directory: 정적 static directory로 이동

app = Flask(__name__, static_url_path='/static')
app.secret_key = secrets.token_hex(16)

# # loginManager 설정
# login_manager = LoginManager(app)
# login_manager.login_view = 'login'
# # login_manager.id_attribute = 'user_Id'

# # 사용자 모델 정의
# class User(UserMixin):
#     def __init__(self, user_Id, user_Name, user_Phone=None, user_Email1=None, user_Email2=None):
#         self.user_Id = user_Id
#         self.user_Name = user_Name
#         self.user_Phone = user_Phone
#         self.user_Email1 = user_Email1
#         self.user_Email2 = user_Email2
    

# # Flask-Login에 load_user 함수를 등록하여 User 모델을 찾아서 반환하게 함.
# @login_manager.user_loader
# def load_user(user_Id):
#     cur = mysql.connection.cursor()
#     querry = "SELECT * FROM t_user WHERE user_Id =%s;"
#     cur.execute(querry, (user_Id,))
#     result = cur.fetchone()
#     mysql.connection.commit()
#     cur.close()
#     if result:
#         return User(user_Id=result[4], user_Name=result[6], user_Phone=result[3], user_Email1=result[7], user_Email2=result[8])
    


# MySQL 연결 설정(configuration)
# connection = pymysql.connect(host='project-db-stu3.smhrd.com',
#                              port=3308,
#                              user='Insa4_IOTB_hacksim_1',
#                              password= 'aishcool1',
#                              database = "Insa4_IOTB_hacksim_1"
#                              )
app.config['MYSQL_HOST'] = 'project-db-stu3.smhrd.com'
app.config['MYSQL_PORT'] = 3308
app.config['MYSQL_USER'] = 'Insa4_IOTB_hacksim_1'
app.config['MYSQL_PASSWORD'] = "aishcool1"
app.config['MYSQL_DB'] = "Insa4_IOTB_hacksim_1"

mysql = MySQL(app)

@app.route('/')
def welcome():
    return render_template("/main/welcome.html")


@app.route('/user/loginForm')
def loginForm():
    return render_template('/user/loginForm.html')

@app.route('/main/logoutMain')
def logoutMain():
    return render_template('/main/logoutMain.html')

# @app.route('/main/loginMain')
# @login_required
# def loginMain():
#     return render_template('/main/loginMain.html', message=current_user.user_Name)

@app.route('/main/loginMain')
def loginMain():
    if 'user' in session:
        user = session['user']
        user_Name = user['user_Name']
        return render_template('/main/loginMain.html', message=user_Name)
    else:
        return render_template('user/loginForm.html')

# 로그아웃 처리
@app.route('/main/logout')
def logout():
    # logout_user
    session.clear()
    return redirect(url_for('logoutMain'))

@app.route('/user/joinForm')
def joinForm():
    return render_template('/user/joinForm.html')   

@app.route('/main/service')
def service():
    if 'user' in session:
        user = session.get('user')
        user_Name = user.get("user_Name")
        user_Id = user.get('user_Id')
        user_Phone = user.get('user_Phone')
        user_Email1 = user.get('user_Email1')
        user_Email2 = user.get('user_Email2')
        user_Email = user_Email1+'@'+user_Email2
        return render_template('/main/service.html', message=user_Name)
    else:
        return render_template('/main/service_logout.html')

@app.route('/main/contact')
# @login_required
def contact():
    # return render_template('/main/contact.html')
    if 'user' in session:
        user = session.get('user')
        user_Name = user.get("user_Name")
        user_Id = user.get('user_Id')
        user_Phone = user.get('user_Phone')
        user_Email1 = user.get('user_Email1')
        user_Email2 = user.get('user_Email2')
        user_Email = user_Email1+'@'+user_Email2
        # user = session['user']// user_Name = user['user_Name']
        return render_template('/main/contact.html', message=user_Name, user_Name=user_Name, user_Email=user_Email)
    else:
        return render_template('/main/contact_logout.html')


# 문의사항 메일링 서비스(이메일 전송)
import smtplib
from email.mime.text import MIMEText
@app.route('/main/contact/SendEmail', methods=["POST"])
def SendEmail():
    try:
        if 'user' in session:
            user = session.get('user')
            user_Name = user.get("user_Name")
            user_Id = user.get('user_Id')
            user_Phone = user.get('user_Phone')
            user_Email1 = user.get('user_Email1')
            user_Email2 = user.get('user_Email2')
            user_Email = user_Email1+'@'+user_Email2
            sendEmail = request.form.get('email') # 로그인 아이디(보낸 이메일 주소)
            recvEmail = 'lcy629@naver.com' # 받는 아이디(받는 이메일주소) // 관리자에게 송부
            emailPassword = request.form.get('emailPassword') # 입력한 이메일 비밀번호
        else:
            sendEmail = request.form.get('email')
            recvEmail = input("전송할 메일주소를 작성하시오.")
            emailPassword = request.form.get('emailPassword')

        smtpName = 'smtp.naver.com' # SMTP 서버 주소
        smtpPort = 587 # TLS 보안 처리를 위한 포트 번호 (TLS 보안처리가 필요 없을시: smtPort = 465)

        text = request.form.get('message')
        msg = MIMEText(text)
                
        msg['Subject'] = request.form.get('subject')
        msg['From'] = sendEmail
        msg['To'] = recvEmail

        s = smtplib.SMTP(smtpName, smtpPort) # SMTP 서버 연결
        s.starttls() # TLS 보안 처리
        s.login(sendEmail, emailPassword) # 로그인

        s.sendmail(sendEmail, recvEmail, msg.as_string()) # 메일 전송
        s.quit() # 서버 연결 종료
            
        return jsonify({'message': 'success'}),200
# redirect(url_for('contact'))

    except:
        return jsonify({'message': 'failed'}),401
    
    
@app.route('/user/join', methods=['POST'])
def join():
    # Get form data
    user_Phone1 = request.form.get('user_Phone1')
    user_Phone2 = request.form.get('user_Phone2')
    user_Phone3 = request.form.get('user_Phone3')
    user_Id = request.form.get('user_Id')
    user_Pwd = request.form.get('user_Pwd')
    user_Name = request.form.get('user_Name')
    user_Email1 = request.form.get('user_Email1')
    user_Email2 = request.form.get('user_Email2')


    # if not all([user_Phone1, user_Phone2, user_Phone3, user_Phone, user_Id, user_Pwd, user_Name, user_Email1, user_Email2]):
    #     return jsonify({"error": "Please provide all required fields"}), 400

    # Save data to the database
    cur = mysql.connection.cursor()
    
    cur.execute("INSERT INTO t_user (user_Phone1, user_Phone2, user_Phone3, user_Phone, user_Id, user_Pwd, user_Name, user_Email1, user_Email2) VALUES (%s, %s, %s, CONCAT(%s, %s, %s), %s, %s, %s, %s, %s);"
                ,(user_Phone1, user_Phone2, user_Phone3, user_Phone1, user_Phone2, user_Phone3, user_Id, user_Pwd, user_Name, user_Email1, user_Email2))

    mysql.connection.commit()
    
    cur.close()
    
    user = {'user_Id':user_Id, 'user_Pwd':user_Pwd, 'user_Name':user_Name, 'user_Email1':user_Email1, 'user_Email2':user_Email2, 'user_Phone1':user_Phone1, 'user_Phone2':user_Phone2, 'user_Phone3':user_Phone3, 'user_Phone':user_Phone1+user_Phone2+user_Phone3}
    session['user'] = user
        
    return redirect(url_for('joinSuccess', user_Name=user_Name)) # url_for('함수이름')

# 아이디 중복검사
@app.route('/user/check_id', methods=['GET'])
def check_id():
    user_Id = request.args.get('user_Id') # database에 있는 아이디 불러오기

    if not user_Id:
        return jsonify({'result': 'False', 'message': '아이디를 입력해 주세요.'})

    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM t_user WHERE user_Id = %s;", (user_Id,))
    data = cur.fetchone()
    cur.close()

    if data:
        # 아이디가 이미 존재합니다.
        return jsonify({'result': 'False', 'message': '이미 사용중인 아이디입니다.'})
    else:
        # 중복된 아이디가 없습니다.
        return jsonify({'result': 'True', 'message': '사용 가능한 아이디입니다.'})

# 폰번호 중복검사
@app.route('/user/check_phone', methods=['GET'])
def check_phone():
    user_Phone = request.args.get('user_Phone') # database에 있는 폰번호 불러오기
    
    if not user_Phone:
        return jsonify({'RESULT': 'False', 'message': '폰번호를 입력해 주세요.'})
    
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM t_user WHERE user_Phone = %s;", (user_Phone,))
    data = cur.fetchone()
    cur.close()
    
    if data:
        # 이미 폰번호가 이미 존재합니다.
        return jsonify({'RESULT': 'NotFound', 'message': '이미 사용중인 번호입니다.'})
    else:
        # 중복된 폰번호가 없습니다.
        return jsonify({'RESULT': 'Found', 'message': '사용 가능한 번호입니다.'})

# 회원가입 성공
@app.route('/user/joinSuccess')
def joinSuccess():
    user_Name = request.args.get('user_Name')
    user = session.get('user')
    return render_template('/user/joinSuccess.html', message=user_Name) # message 변수에 user_Name 전달

# 로그인 처리
@app.route('/user/login', methods=['POST'])
def login():
    user_Id = request.form.get('user_Id')
    user_Pwd = request.form.get('user_Pwd')

    cur = mysql.connection.cursor()
    querry = "SELECT * FROM t_user WHERE user_Id = %s and user_Pwd = %s"
    cur.execute(querry, (user_Id, user_Pwd))
    result = cur.fetchone()
    mysql.connection.commit()
    cur.close()

    if result:
        user_Id = result[4]
        user_Name = result[6]   
        user_Phone = result[3]
        user_Phone1 = result[0]
        user_Phone2 = result[1]
        user_Phone3 = result[2]
        user_Email1 = result[7]
        user_Email2 = result[8]
        # user = User(user_Id=user_Id, user_Name=user_Name, user_Phone=user_Phone, user_Email1=user_Email1, user_Email2=user_Email2)
        # login_user(user)
        # flash('로그인 완료', category='success')
        user = {'user_Id':result[4], 'user_Pwd':result[5], 'user_Name':result[6], 'user_Phone':result[3], 'user_Phone1':result[0], 'user_Phone2':result[1], 'user_Phone3':result[2], 'user_Email1':result[7],'user_Email2':result[8]}
        session['user'] = user
        return jsonify({'message': 'success', 'user_Name': user_Name}), 200
        # return redirect(url_for("loginMain"))
        # return redirect(url_for('loginMain', user_Name=result[6])) # url_for('함수이름')
    else:
        return jsonify({'message': 'failed'}), 401
        # return "아이디 or 비밀번호가 올바르지 않습니다.", 401
    
@app.route('/mypage/updateForm')
def updateForm():
    user = session.get('user')
    if user: # 로그인 된 상태
        user_Id = user.get('user_Id')
        user_Name = user.get('user_Name')
        user_Phone1 = user.get('user_Phone1')
        user_Phone2 = user.get('user_Phone2')
        user_Phone3 = user.get('user_Phone3')
        user_Email1 = user.get('user_Email1')
        user_Email2 = user.get('user_Email2')
        if user_Id == "admin":
            return render_template('/product/addproduct.html')
        else:
            return render_template('/mypage/update.html', user_Id=user_Id, user_Name=user_Name, user_Phone1=user_Phone1, user_Phone2=user_Phone2, user_Phone3=user_Phone3, user_Email1=user_Email1, user_Email2=user_Email2)
    else: # 로그인 되지 않은 상태
        return redirect('/user/loginForm')

@app.route('/mypage/update', methods=["POST"])
def update():
    user = session.get('user')
    if user:
        user_Phone1 = request.form.get('user_Phone1')
        user_Phone2 = request.form.get('user_Phone2')
        user_Phone3 = request.form.get('user_Phone3')
        user_Id = user.get('user_Id')
        user_Pwd = request.form.get('user_Pwd')
        user_Name = user.get('user_Name')
        user_Email1 = request.form.get('user_Email1')
        user_Email2 = request.form.get('user_Email2')
        user_Phone = user_Phone1 + user_Phone2 + user_Phone3
        cur = mysql.connection.cursor()
        querry= "UPDATE t_user SET user_Phone1 = %s, user_Phone2=%s, user_Phone3=%s, user_Phone=%s, user_Pwd=%s, user_Name=%s, user_Email1=%s, user_Email2=%s WHERE user_Id =%s"
        cur.execute(querry, (user_Phone1,user_Phone2, user_Phone3, user_Phone, user_Pwd, user_Name, user_Email1, user_Email2, user_Id))
        
        mysql.connection.commit()
        
        cur.close()
        
        user = {'user_Id':user_Id, 'user_Pwd':user_Pwd, 'user_Name':user_Name, 'user_Email1':user_Email1, 'user_Email2':user_Email2, 'user_Phone1':user_Phone1, 'user_Phone2':user_Phone2, 'user_Phone3':user_Phone3, 'user_Phone':user_Phone1+user_Phone2+user_Phone3}
        session['user'] = user
    
        return redirect(url_for('loginMain'))
    else:
        return redirect(url_for('loginForm'))


@app.route('/mypage/leaveForm')
def leaveForm():
    user = session.get('user')
    if user:
        return render_template('/mypage/leave.html')
    else:
        return redirect(url_for('loginForm'))


@app.route('/mypage/leave', methods=["POST"])
def leave():
    user = session.get('user')
    if user:
        user_Id = user.get('user_Id')
        cur = mysql.connection.cursor()
        querry = "DELETE FROM t_user WHERE user_Id = %s"
        cur.execute(querry, (user_Id,))
        mysql.connection.commit()
        cur.close()
        return redirect(url_for('logoutMain'))
        # return render_template('/main/logoutMain.html')
    else: # 로그인되지 않은경우
        return redirect(url_for('loginForm'))

    
@app.route('/product/product')
def product():
    user = session.get('user')
    user_Id = user.get('user_Id')
    if user_Id == 'admin':
        return render_template('product/addproduct.html')
    else:
        return redirect(url_for('updateForm'))

@app.route('/product/addproduct', methods=['POST'])
def addProduct():
    product_Id = request.form.get('product_Id')
    manufacturing_Date = request.form.get('manufacturing_Date')
    product_Age = request.form.get('product_Age')
    product_Status = request.form.get('product_Status')
    product_Img = request.form.get('product_Img') 
    
    cur = mysql.connection.cursor()
    
    cur.execute("INSERT INTO t_product (product_Id, manufacturing_Date, product_Age, product_Status, product_Img) VALUES (%s, %s, %s, %s, %s);"
                ,(product_Id, manufacturing_Date, product_Age, product_Status, product_Img))

    mysql.connection.commit()
    
    cur.close()
    
    product = {'product_Id':product_Id, 'manufacturing_Date':manufacturing_Date, 'product_Age':product_Age, 'product_Status':product_Status, 'product_Img':product_Img}
        
    return redirect(url_for('productView'))



# 페이징 구현
# 상품뷰(관리자)
@app.route('/product/view')
def productView():
    # product = session.get('product')
    # page, _, offset = get_page_args(per_page=per_page)
    per_page = 10
    page = request.args.get('page',1,type=int)
    offset = (page-1)*per_page
    # page = int(request.args.get(get_page_parameter(),1))
    

# 모든 상품데이터 가져오기
    cur = mysql.connection.cursor()
    cur.execute("SELECT COUNT(*) FROM t_product;")
    count = cur.fetchone()[0]
    # cur.execute(f"SELECT * FROM t_product LIMIT {(page-1)*per_page},{per_page}")
    cur.execute("SELECT * FROM t_product ORDER BY product_Id DESC LIMIT %s OFFSET %s;", (per_page, offset))

    # products = cur.fetchall()
    column_names = [desc[0] for desc in cur.description]
    products = [dict(zip(column_names, product)) for product in cur.fetchall()]
                
    print(products) # 디버깅 용으로 출력

    # pagination = Pagination(
    #     page=page,
    #     total=count,
    #     per_page=per_page,
    #     prev_label="<<",
    #     next_label=">>",
    #     format_total=True,
    #     search=True,
    #     bs_version=5
    # )
    
    pagination = Pagination(
                  page=page, total=count, per_page=per_page, prev_label="<<",
                  next_label=">>", format_total=True, search=True, bs_version=5,
                  record_name='records', format_number=True,
                  css_framework='bootstrap5', size='small',
                  query=False, href="javascript:void(0);",
                  onclick="go_to_page(this, {0});"
              )
    
    return render_template('product/productList.html', products=products,  pagination=pagination, page=page, per_page=per_page)
# Pagination 객체 생성
    # pagination = Pagination(page=page, total=count, per_page=per_page, css_framework='bootstrap4')

# 상품 리스트 페이지 렌더링
    # return render_template('productList.html', products = products, pagination=pagination, count=count)
    

# 포인트 뷰(사용자)
@app.route('/point/view')
def pointView():        
    user = session.get('user')
    if user:
        user_Id = user.get('user_Id')
        user_Name = user.get('user_Name')
        user_Phone = user.get('user_Phone')
        
        per_page = 20
        page = request.args.get('page',1,type=int)
        offset = (page-1)*per_page
        # page = int(request.args.get(get_page_parameter(),1))

    # 모든 포인트 데이터 가져오기
        cur = mysql.connection.cursor()
        cur.execute("SELECT COUNT(*) FROM t_point;")
        count = cur.fetchone()[0]
        # cur.execute(f"SELECT * FROM t_product LIMIT {(page-1)*per_page},{per_page}")
        cur.execute('SELECT * FROM t_point WHERE user_Phone = %s ORDER BY point_Id DESC LIMIT %s OFFSET %s;', (user_Phone, per_page, offset))
        
        # products = cur.fetchall()
        column_names = [desc[0] for desc in cur.description]
        points = [dict(zip(column_names, point)) for point in cur.fetchall()]
        
        cur.execute('SELECT SUM(point) as user_Point FROM t_point WHERE user_Phone = %s ORDER BY point_ID DESC LIMIT %s OFFSET %s;', (user_Phone, per_page, offset))
        column_names = [desc[0] for desc in cur.description]
        user_Point = [dict(zip(column_names, user_Point)) for user_Point in cur.fetchall()]
        
                    
        # pagination = Pagination(
        #     page=page,
        #     total=count,
        #     per_page=per_page,
        #     prev_label="<<",
        #     next_label=">>",
        #     format_total=True,
        #     search=True,
        #     bs_version=5
        # )
        
        pagination = Pagination(
                    page=page, total=count, per_page=per_page, prev_label="<<",
                    next_label=">>", format_total=True, search=True, bs_version=5,
                    record_name='records', format_number=True,
                    css_framework='bootstrap5', size='small',
                    query=False, href="javascript:void(0);",
                    onclick="go_to_page(this, {0});"
                )
        
        return render_template('point/point.html', points=points,user_Point=user_Point, pagination=pagination, page=page, per_page=per_page)
    else:
        return redirect(url_for('loginForm'))



# 포인트 뷰(관리자)
@app.route('/point/view2')
def pointView2():
    per_page = 20
    page = request.args.get('page',1,type=int)
    offset = (page-1)*per_page
    # page = int(request.args.get(get_page_parameter(),1))
    

# 모든 포인트 데이터 가져오기
    cur = mysql.connection.cursor()
    cur.execute("SELECT COUNT(*) FROM t_point;")
    count = cur.fetchone()[0]
    # cur.execute(f"SELECT * FROM t_product LIMIT {(page-1)*per_page},{per_page}")
    cur.execute("SELECT * FROM t_point ORDER BY point_Id DESC LIMIT %s OFFSET %s;", (per_page, offset))

    # points = cur.fetchall()
    column_names = [desc[0] for desc in cur.description]
    points = [dict(zip(column_names, point)) for point in cur.fetchall()]
    
                
    # pagination = Pagination(
    #     page=page,
    #     total=count,
    #     per_page=per_page,
    #     prev_label="<<",
    #     next_label=">>",
    #     format_total=True,
    #     search=True,
    #     bs_version=5
    # )
    
    pagination = Pagination(
                    page=page, total=count, per_page=per_page, prev_label="<<",
                    next_label=">>", format_total=True, search=True, bs_version=5,
                    record_name ='records', format_number=True,
                    css_framework='bootstrap5', size='small',
                    query=False, href="javascript:void(0);",
                    onclick="go_topage(this, {0});"
    )
    
    return render_template('point/point_admin.html', points=points, pagination=pagination, page=page, per_page=per_page)

# 렌탈 뷰(관리자)
@app.route('/rental/view')
def rentalView():
    per_page = 20 # 페이지당 보여줄 리스트 갯수
    page = request.args.get('page',1,type=int)
    offset = (page-1)*per_page
    
    # 모든 데이터 가져오기
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM t_rental;")
    count = cur.fetchone()[0]
    
    cur.execute("SELECT * FROM t_rental ORDER BY rental_Id DESC LIMIT %s OFFSET %s;", (per_page, offset))
    
    # rentals = cur.fetchall()
    column_names = [desc[0] for desc in cur.description]
    rentals = [dict(zip(column_names, rental)) for rental in cur.fetchall()]
    
    pagination = Pagination(
                    page=page, total=count, per_page=per_page, prev_label="<<",
                    next_label=">>", format_total=True, search=True, bs_version=5,
                    record_name ='records', format_number=True,
                    css_framework='bootstrap5', size='small',
                    query=False, href="javascript:void(0);",
                    onclick="go_topage(this, {0});"
    )
    
    return render_template('rental/rental_admin.html', rentals = rentals, pagination=pagination, page=page, per_page=per_page)
    
if __name__ =='__main__':
    app.run(debug=True)
    