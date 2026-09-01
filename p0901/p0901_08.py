stu_list = [
    [1,"홍길동",100,90,80,270,90.0],
    [2,"유관순",90,80,70,240,80.0],
    [3,"이순신",80,70,60,210,70.0],
]

# 이름 점수 수정 방법
# 유관순 - 국어:100, 영어:50
# [2,"유관순",90,80,70,240,80.0]
c = 100
stu_list[1][3] = 50
stu_list[1][5] = stu_list[1][2]+stu_list[1][3]+stu_list[1][4]
stu_list[1][6] = stu_list[1][5]/3
   
print(stu_list)

# sut_list[0][1] = "홍길자"

print(stu_list)
print(stu_list[0][2],stu_list[0][3],stu_list[0][4])


# aa = []
# bb = []
# value = 0
# for i in range (0,100): #방법1
#     aa.append(value)
# value +=2
# print(aa)

# cc =list(range(0,200,2)) #방법2
# print(cc)

# # 리스트내포
# dd = [i+2 for i in range(0,200,2)]
# print(dd)

# for i in range(0,100):


# #
# #
# aa =[10,20,30]
# bb =[1,2,3
# print(aa*3)
# print(aa+bb) #aa,bb가 값이 변경됨.

# aa
# print(aa)

# a = 1
# b = 2


# aa.append(1) # aa값이 변경
# # append,insert,extend,pop, del : 값이 변경이 된다.

# aa = [1,2,3,4,5,6,7]
# print(aa[::-1])
# print(aa[::-2])

# aa = [1,2,3]
# aa[1:2] = [20.30]
# print(aa)
