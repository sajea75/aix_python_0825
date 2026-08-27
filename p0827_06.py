# score = 65
# # score 60점이상이면 합격,불합격
# if score>=60: print("합격")
# else: print("불합격")

# # if문 축약
# reuslt ="합격" if score>=60 else "불합격"


# # 날짜함수를 사용하려면
# import datetime
# now = datetime.datetime.now()

# # 해당월에 따라 봄,여름,가을,겨울이라고 출력하시오.
# # 겨울 12,1,2 봄 3,4,5 여름 6,7,8 가을 9,10,11
# # 비교문을 사용해서
# # 해당월 계절을 출력하시오.
# # now.month

# month = now.month
# month = int(input("월을 입력하세요."))
# if month==12 or 1<=month<=2:
#     print("겨울입니다.")
# elif 8>=month>=6:
#     print("여름입니다.")
# elif 5>=month>=3:
#     print("봄입니다.")


# else:
#     print("가을입니다.")


# if 11>=month>=9:
#     print("가을입니다.")
# elif 8>=month>=6:
#     print("여름입니다.")
# elif 5>=month>=3:
#     print("봄입니다.")
# else:
#     print("겨울입니다.")















# if : 조건문
# if
# if - else
# if elif else
# if elif elif else

# if 조건문:
#    들여쓰기 되어야 함.
# else:
#    들여쓰기 되어야 함.

# if 10>5:
#     pass   # 출력이나 기타 프로그램이 없을시 pass
#     # 빈공백이면 에러감.
# print("프로그램")

# if 10>5: pass
# if 10>5: print("참")  # if 한줄가능
# if 10>5:
#     print("참")

# if 10>5: # 명령어가 2줄이상이면 다음줄에 넣어야 함.
#     print










# elif score >= 70:
# if score >= 78:
#     grade = "C+"
# elif score >=73:
#     grade = "C-"
# elif score >=60:
#     grade = "D"
# else:
#     grade = "f"

#     print(f"학점 : {grade}")














# import random
# # 0-100점  랜덤 숫자 생성
# # 60점 이상 합격
# # 50-59점까지 재시험 if score>=50 / if 50<score<=59:
# #0-49점까지 불합격

# import random

# # 0-100점 랜덤 숫자 생성
# score = random.rendint(0, 100)
# print("생성된 점수:", score)

# #조건에 따른 판정 출력
# if score >= 60:
#  print("합격")
# elif score >= 50: # 50점 이상 60점
#  print("재시험")
# else:
#  print("불합격")
 









# import random

# random_no = random.randint(-2,2)
# print("랜덤 숫자 : ", random_no)

# # 양수, 음수, 0 판단 및 출력
# if random_no > 0:
#     print("양수입니다.") 
# elif random_no == 0:
#     print("음수입니다.")
# else:
#     print("0입니다.")



#  # 조건문을 여러개
# score = 65
# if score>=90:
#     print("A")
# elif score>=80:
#     print("B")
# elif score>=70:
#     print("C")
# elif score>=60:
#     print("D")
# else:
#     print("F")