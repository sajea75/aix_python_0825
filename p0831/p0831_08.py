# 1-100사이의 랜덤번호를 맞추는 프로그램을 구현하시오.
# 랜덤번호보다 높은 수를 입력하면 낮은 숫자입력!!,높은 숫자입력!!
# 정답을 맞추면
# 정답숫자 :
# 숫자입력회수 :
# 입력한숫자 :

import random
randNum = random
randNum = random.randint(1,100) # 랜덤숫자생성
my_list = []    # 입력한숫자모두저장
myNum = 0       # 내가입력한숫자변수
answer = 0      # 정답변수
while True:
    myNum = int(input("1-100사이 숫자를 입력 : "))
    my_list.append(myNum)

    # 랜덤숫자와 입력숫자가 같은지 비교
    if myNum == randNum:
        answer = myNum
        print("정답입니다.")
        break
    elif myNum>randNum:
        print("입력한 숫자가 더 큽니다. 작은수 입력!!")
    else:
        print("입력한 숫자가 더 작습니다. 큰수 입력!!")

print("정답 : ",answer)
print("정답 : ",my_list[-1])
print("입력한모든 숫자 : ",my_list)

