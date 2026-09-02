# 반복문믈 사용해서 1-100까지 합을 출력 하시오.
tatol_sum = 0
for i  in range(1, 100):
    tatol_sum  += i
    print("-" *30)
# 200을 넘는  시점의 i위 값과 i번째 합계를 출력하시오.
tatol_sum = 0
for i in range(1, 100):
   if tatol_sum > 200:
    print(f"200을 넘는 시점의 i: {i}, 합계: {tatol_sum}")
    break

print("-" *30)

# 구구단을 출력하시오
for i in range(2,10):  #2단부터 9단까지
    print(f"=== {i}단 ===")
    for j in range(1, 10):
        print(f"{i} x {j} = {i * j}")
        print() # 단별 줄바꿈


stu = []
for i in range(100):
    no = i+1
    name = input("이름입력 : ")
    kor = int(input("국어점수 입력 : "))
    stu.append([no,name,kor])

for i in range(2):
    print("{}\t{}\t{}".format(stu[i][0],stu[i][1],stu[i][2]))





