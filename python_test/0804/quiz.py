from random import *
# lst=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
lst=list(range(1,21))
shuffle(lst)
a=lst.pop()
print("--당첨자 발표 --")
print("치킨 당첨자:"+str(a))
print("커피 당첨자:"+str(sample(lst,3)))
print("--축하합니다--")


#a=randint(0,20)
