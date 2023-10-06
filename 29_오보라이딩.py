class Unit:
    def __init__(self, name, hp, speed):
        self.name = name
        self.hp = hp
        self.speed = speed

    def move(self, location):
        print("[지상 유닛 이동]")
        print("{0} : {1}시 방향으로 이동하였습니다. [속도 : {2}]".format(self.name, location, self.speed))

class AttackUnit(Unit):
    def __init__(self, name, hp, damage, speed):
        Unit.__init__(self, name, hp, speed)
        self.damage = damage

    def attack(self, location):
        print("{0} : {1}시 방향으로 공격했습니다. [공격력 {2}]".format(self.name, location, self.damage))

    def damaged(self, damage):
        print("{0} : {1} 데미지를 입었습니다.".format(self.name, damage))
        self.hp -= damage
        print("{0}의 현재 체력은 {1} 입니다.".format(self.name, self.hp))
        if self.hp <= 0:
            print("{0} 유닛은 파괴되었습니다".format(self.name))

class Flyable:
    def __init__(self, flying_speed):
        self.flying_speed = flying_speed

    def fly(self, name, location):
        print("{0} : {1}시 방향으로 이동하였습니다. [속도 {2}]".format(name, location, self.flying_speed))

class FlyAttackUnit(Flyable, AttackUnit):
    def __init__(self, name, hp, damage, flying_speed):
        AttackUnit.__init__(self, name, hp, damage, 0) # 지상 speed 0
        Flyable.__init__(self, flying_speed)

    # 메소드 오보라이딩 상속받은 클래스의 메소드를 재정의해서 사용
    def move(self, location):
        print("[공중 유닛 이동]")
        self.fly(self.name, location)

vulture = AttackUnit("벌쳐", 75, 20, 30)
vulture.move("7시")

battlecruisor = FlyAttackUnit("배틀크루저", 400, 25, 50)
battlecruisor.move("3시")


