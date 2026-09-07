# import p_stu_m as pm
from p_stu_m import *

# 학생성적 파일불러오기
def readStu():
    with open("c:/aaa/stu.txt","r",encoding="utf-8") as f:
        while True:
            str = f.readline()  #1,홍길동,100,100,100,300,100.0
            if str == "": break
            stu = str.split(",")
            for i,s in enumerate(stu):
                if 0<=i<=1: continue
                elif 2<=i<=5: stu[i] = int(s.strip())
                elif i==6: stu[i] = float(s.strip())
                elif i==7: stu[i] = int(s.strip())


            stuList.append(딕셔너리)




while True:
    # 0.메인화면함수
    choice = main_screen()
    if choice == 1:
        stu_input()    # 1.학생성적입력함수
    elif choice == 2:
        stu_output()   # 2.학생성적출력함수
    elif choice == 3:
        pass
    elif choice == 9:
        pass
    else:
        print("프로그램 종료")
        break
