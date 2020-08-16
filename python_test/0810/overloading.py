#다중상속
class Unit:
    def __init__(self,name,hp,speed):
        #self를 제외하고는 다 똑같은 갯수만큼 적어야함 name hp damage
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
        print("{0}:현재 체력은{1}입니다".format(self.name,self.hp))
        if self.hp <=0:
            print("{0}:파괴되었습니다".format(self.name))
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

vulture.move("11시")
battlecruiser.fly("9시")
print("벌쳐:"+str(vulture))
print("ㅂㅐ틀쿠루져:"+str(battlecruiser))
print("벌쳐:"+str(vulture))
print("ㅂㅐ틀쿠루져:"+str(battlecruiser))

battlecruiser.move("9시")
