a = [1,2,3,4,5]
print(a)
print(*a)
print(a[0],a[1],a[2],a[3],a[4])


# # split() 구분자로 분리
# str1 = "1,홍길동,100,100,99"
# s = str1.split(",")
# print(s)    # 리스트-문자열
# print(s[4]) # 타입:문자열

# 번호,이름,국어,영어,수학,합계,평균을 출룍 하시오.
# str1 = "1,홍길동,100,100,99"
# s = st



#1.split(",") #[1,홍길동,]
# s[2] = int(s[2]) #국어
# s[3] = int(s[3])
# s[4] = int(s[4])
# s.append(s[2]+s[3]+s[4]) #합계추가
# s.append(s[2]+s[3]) #평균추가

# print("[학생성적프로그램]")
# print("번호\t이름\t국어\t영어\t수학\t합계\t평균")
# print("-"*60)  #문자*반복

# # *s :
# print("{}\t{}\t{}\t{}\t{}\t{}\t{:.2f}".format(*s))
# print("{}\t{}\t{}\t{}\t{}\t{}\t{:.2f}".format(*s))


# 함수
# paper ="네팔 대홍수 참사 수습이 언제 끝날지도 모르는 상황에서\
#     2차 홍수가 덮칠 수 있다는 관측이 나오고 있습니다.\
#     이번 홍수의 원인으로 지목된 것처럼 산 위의 빙하가 붕괴되면서\
#         비 한 방울 없이 홍수가 또 일어날 수 있다는 겁니다."

# if "코치 " in paper:
#     print("있음")
# else:
#     print("없음")


#     alist =[딸기,포도 =,바나나]




# paper ="네팔 대홍수 참사 수습이 언제 끝날지도 모르는 상황에서\
#     2차 홍수가 덮칠 수 있다는 관측이 나오고 있습니다.\
#     이번 홍수의 원인으로 지목된 것처럼 산 위의 빙하가 붕괴되면서\
#         비 한 방울 없이 홍수가 또 일어날 수 있다는 겁니다."

# result1 = paper.find("홍수")
# print(result1) #4

# #find(검색내용,시작위치,종료위지)
# result2 = paper.find("홍수",5)
# print(result2)



# result1 = paper.find("홍수")
# #print(result1)

# # result1 = paper.find("홍수")
# #print(result2)








# # print("[ 로그인페이지]")
# # while(True):
# #     id = input("아이디 :")
# #     pw = input("패스워드: ")
# #     if id=="aaa" and pw=="1111":
# #         print("로그인성공 메인페이지로 이동합니다.")
# #         break
# #     else:
# #         print("아이디 또는 패스워드가 일치하지 않습니다. 다시 로그인해주세요")



# # 문자인지 아닌지 확인 
# # 이름 을 입력 받는데 영문 이름 
# Name = input("이름을 입력 하시오")
# if Name.isalpha(): # 특수문자나 숫자인지 확인 가능
#     print("문 자 알파벳으로 되어 있습니다.")
# else:
#     print("특수문자나 숫자가 입력 되었습니다.")
#     #print(name)



# num = input("숫자를 입력 하세요.>>> ")
# if num.isdigit()





# # format함수
# a = 10
# print("{}".format(a))
# print("{:10d}".format(a))
# print(("{:+010d}".format(a)))
# print("{:+010d}".format(-10)) # + : 숫자 앞에 
# print("{:3,d}".format(123456789)) # 천단위 표시
# print("{:012.2f}".format(12.12345)) # 소수점 제한
