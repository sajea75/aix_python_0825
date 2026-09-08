# stus = Students()
# student -> Student
# 홍길동성적 -> stus.add(s1)
# 유관순성적 -> stus.add(a2)




# stus.print




#stuList = []




# student -> student클래스
# 홍길동성적 -> stuList.append(s1)
# 유관순성적 -> stuList.append(s2)

#학생성적을 출력하시오.
# for문 사용을 해서 출력하시오.


class Student:

    def __init__(self, no, name, kor, eng, math):
        self.no = no
        self.name = name
        self.kor = kor
        self.eng = eng
        self.math = math

    def total(self):
        return self.kor + self.eng + self.math

    def avg(self):
        return self.total() / 3


# 학생 성적을 저장할 리스트
stuList = []


# 학생 객체 생성
s1 = Student(1, "홍길동", 90, 80, 70)
s2 = Student(2, "유관순", 100, 90, 80)


# 리스트에 학생 객체 추가
stuList.append(s1)
stuList.append(s2)


# 학생 성적 출력
print("==========================================")
print("              학생 성적 출력")
print("==========================================")

for stu in stuList:
    print(
        "번호:", stu.no,
        "이름:", stu.name,
        "국어:", stu.kor,
        "영어:", stu.eng,
        "수학:", stu.math,
        "총점:", stu.total(),
        "평균:", round(stu.avg(), 2)
    )

print("==========================================")
