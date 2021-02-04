# print("python", "java", sep=" vs ")
print("python", "java", sep=" , ", end ="?") #end는 줄의 끝에 end의 값을 넣어라
print("무엇이 더 재미있을까요?")

import sys
print("python", "java", file=sys.stdout) #표준 출력으로 표현
print("python", "java", file=sys.stderr) #표준 에러로 표현

#시험성적
scores = {"수학":0, "영어":50, "코딩":100}
for subject, score in scores.items():
    # print(subject, score)
    print(subject.ljust(8), str(score).rjust(4), sep = ":") #ljust 왼쪽정렬 rjust 오른쪽 정렬

#은행 대기 순번표
#001,002,003....
for num in range(1,21):
    print("대기번호 : " + str(num).zfill(3))

answer = input("아무 값이나 입력하세요 : ") 
print(type(answer))
print("입력하신값은" + answer + "입니다.")
