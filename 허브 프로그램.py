from tkinter import *
import sqlite3
import datetime
now= datetime.datetime.now()
################################
#디비 연동함수
####insert#####################
def db_i(sql):
    con = sqlite3.connect("Hubdb")
    cur = con.cursor()
    cur.execute("pragma foreign_keys = 1")
    con.commit()
    cur.execute(sql)
    con.commit()
    con.close()
####select용##########################
def db_s1(sql):
    con = sqlite3.connect("Hubdb")
    cur = con.cursor()
    cur.execute(sql)
    while True:
            row = cur.fetchone()
            if row == None :
                break
            print(row)
    con.close()

########################################################
num = 1
################################################################
def okClick1():
    root.destroy()
    def okClick1_1():
        root1.destroy()
        i1 = input("상품명: ")
        i2 = input("재고량: ")
        i3 = input("위 치: ")
        sql = f"insert into 상품(상품명, 재고량 , 위치) values('{i1}',{i2},'{i3}')"
        try:
            db_i(sql)
            print("입력완료")
        except:
            print("없는 위치입니다.")
    
    def okClick1_2():
        root1.destroy()
        def okClick1_2_1():                              #상품명 변경
            root1_2.destroy()        
            i1 = input("상품번호: ")
            i2 = input("변경할 상품명: ")
            sql = f"update 상품 set 상품명 = '{i2}' where 상품번호 = {i1}"
            try:
                db_i(sql)
                print("변경완료")
            except:
                print("없는 상품입니다")                   
        def okClick1_2_2():                           
            root1_2.destroy()                     #재고량 변경
            i1 = input("상품번호: ")
            i2 = input("변경할 재고량: ")
            sql = f"update 상품 set 재고량 = {i2} where 상품번호 = {i1}"
            try:
                db_i(sql)
                print("변경완료")
            except:
                print("없는 상품입니다")   
        def okClick1_2_3():                           
            root1_2.destroy()                     #위치 변경
            i1 = input("상품번호: ")
            i2 = input("변경할 위치: ")
            sql = f"update 상품 set 위치 = '{i2}' where 상품번호 = {i1}"
            try:
                db_i(sql)
                print("변경완료")
            except:
                print("없는 상품입니다")  
    # 버튼 클릭 이벤트 핸들러
        root1_2 = Tk()
        root1_2.geometry("100x200+200+100")
        lbl = Label(root1_2, text="상품변경")
        lbl.pack()
    # 버튼 클릭 이벤트와 핸들러 정의
        btn1 = Button(root1_2, text="상품명 변경", command=okClick1_2_1)
        btn1.pack()
        btn2 = Button(root1_2, text="재고량 변경", command=okClick1_2_2)
        btn2.pack()
        btn3 = Button(root1_2, text="위 치 변경", command=okClick1_2_3)
        btn3.pack()
        
    def okClick1_3():
        root1.destroy()
        def okClick1_3_1():                           
            root1_3.destroy()                     #검색
            def okClick1_3_1_1():                           
                root1_3_1.destroy()  
                i1 = input("상품번호: ")
                sql = f"select * from 상품 where 상품번호 = {i1}"
                db_s1(sql)
            def okClick1_3_1_2():                           
                root1_3_1.destroy()  
                i1 = input("상품명: ")
                sql = f"select * from 상품 where 상품명 = '{i1}'"
                db_s1(sql)  
            def okClick1_3_1_3():                           
                root1_3_1.destroy()  
                i1 = input("재고량: ")
                sql = f"select * from 상품 where 재고량 = {i1}"
                db_s1(sql)
            def okClick1_3_1_4():                           
                root1_3_1.destroy()  
                i1 = input("위 치: ")
                sql = f"select * from 상품 where 위치 = '{i1}'"
                db_s1(sql)
              # 버튼 클릭 이벤트 핸들러
            root1_3_1 = Tk()
            root1_3_1.geometry("100x200+200+100")
            lbl = Label(root1_3_1, text="상품검색")
            lbl.pack()
        # 버튼 클릭 이벤트와 핸들러 정의
            btn1 = Button(root1_3_1, text="상품번호로 검색", command=okClick1_3_1_1)
            btn1.pack()
            btn2 = Button(root1_3_1, text="상품명으로 검색", command=okClick1_3_1_2)
            btn2.pack()
            btn2 = Button(root1_3_1, text="재고량으로 검색", command=okClick1_3_1_3)
            btn2.pack()
            btn2 = Button(root1_3_1, text="위치로 검색", command=okClick1_3_1_4)
            btn2.pack()             
        def okClick1_3_2():                           
            root1_3.destroy()                      #전체보기
            sql = "select * from 상품"
            db_s1(sql)        
        # 버튼 클릭 이벤트 핸들러
        root1_3 = Tk()
        root1_3.geometry("100x200+200+100")
        lbl = Label(root1_3, text="상품조회")
        lbl.pack()
    # 버튼 클릭 이벤트와 핸들러 정의
        btn1 = Button(root1_3, text="검색", command=okClick1_3_1)
        btn1.pack()
        btn2 = Button(root1_3, text="전체보기", command=okClick1_3_2)
        btn2.pack()

    def okClick1_4():
        root1.destroy()
        i1 = input("상품번호: ")
        sql = f"delete from 상품 where 상품번호 = {i1}"
        try:
            db_i(sql)
            print("삭제완료")
        except:
            print("삭제불가 상품입니다")
            
    def okClick1_5():
        root1.destroy()
        global num1
        num1 = 0
        return
  
    while num1: 
    # 버튼 클릭 이벤트 핸들러
        root1 = Tk()
        root1.geometry("100x200+200+100")
        lbl = Label(root1, text="상품관리")
        lbl.pack()
    # 버튼 클릭 이벤트와 핸들러 정의
        btn1 = Button(root1, text="등록", command=okClick1_1)
        btn1.pack()
        btn2 = Button(root1, text="변경", command=okClick1_2)
        btn2.pack()
        btn3 = Button(root1, text="조회", command=okClick1_3)
        btn3.pack()
        btn4 = Button(root1, text="삭제", command=okClick1_4)
        btn4.pack()
        btn5 = Button(root1, text="뒤로", command=okClick1_5)
        btn5.pack()
        root1.mainloop()
