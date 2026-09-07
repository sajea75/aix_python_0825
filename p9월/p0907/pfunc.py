stuList = []
title = ["번호","이름","국어","영어","수학","합계","평균","등수"]
s_title = ["no","name","kor","eng","math","total","avg","rank"]
stuNum = 1 

while True:
    print("[ 학생성적프로그램 ]")
    print("1. 성적입력")
    print("2. 성적출력")
    print("3. 성적수정")
    print("0. 프로그램종료")
    print("-"*60)
    choice = int(input("원하는 번호 입력 : "))
    if choice == 1:
        while True:
            print()
            print("[ 학생성적입력 ]")
            no = stuNum 
            name = input(f"{stuNum}번째. 학생이름(0.이전페이지 이동): ")
            if name == "0": break
            kor = int(input("국어 : "))
            eng = int(input("영어 : "))
            math = int(input("수학: "))
            total = kor+eng+math
            avg = total/3
            rank = 0
            stuList.append({'no':no,'name':name,'kor':kor,\
                            'eng':eng,'math':math,\
                                'total':total,'avg':avg,\
                                        'rank':rank,})
            print(f"{stuNum}.{name} 학생성적이 저장되었습니다.")
            print()
            stuNum += 1

    elif choice == 2:
        print()
        print(" "*25,end="")
        print("[ 학생성적출력 ]")
        print("{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}".format(*title))
        print(" "*60)
        for s in stuList:
            print(f"{s['no']}\t{s['name']}\t{s['kor']}\t{s['eng']}\t{s['math']}\t{s['total']}\t{s['avg']}\t{s['rank']}\t")
            print()

    elif choice == 3:
        pass
    elif choice == 9:
        pass
    else:    
        print("프로그램 종료")
        break

    


