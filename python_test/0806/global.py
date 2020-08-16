#지역변수와 전역변수
gun=10
def checkpoint(soldiers):#경계근무
    global gun #전역공간에있는 gun사용
    gun=gun-soldiers
    print("[함수내]남은 총:{0}".format(gun))
def checkpoint_ret(gun,soldiers):
    gun=gun-soldiers
    print("[함수내]남은 총:{0}".format(gun))
    return gun
print("전체총:{0}".format(gun))
checkpoint(2) #명이 경계근무 나감
print("남은 총:{0}".format(gun))