from student import Student
from students import Students

stus = Students()
stuNum = 1 

def readStu():
    global stuNum
    with open("c:/aaa/stu.txt","r",encoding="utf-8") as f:
        while True:
            str = f.readline() 
            if str == "": break
            stu = str.split(",")
            for i,s in enumerate(stu):
                if 0<=i<=1: continue
                elif 2<=i<=5: stu[i] = int(s.strip())
                elif i==6: stu[i] = float(s.strip())
            stus.add(Student(stu[0],stu[1],stu[2],stu[3],stu[4],stu[5],stu[6]))
            stuNum = len(stus.slist)+1
               
def main_screen():
    print("[ 학생성적프로그램 ]")
    print("1. 학생성적입력 ")
    print("2. 학생성적출력 ")
    print("3. 학생성적수정 ")
    print("9. 학생성적파일저장 ")
    print("0. 학생프로그램종료 ")
    print("-"*60)
    choice = int(input("원하는 번호를 입력하세요.>> "))
    return choice

def stu_input():
    global stuNum
    while True:
        print()
        print("[ 학생성적입력 ]")
        no = stuNum
        name = input(f"{stuNum}번째 이름입력 (0.이전화면이동) : ")
        if name =="0": break
        kor = int(input("국어점수입력 : "))
        eng = int(input("영어점수입력 : "))
        math = int(input("수학점수입력 : "))
        total = kor + eng + math
        avg = total/3
        stus.add(Student(no,name,kor,eng,math))
        print(f"{stuNum}.{name} 학생성적이 저장되었습니다.")
        print()
        stuNum +=1

def stu_output():
     stus.print()
  
def stu_update():
    print()
    print("[ 학생성적수정 ]")
    name = input("찾으려는 학생이름을 입력하세요.>> ")
    temp = 0
    for s in stus.slist:
         if s.name == name:
             temp = 1
             print(f"{name}학생이 검색되었습니다.")
             print("[ 수정과목 ]")
             print("1.국어  2.영어  3.수학")
             print("-"*60)
             choice = int(input("과목을 선택하세요.(0.취소)>> "))
             if choice == 0:
                 break
             elif choice == 1:
                 print("[ 국어점수 변경 ]")
                 print("현재점수 : ",s.kor)
                 s.kor = int(input("변경점수입력 : "))               
             elif choice == 2:
                 print("[ 영어점수 변경 ]")
                 print("현재점수 : ",s.eng)
                 s.eng = int(input("변경점수입력 : "))              
             elif choice == 3:
                 print("[ 수학점수 변경 ]")
                 print("현재점수 : ",s.math)
                 s.math = int(input("변경점수입력 : "))
 
             s.s_total()
             s.s_avg()
             print("수정이 완료되었습니다.")
             print()

    if temp==0:
            print(f"{name} 학생이 없습니다. 다시 검색하세요.")  


def writeStu():
    print()
    print("[ 학생성적파일저장 ]")
    with open("c:/aaa/stu.txt", "w", encoding="utf-8") as f:
        if len(stus) == 0:
            print("저장할 학생 성적이 없습니다.")
            f.write(str)
        for s in stus:
            f.write(f"{s['no']}\t{s['name']}\t{s['kor']}\t{s['eng']}\t{s['math']}\t{s['total']}\t{s['avg']:.2f}\n")
    print("학생 성적 파일 저장이 완료되었습니다.")
    print("저장 파일 : stu.txt")