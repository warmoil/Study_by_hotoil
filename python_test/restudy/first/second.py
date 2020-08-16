#리스트 []
#지하철 칸별로 10 ,20 30 명
# subway1=10
# subway2=20
# subway3=30

# subway=["유재석","조세호","박명수"]
# print(subway)
# print(subway.index("조세호"))

# subway.append("하하")
 

# cabinet={3:"유재석",100:"김태호"}
# print(cabinet[3])
# print(cabinet.get(5,"사용가능"))
# if cabinet.get(5)==None:
#     print("사용이가능")

# singer_room=[11,2,3,4,5,6,7,8,9]
# for i in singer_room:
#     print(i)
from random import *
lst=[1,2,3,4,5,6,7,8,9,10]
shuffle(lst)

winner=sample(lst,3)
print(winner)
chiken=winner.pop()
print(chiken)
print(winner)

users=list(range(1,21))
shuffle(users)
print(type(users),users)