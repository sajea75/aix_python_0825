total = ["번호","이름","국어","영어","수학","합계","평균"]
k_total = ["no","name","kor","eng","math","total","avg"]
stu = []
sno = 1

while True:
    print("[ 학생성적프로그램 ]")
    print("-"*60)
    print("1. 학생성적입력 ")
    print("2. 학생성적출력 ")
    print("3. 학생성적수정 ")
    print("4. 학생성적삭제 ")
    print("-"*60)
    choice = int(input("원하는 번호를 입력해주세요.>> "))
    print()

    if choice == 1:
        while True:
            no = sno
            print("[ 학생성적입력 ]")
            name = input(f"{no}번째 이름 입력(0.이전화면이동): ")
            if name == "0": break
            kor = int(input("국어점수 입력 : "))
            eng = int(input("영어점수 입력 : "))
            math = int(input("수학점수 입력 : "))
            total = kor + eng + math
            avg = total/3
            stu.append({"no":no,"name":name,"kor":kor,"eng":eng,"math":math,"total":total,"avg":avg})
            print(f"{name} 학생성적이 저장되었습니다.")
            sno += 1
            print()

    if choice == 2:
        print("[ 학생성적출력 ]")
        print("-"*60)
        print("번호\t이름\t국어\t영어\t수학\t합계\t평균")
        print("-"*60)
        for s in stu:
            print("{}\t{}\t{}\t{}\t{}\t{}\t{}".format(*total))
        stu.append(f"{s['no']}\t{s['name']}\t{s['kor']}\t{s['eng']}\t{s['math']}\t{s['total']}\t{s['avg']}:.2f")
        print()





                