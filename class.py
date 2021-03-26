# #스타크래프트예제

# # 마린 : 공격 유닛, 군인. 총을 쓸 수 있음
# name = "마린"
# hp = 40
# damage = 5
# print("{} 유닛이 생성되었습니다.".format(name))
# print(" 체력 {0}, 공격력 {1}\n".format(hp, damage))

# #탱크 : 공격 유닛, 탱크. 포를 쏠수 있는데, 일반 모드 / 시즈모드.
# tank_name = "탱크"
# tank_hp = 150
# tank_damage = 35
# print("{} 유닛이 생성되었습니다.".format(tank_name))
# print(" 체력 {0}, 공격력 {1}\n".format(tank_hp, tank_damage))

# tank2_name = "탱크"
# tank2_hp = 150
# tank2_damage = 35
# print("{} 유닛이 생성되었습니다.".format(tank2_name))
# print(" 체력 {0}, 공격력 {1}\n".format(tank2_hp, tank2_damage))

# def attack(name, location, damage):
#     print("{0} {1} : 방향으로 적군을 공격 합니다. [ 공격력 {2}]".format(name, location, damage))

# attack(name, "1시", damage)
# attack(tank_name, "1시", tank_damage)
# attack(tank2_name, "1시", tank2_damage)

#하나의 클래스를 만듬
class Unit:
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage
        print("{0} 유닛이 생성되었습니다.".format(self.name))
        print(" 체력 {0}, 공격력 {1}\n".format(self.hp, self.damage))

#클래스 사용
marine1 = Unit("마린", 40, 5)   #self를 제외한 나머지를 적어줌
marine2 = Unit("마린", 40, 5)
tank = Unit("탱크", 150, 35)

#__init__ 파이썬에서 쓰이는 생성자를 말함
# 인자값은 정의한 갯수만큼 보내주어야 객체를 만들어 줄수 있다.
# name, hp, damage를 맴버 변수 라고 함

#레이스 : 공주 유닛, 비행기. 클로킹(상대방에게 보이지 않음)
wraith1 = Unit("레이스", 80, 5)
print("유닛이름: {0}, 공격력: {1}".format(wraith1.name, wraith1.damage))

#마인드 컨트롤 : 상대방 유닛을 내것으로 만들는 것
wraith2 = Unit("빼앗은 레이스", 80, 5)
wraith2.clocking = True #외부에서 변수를 선언해서 값을 넣어줄수 있음

if wraith2.clocking == True:
    print("{0}는 현재 클로킹 상태입니다.".format(wraith2.name))

#이처럼 클래스 외부에서 변수 선언을 통해 확장을 할수가 있고 그 범위는 해당 객체만 적용되며 기존의 다른 객체에서는 적용되지 않는다.


