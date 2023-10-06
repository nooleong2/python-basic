class Unit:
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp
        print("{0} 유닛이 생성되었습니다".format(self.name))

class AttackUnit(Unit):
    def __init__(self, name, hp, damage):
        Unit.__init__(self, name, hp)
        self.damage = damage

    def attack(self, location):
        print("{0} : {1}시 방향으로 적군을 공격합니다. [공격력 : {2}]".format(self.name, location, self.damage))

    def damaged(self, damage):
        print("{0} : {1} 데미지를 입었습니다.".format(self.name, damage))
        self.hp -= damage
        print("{0} 현재 체력은 {1} 입니다.".format(self.name, self.hp))
        if self.hp <= 0:
            print("{0} 유닛이 파괴되었습니다.".format(self.name))

class Flyable:
    def __init__(self, flying_speed):
        self.flying_speed = flying_speed

    def fly(self, location):
        print("{0} 방향으로 날라가고있습니다 [이동속도 : {1}]".format(location, self.flying_speed))

# 다중 상속일 경우 ,로 표시하면 됨
# Flyable, AttackUnit 클래스를 상속받아서 사용
class FlyAttackUnit(Flyable, AttackUnit):
    def __init__(self, name, hp, damage, flying_speed):
        Flyable.__init__(self, flying_speed) # 부모 클래스에 초기화 넘김
        AttackUnit.__init__(self, name, hp, damage) # 부모 클래스 초기화 넘김

# 단일 상속 인스턴스 생성
firebat = AttackUnit("파이어뱃", 50, 16)
firebat.attack("5시")
firebat.damaged(25)
firebat.damaged(25)

# 다중 상속 인스턴스 생성
valkyrie = FlyAttackUnit("발키리", 200, 6, 20)
valkyrie.attack("3시")
valkyrie.fly("5시")
valkyrie.damaged(100)
valkyrie.damaged(100)









