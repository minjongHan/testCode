from random import *

users = range(1,21)
print(list(users))
users = list(users)
shuffle(users)
print(users)
winner = sample(users, 4)
print(winner)

# print("-- 당첨자 발표 --")
# print("치킨 당첨자 : %s" %winner[0])
# print("커피 당첨자 : %s %s %s" %(winner[1] , winner[2], winner[3]))
# print("-- 축하합니다. --")

print("""-- 당첨자 발표 --
치킨 당첨자 : {0}
커피 당첨자 : {1}, {2}, {3}
-- 축하합니다. --""".format(winner[0],winner[1],winner[2],winner[3]))

# kitchin = sample(comment, 1)
# print(kitchin)
# comment.remove(str(kitchin))

# print(comment)
