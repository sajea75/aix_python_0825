# 정수를 특정 칸에 출력하기.

# 정수
# output_a = "{:d}".format(52)

# # 특정 칸에 출력하기
# output_b = "{:5d}".format(52)  # 5칸
# output_c = "{:10d}".format(52) # 10칸

# # 빈칸을 0으로 채우기
# output_d = "{:05d}".format(52) # 양수
# output_e = "{:05d}".format(-52) # 음수

# print("#기본")
# print(output_a)
# print("# 특정 칸에 출력하기")
# print(output_b)
# print(output_c)
# print("# 빈칸을 0으로 채우기")
# print(output_d)
# print(output_e)

# 기호 붙여 출력하기.

# 기호 와 함께 출력하기
# output_f = "{:+d}".format(52) # 양수
# output_g = "{:+d}".format(-52) # 음수
# output_h = "{: d}".format(52) # 양수: 기호 부분 공백
# output_i = "{: d}".format(-52) # 음수: 기호 부분 공백

# print("# 기호와 함께 출력하기")
# print(output_f)
# print(output_g)
# print(output_h)
# print(output_i)

# 조합해 보기

# 조합 하기
# output_h = "{:+5d}".format(52) # 기호를 뒤로 밀기: 양수
# output_i = "{:+5d}".format(-52) # 기호를 뒤로 밀기: 음수
# output_j = "{:=+5d}".format(52) # 기호를 앞으로 밀기: 양수
# output_k = "{:=+5d}".format(-52) # 기호를 앞으로 밀기: 음수
# output_l = "{:+05d}".format(52) # 0으로 채우기: 양수
# output_m = "{:+05d}".format(-52) # 0으로 채우기: 음수

# print("# 조합하기")
# print(output_h)
# print(output_i)
# print(output_j)
# print(output_k)
# print(output_l)
# print(output_m)
