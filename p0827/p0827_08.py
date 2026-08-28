arr2 = random.sample(range(1,101),3)
input1 = int(input("숫자입력 : "))
if input1 in arr2:
    print("당첨")
else:
    print("꽝")
print("랜덤숫자 :",arr2)
print("입력숫자 :",input1)















# 1-100까지 랜덤숫자 3개를 만들어서
# 2.1입력한 숫자가 1개가 있는 지를 확인해서
# 있으면 당첨, 없으면 꽝
# 랜덤숫자 리스트 출력
# 입력숫자 출력 

# import random

# # 1. 사용자로부터 숫자 1개 입력받기
# user_num = int(input("1부터 100 사이의 숫자를 입력 하세요: "))

# # 2. 1~100 사이의 랜덤 숫자 3개 생성 (중복 없이 뽑으려면 sample 사용)
# random_numbers = random.sample(range(1.101), 3)

# # 3. 입력한 숫자가 랜덤  숫자 리스츠에 있는지 확인 및 당첨/꽝 판정
# if user_num in random_numbers:
#     result = "당첨"

# # 4.출력 
# print(f"랜덤숫자 리스트: {random_numbers}")
# print(f"입력숫자:{user_num}")
# print(f"결과: {result}")

