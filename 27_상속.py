class Unit:
    def __init__(self, name, hp): # __init__ : 셍성자
        self.name = name # self.?? : 멤버 변수 : 클래스네에서 정의된 변수
        self.hp = hp

# Unit을 상속 받아서 클래스 생성
class AttackUnit(Unit):
    def __init__(self, name, hp, damage):
        Unit.__init__(self, name, hp) # 상위 클래스에서 변수 초기화를 위해 호출
        self.damage = damage

    def attack(self, location): # self -> 자기 자신
        print("{0} : {1} 방향으로 적군을 공격 합니다. [공격력 : {2}]".format(self.name, location, self.damage))

    def damaged(self, damage):
        print("{0} : {1} 데미지를 입었습니다.".format(self.name, damage))
        self.hp -= damage
        print("{0} : 현재 체력은 {1} 입니다.".format(self.name, self.hp))
        if self.hp <= 0:
            print("{0} : 파괴되었습니다.".format(self.name))

firebat1 = AttackUnit("파이어뱃", 50, 16)
firebat1.attack("1시")

firebat1.damaged(25)
firebat1.damaged(25)