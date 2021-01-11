cabinet = {3:"유재석", 100:"김태호"}
print(cabinet[3])
print(cabinet[100])

print(cabinet.get(3))
# print(cabinet[5])
print("hi")
print(cabinet.get(5))
print(cabinet.get(5,"사용 가능"))

print(3 in cabinet)
print(5 in cabinet)

cabinet = {"A-3":"유재석", "B-100":"김태호"}
print(cabinet["A-3"])
print(cabinet["B-100"])

# 새 손님
print(cabinet)
cabinet["C-20"] = "조세호"
print(cabinet)

cabinet["A-3"] = "김종국"
print(cabinet)

# 간 손님
del cabinet["A-3"]
print(cabinet)

# key들만 출력
print(cabinet.keys())
print(cabinet.values())
print(cabinet.items())

# 손님들이 모두 나감
cabinet.clear()
print(cabinet)
