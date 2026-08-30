# 다양한 형태 의 부동 소수점 출력하기
# output_a = "{:f}".format(52.273)
# output_b = "{:15f}".format(52.273) # 15 칸 만들기
# output_c = "{:+15f}".format(52.273) # 15칸에 부호 추가하기
# output_d = "{:+015f}".format(52.273) # 15칸에 부호 추가하고 0으로 채우기

# print(output_a)
# print(output_b)
# print(output_c)
# print(output_d)

# 소수점 아래 자릿수 지정하기
# output_a = "{:15.3f}".format(52.273)
# output_b = "{:15.2f}".format(52.273)
# output_c = "{:15.1f}".format(52.273)

# print(output_a)
# print(output_b)
# print(output_c)

# 의미 없는 소수점 제거하기
# output_a = 52.0
# output_b = "{:g}".format(output_a)
# print(output_a)
# print(output_b)

# not 연산자 조합하기.
# x = 10
# under_20 = x < 20 # under_20 = (x < 20)
# print("under_20:", under_20)
# print("not under_20:", not under_20)

# 조건문의 기본 사용.
# # 입력을 받습니다.
# number = input("점수 입력> ")
# number = int(number)  

# # 양수 조건 
# if number > 0:
#     print("양수입니다")

# # 음수 조건
# if number < 0:
#     print("음수입니다")

#     # 0 조건 
# if number == 0:
# #     print("0입니다")

# while True:
#     number = input("점수 입력> ")
#     number = int(number)  

# # 양수 조건 
#     if number > 0:
#         print("양수입니다")

# # 음수 조건
#     elif number < 0:
#         print("음수입니다")

#     # 0 조건 
#     else:
#         print("0입니다")