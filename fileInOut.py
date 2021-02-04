# score_file = open("source.txt","w", encoding="utf-8")
# print("수학 : 0", file=score_file)
# print("영어 : 50", file=score_file)
# score_file.close()

# score_file = open("source.txt", "a", encoding="utf-8")
# score_file.write("과학 : 80")   #write는 줄바꿈이 없음
# score_file.write("\n코딩 : 100")
# score_file.close()

score_file = open("source.txt","r", encoding="utf-8")
print(score_file.read())
score_file.close()

score_file = open("source.txt","r", encoding="utf-8")
print(score_file.readline(), end="") # 한줄만 읽고, 커서는 다음줄로 이동
print(score_file.readline())
print(score_file.readline())
print(score_file.readline())
score_file.close()

#몇 줄일지 모를때
score_file = open("source.txt","r", encoding="utf-8")
while True:
    line = score_file.readline()
    if not line:
        break
    print(line)
score_file.close()

score_file = open("source.txt","r", encoding="utf-8")
lines = score_file.readlines() #list 형태로 저장
for line in lines:
    print("list형태" , line, end="")

score_file.close()