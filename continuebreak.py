abset = [2, 5]
no_book =  [7]
for student in range(1, 11):
    if student in abset:
        continue
    elif student in no_book:
        print("오늘 수업 여기까지. {0}는 교무실로 따라와".format(student))
        break
    print("{0},  책을 읽어봐".format(student))


#한줄 for 문
#출석 번호 1 2 3 4, 앞에 100을 붙이기로 함 -> 101, 102, 103, 104.
student = [1, 2, 3, 4, 5]
print(student)
students = [i+100 for i in student]
print(students)

# 학생 이름을 길이로 변환
students = ["Iron man", "Thor", "I am groot"]
students = [len(i) for i in students]
print(students)

#학생 이름을 대문자로 변환
students = ["Iron man", "Thor", "I am groot"]
students = [i.upper() for i in students]
print(students)