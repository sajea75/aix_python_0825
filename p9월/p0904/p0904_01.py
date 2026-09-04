# 학생 정보를 저장할 리스트
student = []


# ==============================
# 메인 화면 함수
# ==============================
def s_mainPrint():
    print()
    print("==============================")
    print("       학생 성적 관리")
    print("==============================")
    print("1. 학생 성적 입력")
    print("2. 학생 성적 출력")
    print("3. 학생 성적 수정")
    print("4. 프로그램 종료")
    print("==============================")

    choice = int(input("메뉴를 선택하세요 : "))

    return choice


# ==============================
# 학생 성적 입력 함수
# ==============================
def s_input():
    print()
    print("[ 학생 성적 입력 ]")

    name = input("학생 이름 : ")
    kor = int(input("국어 점수 : "))
    eng = int(input("영어 점수 : "))
    math = int(input("수학 점수 : "))

    total = kor + eng + math
    avg = total / 3

    data = {
        "name": name,
        "kor": kor,
        "eng": eng,
        "math": math,
        "total": total,
        "avg": avg
    }

    student.append(data)

    print("학생 성적이 입력되었습니다.")


# ==============================
# 학생 성적 출력 함수
# ==============================
def s_output():
    print()
    print("[ 학생 성적 출력 ]")

    if len(student) == 0:
        print("등록된 학생이 없습니다.")
        return

    for i in range(len(student)):
        print("------------------------------")
        print("번호 :", i + 1)
        print("이름 :", student[i]["name"])
        print("국어 :", student[i]["kor"])
        print("영어 :", student[i]["eng"])
        print("수학 :", student[i]["math"])
        print("총점 :", student[i]["total"])
        print("평균 :", round(student[i]["avg"], 2))


# ==============================
# 학생 성적 수정 함수
# ==============================
def s_update():
    print()
    print("[ 학생 성적 수정 ]")

    if len(student) == 0:
        print("등록된 학생이 없습니다.")
        return

    for i in range(len(student)):
        print(i + 1, ".", student[i]["name"])

    no = int(input("수정할 학생 번호 : "))

    if no < 1 or no > len(student):
        print("잘못된 학생 번호입니다.")
        return

    index = no - 1

    print()
    print(student[index]["name"], "학생의 성적을 수정합니다.")

    kor = int(input("국어 점수 : "))
    eng = int(input("영어 점수 : "))
    math = int(input("수학 점수 : "))

    total = kor + eng + math
    avg = total / 3

    student[index]["kor"] = kor 
    student[index]["eng"] = eng
    student[index]["math"] = math
    student[index]["total"] = total
    student[index]["avg"] = avg

    print("학생 성적이 수정되었습니다.")


# ==============================
# 메인 프로그램
# ==============================
while True:

    choice = s_mainPrint()      # 메인화면 함수 호출

    if choice == 1:
        s_input()               # 학생 성적 입력

    elif choice == 2:
        s_output()              # 학생 성적 출력

    elif choice == 3:
        s_update()              # 학생 성적 수정

    elif choice == 4:
        print("프로그램을 종료합니다.")
        break

    else:
        print("잘못된 메뉴입니다.")
