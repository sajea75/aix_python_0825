import os
# r-읽기, w-덮어쓰기, a-이어쓰기
# 없는 폴더에 파일저장시 에러
fname = input("저장할 파일이름을 입력하세요(폴더/파일명)>> ")

if not os.path.exists("common"):
    os.makedirs("common") #폴더를 생성해줌.

with open("common/"+fname,"a") as f:
    while True:
        outstr = input("내용입력 : ")
        if outstr =="": break
        f.write(outstr+"\n")

print("파일내용이 저장되었습니다.")