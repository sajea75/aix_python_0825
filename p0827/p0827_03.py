# # 랜덤향수
# Import random #파이썬에 있는 random클래스 사용하겠다 선언

# # 첫번째입력숫자~두번째입력숫자까지 랜덤으로 정수값 1개 

# 
#print(num)

# 1-5 




# # 1-5 랜덤 숫자를 출력하시오.
# num =random.randint(1,5) # 1~5까지 랜덤숫자 생성
# input1 = int(input("1-5까지 범위의 숫자를 입력하세요>> "))
# input2 = int(input("1-5까지 범위의 숫자를 입력하세요>> "))
# print("랜덤숫자 : ",num)
# print("입력숫자 : ",input1)
# if (num==input1) or (num==input2):
#     print("당첨!!")
# else:
#     print("꽝!!")




# 산술 연산자 +,-,*,/,//,%,**
# 비교연산자 ==, !=, >,<,>=<=
# 논리연산자 and,or,xor



# # 입력한 숫자가 2의 배수인지, 아닌지 출력하시오.
# # a%2 ==0
# a = int(input("숫자입력: "))
# if a%2 == 0: # ==, !=, >,<







# # a,b 를 입력받아
# # 합계가 100 넘으면 100큰수, 100작은수라고 출력하시오.

# # 1. 숫자입력
# a = int(input("숫자입력 : "))
# b = int(input("숫자입력 : "))
# # 2. 합계
# total = a+b
# # 3. 조건
# if total>100:
#     print("100보다 큰수")
# else:
#     print("100보다 작은수")

# print("입력숫자:{},{} / 합계:{}".format(a,b,total))
# print(f"입력숫자:{a},{b} / 합계:{total}")