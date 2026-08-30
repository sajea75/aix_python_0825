# int()함수와 float()함수 활용하기.

# output_a = int("52")
# output_b = float("52.273")

# print(type(output_a), output_a)
# print(type(output_b),output_b)

# int()함수와 float()함수 조합하기.

# input_a = float(input("첫 번째 숫자> "))
# input_b = float(input("두 번째 숫자> "))

# print("덧샘 결과:",input_a + input_b)
# print("뺄샘 결과", input_a - input_b)
# print("곱셈 결과", input_a * input_b)
# print("나눗셈 결과", input_a / input_b)

# str()함수를 사용해 숫자를 문자열로 변환하기.

# output_a = str(52)
# output_b = str(52.273)
# print(type(output_a),output_a)
# print(type(output_b),output_b)

# inch 단위를 cm 단위로 변경하기.

# 숫자를 입력 받습니다.
# raw_input =input("inch 단위의 숫자를 입력해주세요: ")

# # 입력받은 테이터를 숫자 자료형으로 변경하고, cm 단위로 변경합니다.
# inch = int(raw_input)
# cm = inch * 2.54

# # 출력 합니다.
# print(inch, "inch는 cm 단위로", cm, "cm입니다.")

#format()함수로 숫자를 문자열로 변환하기.

# format()함수로 숫자를 문자열로 변환하기
string_a = "{}".format(10)

# # 출력하기
# print(string_a)
# print(type(string_a))

# format()함수의 다양한 형태.

# format() 함수로 숫자를 문자열로 변환하기
# format_a = "{}만 원".format(5000)
# format_b = "파이썬 열공하여 첫 연봉 {}만 원 만들기 ".format(5000)
# format_c = "{} {} {}".format(3000,4000,5000)
# format_d = "{} {} {}".format(1, "문자열", True)

# #출력하기

# print(format_a)
# print(format_b)
# print(format_c)
# print(format_d)
