# # 학생 성적표 를 여러명 의 이름 과 성적을 넣어서 성적표를 만드시오.
# # 1 박영훈 100 100 100 100
# no = input("번호 입력>> ")
# name = input("이름 입력>> ")
# kor = int(input("국어점수 입력>> "))
# eng = int(input("영어점수 입력>> "))
# math = int(input("수학점수 입력>> "))
# sci = int(input("과학점수 입력>> "))
# total = kor+eng+math
# avg = total/3

# # 2 이경화 100 100 91 100
# no2 = input("번호 입력>> ")
# name2 = input("이름 입력>> ")
# kor2 = int(input("국어점수 입력>> "))
# eng2 = int(input("영어점수 입력>> "))
# math2 = int(input("수학점수 입력>> "))
# sci = int(input("과학점수 입력>> "))
# total2 = kor2+eng2+math2
# avg2 = total2/3

# # 3 박현준 100 100 80 100
# no3 = input("번호 입력>> ")
# name3 = input("이름 입력>> ")
# kor3 = int(input("국어점수 입력>> "))
# eng3 = int(input("영어점수 입력>> "))
# math3 = int(input("수학점수 입력>> "))
# sci = int(input("과학점수 입력>> "))
# total3 = kor2+eng2+math2
# avg3 = total3/3

# # 4 박예진 100 100 80 90
# no4 = input("번호 입력>> ")
# name4 = input("이름 입력>> ")
# kor4 = int(input("국어점수 입력>> "))
# eng4 = int(input("영어점수 입력>> "))
# math4 = int(input("수학점수 입력>> "))
# sci = int(input("과학점수 입력>> "))
# total4 = kor2+eng2+math2
# avg4 = total4/3

# print("-"*60)
# print("번호\t이름\t국어\t영어\t수학\t\과학\t합계\t평균")
# print("-"*60)
# print("{}\t{}\t{}\t{}\t{}\t{}\t{:.2f}".\
# format(no,name,kor,eng,math,total,avg))
# print("-"*60)
# print("{}\t{}\t{}\t{}\t{}\t{}\t{:.2f}".\
# format(no2,name2,kor2,eng2,math2,total2,avg2))
# print("-"*60)
# print("{}\t{}\t{}\t{}\t{}\t{}\t{:.2f}".\
# format(3,name3,kor3,eng3,math3,total3,avg3))
# print("-"*60)
# print("{}\t{}\t{}\t{}\t{}\t{}\t{:.2f}".\
# format(no4,name4,kor4,eng4,math4,total4,avg4))
# print("-"*60)

# 로또 번호 랜덤 숫자.
# import random

# # 로또 랜덤부분
# lotto = random.sample(range(1,46),6)
# # print("확인로또>> : ",lotto)
# # 입력6개
# myNum = []
# i = 0
# while i<6:
#     no = int(input("숫자입력 : "))
#     if no not in myNum:
#         myNum.append(no)
#         i = i+1
#     else:
#         print("번호가 있습니다.")  

# # 맞는지 확인
# count = 0
# answer = []
# for i in myNum:
#     if i in lotto:
#         count = count+1
#         answer.append(i)

# print("로또번호 : ",lotto)
# print("입력한번호 : ",myNum)
# print("정답번호 : ",answer)
# print("정답개수 : ",count)
