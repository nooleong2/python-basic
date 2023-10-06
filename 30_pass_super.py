# pass : 일단 더 이상 진행하지 않고 그냥 넘어간다는 뜻
class Unit:
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp

class BuildingUnit(Unit):
    def __init__(self, name, hp, location):
        pass # 아무 일도 하지 않고 넘어감

supply_depot = BuildingUnit("서플라이 디폿", 500, "7시")

# pass 활용 
def game_start():
    print("[알림] 게임 시잓")

def game_over():
    pass # 아무 일도 하지 않고 넘어감

game_start()
game_over()

# super : 부모 클래스 생성자 호출
# super를 통한 생성자 호출 시 self 생략 가능
# 명시적으로 생성자 호출 시 self 생략 불가능
# but 다중 상속일 경우 super 사용 금지, 기존 생성자 호출 방식
class Animal:
    def __init__(self):
        print("Animal 생성자")

class Flyable:
    def __init__(self):
        print("Flayable 생성자")

# 단일 상속시 super로 대체 가능
class Dog(Animal):
    def __init__(self):
        super().__init__()

nooleong2 = Dog()

# 다중 상속시 명시적으로 생성자 호출
class Eagle(Flyable, Animal):
    def __init__(self):
        Flyable.__init__(self)
        Animal.__init__(self)

hanhwa = Eagle()
    