# 입력한 숫자를 모두 저장해서 프로그램을 종료할때 출력하시오.
noArr = [10,40,2,9,5]
no = []
answer = []
count = 0
while True:
    i_no = int(input("숫자입력 : ")) # 1,2,3,4,5
    # 1. 0을 입력할때 반복문 break
    if i_no == 0: break

    # 2.입력한 숫자 리스트에 저장
    no.append(i_no)

for i in no:
    if i in noArr:
        count = count + 1
        answer.append(i)

# 3. 반복문 종료시, 입력된 숫자 모두출력
print("리스트 : ",noArr)
print("입력숫자 : ",no)
print("정답숫자 : ",answer)
print("정답개수 :",count)

# 파이 * 반지름 * 반지름
# 2 * 파이 * 반지름

a = float(input("반지름을 입력하세요.>>"))
pi = 3.14
print("넓이 : ",pi*a*a)
print("넓이 : ",pi*a**2)
print("원의 둘레 : ",2*pi*a)

# a = input("숫자입력 : ")
# a = int(a)
# result = a*2.54
# print("inch : ",a)
# print("cm : ",result)