#######################################################################################  
def okClick2():
    root.destroy()
    def okClick2_1():
        root1.destroy()
        i1 = input("이 름: ")
        i2 = input("핸드폰번호(-포함): ")
        i3 = input("주 소: ")
        i4 = input("상품번호: ")
        i5 = input("상품수량: ")
        i6 = now.strftime('%Y-%m-%d')
        try:
            sql = f"update 상품 set 재고량 = 재고량 - {i5} where 상품번호 = {i4}"
            db_i(sql)
            sql = f"insert into 수령인(이름, 휴대폰번호 , 주소, 상품번호, 상품수량, 주문일자) values('{i1}','{i2}','{i3}',{i4},{i5},'{i6}')"
            db_i(sql)
            print("입력완료")
        except:
            print("입력불가")

    def okClick2_2():
        root1.destroy()
        def okClick2_2_1():                           
            root1_2.destroy()                     #검색
            def okClick2_2_1_1():                           
                root1_2_1.destroy()  
                i1 = input("수령번호: ")
                sql = f"select * from 수령인 where 수령번호 = {i1}"
                db_s1(sql)
            def okClick2_2_1_2():                           
                root1_2_1.destroy()  
                i1 = input("상품번호: ")
                sql = f"select * from 수령인 where 상품번호 = {i1}"
                db_s1(sql) 
              # 버튼 클릭 이벤트 핸들러
            root1_2_1 = Tk()
            root1_2_1.geometry("100x200+200+100")
            lbl = Label(root1_2_1, text="주문검색")
            lbl.pack()
        # 버튼 클릭 이벤트와 핸들러 정의
            btn1 = Button(root1_2_1, text="수령번호로 검색", command=okClick2_2_1_1)
            btn1.pack()
            btn2 = Button(root1_2_1, text="상품번호로 검색", command=okClick2_2_1_2)
            btn2.pack()     
        def okClick2_2_2():                           
            root1_2.destroy()                      #전체보기
            sql = "select * from 수령인"
            db_s1(sql)    
        # 버튼 클릭 이벤트 핸들러
        root1_2 = Tk()
        root1_2.geometry("100x200+200+100")
        lbl = Label(root1_2, text="주문조회")
        lbl.pack()
    # 버튼 클릭 이벤트와 핸들러 정의
        btn1 = Button(root1_2, text="검색", command=okClick2_2_1)
        btn1.pack()
        btn2 = Button(root1_2, text="전체보기", command=okClick2_2_2)
        btn2.pack()
        
    def okClick2_3():
        root1.destroy()
        i1 = input("수령번호: ")
        sql = f"delete from 수령인 where 수령번호 = {i1}"
        try:
            db_i(sql)
            print("삭제완료")
        except:
            print("삭제불가 상품입니다")
            
    def okClick2_4():
        root1.destroy()
        global num1
        num1 = 0
        return
  
    while num1: 
    # 버튼 클릭 이벤트 핸들러
        root1 = Tk()
        root1.geometry("100x200+200+100")
        lbl = Label(root1, text="주문관리")
        lbl.pack()
    # 버튼 클릭 이벤트와 핸들러 정의
        btn1 = Button(root1, text="등록", command=okClick2_1)
        btn1.pack()
        btn3 = Button(root1, text="조회", command=okClick2_2)
        btn3.pack()
        btn4 = Button(root1, text="삭제", command=okClick2_3)
        btn4.pack()
        btn5 = Button(root1, text="뒤로", command=okClick2_4)
        btn5.pack()
        root1.mainloop()
