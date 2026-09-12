# 학생성적프로그램

title = ["번호", "이름", "국어", "영어", "수학", "합계", "평균"]
k_title = ["no", "name", "kor", "eng", "math", "total", "avg"]

stu = []
sno = 1   # 학생성적인원변수


while True:

    # ==================================
    # 메인화면
    # ==================================

    print()
    print("[ 학생성적프로그램 ]")
    print("1. 성적입력")
    print("2. 성적출력")
    print("3. 성적수정")
    print("9. 성적파일저장")
    print("0. 성적프로그램종료")
    print("-" * 60)

    choice = int(input("원하는 번호 입력: "))


    # ==================================
    # 1. 학생성적입력
    # ==================================

    if choice == 1:

        while True:

            no = sno

            print()
            print("[ 학생성적입력 ]")

            name = input(
                f"{no}번째 이름입력 (0.이전화면 이동): "
            )

            if name == "0":
                break

            kor = int(input("국어점수 입력 : "))
            eng = int(input("영어점수 입력 : "))
            math = int(input("수학점수 입력 : "))

            total = kor + eng + math
            avg = total / 3

            # 학생정보 저장
            stu.append({
                "no": no,
                "name": name,
                "kor": kor,
                "eng": eng,
                "math": math,
                "total": total,
                "avg": avg
            })

            print()
            print(f"{name} 학생성적이 저장 되었습니다.")

            sno += 1


    # ==================================
    # 2. 학생성적출력
    # ==================================

    elif choice == 2:

        print()
        print("[ 학생성적 출력 ]")
        print("-" * 60)

        print("{}\t{}\t{}\t{}\t{}\t{}\t{}".format(*title))

        print("-" * 60)

        if len(stu) == 0:

            print("** 학생데이터가 없습니다. **")

        else:

            for s in stu:

                print(
                    f"{s['no']}\t"
                    f"{s['name']}\t"
                    f"{s['kor']}\t"
                    f"{s['eng']}\t"
                    f"{s['math']}\t"
                    f"{s['total']}\t"
                    f"{s['avg']:.2f}"
                )

        print()


    # ==================================
    # 3. 학생성적수정
    # ==================================

    elif choice == 3:

        print()
        print("[ 학생성적수정 ]")

        name = input(
            "찾으려는 학생이름을 입력하세요.>> "
        )

        temp = 0

        for i, s in enumerate(stu):

            if s["name"] == name:

                print(f"{name} 학생을 찾았습니다.")

                temp = 1

                print()
                print("[ 과목수정선택 ]")
                print("1. 국어")
                print("2. 영어")
                print("3. 수학")

                choice = int(
                    input("원하는 번호입력 : ")
                )

                if choice < 1 or choice > 3:

                    print("잘못된 번호입니다.")

                    break

                # 과목번호 설정
                subject_index = choice + 1

                # 딕셔너리 키 설정
                subject_key = k_title[subject_index]

                # 과목 이름 설정
                subject_name = title[subject_index]

                print(
                    f"현재 {subject_name}점수 : "
                    f"{s[subject_key]}"
                )

                # 점수 수정
                s[subject_key] = int(
                    input(
                        f"변경하려는 {subject_name}점수입력 : "
                    )
                )

                # 합계 재계산
                s["total"] = (
                    s["kor"]
                    + s["eng"]
                    + s["math"]
                )

                # 평균 재계산
                s["avg"] = s["total"] / 3

                print()
                print(
                    f"{s[subject_key]}점으로 "
                    f"{subject_name}점수가 변경되었습니다."
                )

                print(f"새로운 합계 : {s['total']}")
                print(f"새로운 평균 : {s['avg']:.2f}")

                break

        if temp == 0:

            print(f"{name} 학생이 없습니다.")


    # ==================================
    # 9. 학생성적파일저장
    # ==================================

    elif choice == 9:

        print()
        print("[ 학생성적 파일저장 ]")

        with open("c:/aaa/student.txt", "w", encoding="utf-8") as f:

            # 제목 저장
            f.write(
                "{}\t{}\t{}\t{}\t{}\t{}\t{}\n".format(*title)
            )

            # 학생정보 저장
            for s in stu:

                f.write(
                    f"{s['no']}\t"
                    f"{s['name']}\t"
                    f"{s['kor']}\t"
                    f"{s['eng']}\t"
                    f"{s['math']}\t"
                    f"{s['total']}\t"
                    f"{s['avg']:.2f}\n"
                )

        print("학생성적이 student.txt 파일에 저장되었습니다.")


    # ==================================
    # 0. 프로그램종료
    # ==================================

    elif choice == 0:

        print()
        print("학생성적프로그램을 종료합니다.")

        break


    # ==================================
    # 잘못된 번호
    # ==================================

    else:

        print("잘못된 번호입니다.")
        print("다시 입력해주세요.")
