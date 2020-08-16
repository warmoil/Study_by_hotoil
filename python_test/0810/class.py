# #마린:공격유닛,군인,총을쏠수 있음
# name="마린"
# hp=40
# damage=6

# print("{0} 유닛이 생성되었습니다".format(name))
# print("체력{0},공격력{1}\n".format(hp,damage))
# tank_name="탱크"
# tank_hp=150
# tank_damage=35
# tank2_name="탱크"
# tank2_hp=150
# tank2_damage=35

# print("{0} 유닛이 생성되었습니다".format(tank_name))
# print("체력{0},공격력{1}\n".format(tank_hp,tank_damage))

# def attack(name,location,damage):
#     print("{0}:{1}방향으로 적군을 공격합니다.[공격력{2}]".format(\
#     name,location,damage))

# attack(name,"1시",damage)
# attack(tank_name,"1시",tank_damage)
# attack(tank2_name,"1시",tank2_damage)

class Unit:
    def __init__(self,name,hp,damage):
        #self를 제외하고는 다 똑같은 갯수만큼 적어야함 name hp damage
        self.name=name
        self.hp=hp
        self.damage=damage
        print("{0} 유닛이 생성 되었습니다".format(self.name))
        print("체력{0},공격력{1}".format(self.hp,self.damage))

marine1=Unit("마린",40,5)
marine2=Unit("마린",40,5)
tank=Unit("탱크",150,35)
#레이스:공중 유닛,비행기,클로킹(상대방에게 보이지않음)
wraith1=Unit("레이스",80,5)
print("유닛 이름:{0},공격력{1}".format(wraith1.name,wraith1.damage))
#마인드 컨트롤:상대방 유닛을 내것으로 만드는것(빼앗음)
wraith2=Unit("빼앗은 레이스",80,5)
wraith2.cloking=True

if wraith2.cloking == True:
    print("{0}는 현재 클록킹중입니다".format(wraith2.name))