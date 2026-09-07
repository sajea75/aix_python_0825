def add():
    num = int(input("숫자를 입력하세요. >>"))
    sum = 0
    for i in range(1,num+1):
        sum += i
    print(sum)

# 매개변수 1개
def add2(num2):
    num = int(input("숫자를 입력하세요. >>"))
    sum = 0
    for i in range(1,num+2):
        sum += i
        print(sum)
# 매개변수 2개
def add3(num3,num4):
    num = int(input("숫자를 입력하세요. >>"))
    sum = 0
    for i in range(num3,num4+1):
        sum += i
        print(sum)


# 10 반복
for i in range(10):
    add()

for i in range(10):
    num2 = int(input("숫자를 입력하세요. >>"))
    add2(num2)

for i in range(10):
    num3 = int(input("숫자를 입력하세요. >>"))
    num4 = int(input("숫자를 입력하세요. >>"))
    add2(num3,num4)