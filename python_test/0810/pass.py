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
#건물
class BuildingUnit(Unit):
    def __init__(self,name,hp,location):
        #Unit.__init__(self,name,hp,0)
        super().__init__(name,hp,0)
        self.location=location