##########################################################################################
def okClick3():
    root.destroy()
    def okClick3_1():
        root1.destroy()
        i1 = input("위 치: ")
        sql = f"insert into 창고 values('{i1}')"
        try:
            db_i(sql)
            print("입력완료")
        except:
            print("없는 위치입니다.")
    
    def okClick3_2():
        root1.destroy()
        i1 = input("변경할 위치: ")
        i2 = input("변경될 위치: ")
        sql = f"update 창고 set 위치 = '{i2}' where 위치 = '{i1}'"
        try:
            db_i(sql)
            print("변경완료")
        except:
            print("없는 위치입니다")  
            
    def okClick3_3():
        root1.destroy()
        def okClick3_3_1():                           
            root1_3.destroy()                     #검색
            i1 = input("위 치: ")
            sql = f"select 위치,상품명 from 상품 where 위치 = '{i1}'"
            db_s1(sql)
        def okClick3_3_2():  
            root1_3.destroy()
            sql = "select * from 창고"
            db_s1(sql)     
            
        # 버튼 클릭 이벤트 핸들러
        root1_3 = Tk()
        root1_3.geometry("100x200+200+100")
        lbl = Label(root1_3, text="창고조회")
        lbl.pack()
    # 버튼 클릭 이벤트와 핸들러 정의
        btn1 = Button(root1_3, text="검색", command=okClick3_3_1)
        btn1.pack()
        btn2 = Button(root1_3, text="전체보기", command=okClick3_3_2)
        btn2.pack()
        
    def okClick3_4():
        root1.destroy()
        i1 = input("위 치: ")
        sql = f"delete from 창고 where 위치 = '{i1}'"
        try:
            db_i(sql)
            print("삭제완료")
        except:
            print("삭제불가")
            
    def okClick3_5():
        root1.destroy()
        global num1
        num1 = 0
        return
  
    while num1: 
    # 버튼 클릭 이벤트 핸들러
        root1 = Tk()
        root1.geometry("100x200+200+100")
        lbl = Label(root1, text="창고관리")
        lbl.pack()
    # 버튼 클릭 이벤트와 핸들러 정의
        btn1 = Button(root1, text="등록", command=okClick3_1)
        btn1.pack()
        btn2 = Button(root1, text="변경", command=okClick3_2)
        btn2.pack()
        btn3 = Button(root1, text="조회", command=okClick3_3)
        btn3.pack()
        btn4 = Button(root1, text="삭제", command=okClick3_4)
        btn4.pack()
        btn5 = Button(root1, text="뒤로", command=okClick3_5)
        btn5.pack()
        root1.mainloop()
    
########################################################################################
def okClick4():
    root.destroy()
    global num
    num = 0
    return
###############################################################################
while num: 
    num1= 1
# 버튼 클릭 이벤트 핸들러 
    root = Tk()             
    root.geometry("100x200+200+100")
    lbl = Label(root, text="허브관리")
    lbl.pack()
# 버튼 클릭 이벤트와 핸들러 정의
    btn1 = Button(root, text="상품관리", command=okClick1)
    btn1.pack()
    btn2 = Button(root, text="주문관리", command=okClick2)
    btn2.pack()
    btn3 = Button(root, text="창고관리", command=okClick3)
    btn3.pack()
    btn4 = Button(root, text="종   료", command=okClick4)
    btn4.pack()
    root.mainloop()
