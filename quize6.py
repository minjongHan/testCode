# Quize) 표준 체중을 구하는 프로그램을 작성하시오

# * 표준 체중 : 각 개인의 키에 적당한 체중

# (성별에 따른 공식)
# 남자 : 키(m) x 키(m) x 22
# 여자 : 키(m) x 키(m) x 21

# 조건1 :  표준 체중은 별도의 함수 내에서 계산
#     * 함수명 : std_weight
#     * 전달값 : 키(height), 성별(gender)
# 조건2 : 표준 체중은 소수점 둘째자리까지 표시

# (출력 예제)
# 키 175cm 남자의 표준 체중은 67.38kg 입니다.
from math import *
def std_weight(height, gender):
    weight = height * height
    if "남자" in gender:
        return weight * 22
    else:
        return weight * 21    

height = 172
gender = "남자"
weight = std_weight(height/100, gender)
print("키 {0}cm {1}의 표준 체중은 {2}kg 입니다.".format(height, gender,  round(weight,2)))
