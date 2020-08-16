from random import *
#다중상속
class Unit:
    def __init__(self,name,hp,speed):
        self.name=name
        self.hp=hp
        self.speed=speed
    def move(self,location):
        print("[지상유닛이동]")
        print("{0}:{1}방향으로 이동합니다 [속도{2}]"\
            .format(self.name,location,self.speed))
    #공격유닛
class AttackUnit(Unit):
     def __init__(self,name,hp,speed,damage):
        #self를 제외하고는 다 똑같은 갯수만큼 적어야함 name hp damage
        Unit.__init__(self,name,hp,speed) 
        self.damage=damage


     def attack(self,location):
        print("{0}:{1} 방향으로 적군을 공격합니다.[공격력{2}]"\
            .format(self.name,location,self.damage))

     def damaged(self,damage):
        print("{0}:{1}데미지를 입었습니다.".format(self.name,damage))
        self.hp-=damage
        
        if self.hp >0:
            print("{0}:현재 체력은{1}입니다".format(self.name,self.hp))
        else:
            print("{0}:파괘되었습니다!!!!!!!!lol!!!!!!!".format(self.name))
#날수있는 기능을 가진클래스
class Flyable:
    def __init__(self,flying_speed):
        self.flying_speed=flying_speed

#드랍쉽:공중,수송기,공격x
    def fly(self,location):
        print("{0}:{1} 방향으로 날아갑니다.[속도{2}]"\
            .format(self.name,location,self.flying_speed))
#공중공격 유닛 클래스
class FlyableAttackUnit(AttackUnit,Flyable):
    def __init__(self,name,hp,damage,flying_speed):
        AttackUnit.__init__(self,name,hp,0,damage)   #지상speed 0
        Flyable.__init__(self,flying_speed) 
    # def move(self,location):
    #     print("[공중유닛 이동]")
    #     self.fly(self.name,location)


# 벌쳐:지상유닛,기동성좋음
vulture=AttackUnit("벌쳐",80,10,20)

#배틀크루저:공중유닛,체력 공 좋음
battlecruiser=FlyableAttackUnit("배틀쿠루저",500,25,3)

# vulture.move("11시")
# battlecruiser.fly("9시")
# print("벌쳐:"+str(vulture))
# print("ㅂㅐ틀쿠루져:"+str(battlecruiser))
# print("벌쳐:"+str(vulture))
# print("ㅂㅐ틀쿠루져:"+str(battlecruiser))

# battlecruiser.move("9시")

#마린
class Marine(AttackUnit):
    def __init__(self):
        
        AttackUnit.__init__(self,"마린",40,1,5)
    
    def stimpack(self):
        if self.hp >10:
            self.hp-=10
            print("{0}:스팀팩을 사용합니다 (hp)감소".format(self.name))

        else:
            print("{0}:체력이 부족하여 스팀팩을 사용하지 않습니다".format(self.name))
    
class Tank(AttackUnit):
    #시즈모드 탱크를 지상에 고정시켜 ,더높은 파워로 공격가능,이동불가

    seize_developed=False#시즈모드 개발여부
    def __init__(self):
        AttackUnit.__init__(self,"탱크",150,1,35)
        self.seize_mode=False # 시즈모드 여부 (변수)
    def set_seize_mode(self): # 시즈모드 변경해! (메소드, 해라/풀어)
        if self.seize_developed==False:
            return
        if self.seize_mode==False:
            print("{0}:시즈모드로 전환합니다".format(self.name))
            self.damage*=2
            self.seize_mode=True

        else:
             print("{0}:시즈모드를 해제합니다".format(self.name))
             self.damage /=2
             self.seize_mode=False

#레이스
class Wraith(FlyableAttackUnit):
    def __init__(self):
        FlyableAttackUnit.__init__(self,"레이스",80,20,5)
        self.clocked=False #클로킹모드 해제상태

    def clocking(self):
        if self.clocked ==True:
            print("{0}:클로킹 모드 해제합니다".format(self.name))
            self.clocked=False

        else:
            print("{0}:클로킹 모드 설정합니다".format(self.name))
            self.clocked=True


def game_start():
    print("[알림] 새로운 게임을 시작합니다.")

def game_over():
    print("player:gg")
    print("[player]님이 게임에서 퇴장하셨습니다")

game_start()

m1 = Marine()
m2 = Marine()
m3 = Marine()

t1=Tank()
t2=Tank()
#유닛 일괄 관리 (생성된 모든 유닛 append)
w1=Wraith()
attack_units=[]
attack_units.append(m1)
attack_units.append(m2)
attack_units.append(m3)
attack_units.append(t1)
attack_units.append(t2)
attack_units.append(w1)
#전군 이동
for unit in attack_units:
    unit.move("1시")

#탱크 시즈모드 개발
Tank.seize_developed=True
print("[알림] 탱크시즈모드 개발이 완료되었습니다")

#공격 모드 준비 (마린:스팀팩,탱크:시즈모드,레이스:클로킹)
for unit in attack_units:
    if isinstance(unit,Marine):
        unit.stimpack()
    elif isinstance(unit,Tank):
        unit.set_seize_mode()
    elif isinstance(unit,Wraith):
        unit.clocking()

for unit in attack_units:
    unit.attack("1시")

# 전군 피해
for unit in attack_units:
    unit.damaged(randint(5,190))
cnt=0
for unit in attack_units:
    if unit.hp<1:
        cnt+=1
if cnt==6:
    print("졌어요 너는 루저예요")
else:
    print("이겼어요{0}개가 파괴되었어요".format(cnt))
#게임 종료
game_over()
