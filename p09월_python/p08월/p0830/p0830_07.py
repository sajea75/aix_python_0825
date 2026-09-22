# 날짜/시간 활용하기.
# 날짜/시간과 관련된 기능을 가져옵니다.
# import datetime

# 현재 날짜/시간을 구합니다.
# now = datetime. datetime.now()

# 출력합니다.
# print(now.year, "년")
# print(now.month, "월")
# print(now.day, "일")
# print(now.hour, "시")
# print(now.minute, "분")
# print(now.second, "초")

# 날짜/시간을 한줄로 출력하기.
# 날짜/시간과 관련된 기능을 가져옵니다.
# import datetime

# 현재 날짜/시간을 구합니다.
# now = datetime.datetime.now()

# 출력합니다.
# print("{}년 {}월 {}일 {}시 {}분 {}초".format(
#     now.year,
#     now.month,
#     now.day,
#     now.hour,
#     now.minute,
#     now.second
# ))

# 오전과 오후를 구분하는 프로그램.
# 날짜/시간과 관련된 기능을 가져옵니다.
# import datetime

# 현재 날짜/시간을 구합니다.
# now = datetime.datetime.now()

# 오전 구분
# if now.hour < 12:
#     print("현제 시간은 {}시로 오전 입니다".format(now.hour))

# 오후 구분 
# if now.hour >= 12:
#     print("현재 시각은 {}시로 오후 입니다".format(now.hour))

# 계절 구분하는 프로그램.
# 날짜/시간과 관련된 기능을 가져옵니다.
# import datetime

# 현재 날짜/시간을 구합니다.
# now = datetime.datetime.now()

# 봄 구분 
# if 3 <= now.month <= 5:
#     print("이번 달은 {}월로 봄입니다".format(now.month))

# 여름 구분 
# if 6 <= now.month <= 8:
#     print("이번 달은 {}월로 여름입니다".format(now.month))

# 가을 구분 
# if 9 <= now.month <= 11:
#     print("이번 달은 {}월로 가을입니다".format(now.month))

# 겨울 구분 
# if now.month == 12 or 1<= now.month <= 2:
#     print("이번 달은 {}월로 겨울입니다".format(now.month))

# 끝짜리로 짝수와 홀수 구분.
# 입력을 받습니다.
# number = input("점수 입력")

# 마지막 자리 숫자를 추출
# last_character = number[-1]

# 숫자로 변환하기
# last_number = int(last_character)

# 짝수 확인
# if last_number == 0 \
#    or last_number == 2 \
#    or last_number == 4 \
#    or last_number == 6 \
#    or last_number == 8:
#    print("짝수입니다")

# 홀수 확인
# if last_number == 1 \
#    or last_number == 3 \
#    or last_number == 5 \
#    or last_number == 7 \
#    or last_number == 9:
#    print("홀수입니다")
  