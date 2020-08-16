from random import *
# lst=list(range(5,51))
# shuffle(lst)
# print(lst)
# for i in range(1,51):
# if lst >= 15:
#     print("[0]")
# elif
#     print("[x]")



#     print("{0}번째 손님(소요시간:{1}분".format(i,lst.pop()))


cnt=0 #총 탑승 승객수
for i in range(1,51):#1~50
    time=randrange(5,51) #5~50분
    if 5<= time <= 15:
        print("[O] {0}번째 손님 (소요시간:{1}분".format(i,time))
        cnt +=1
    else:
        print("[ ] {0}번째 손님 (소요시간{1}분".format(i,time))

print("총 탑승 승객:{0}분".format(cnt))