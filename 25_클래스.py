# 클래스 생성
class Unit:
    def __init__(self, name, hp, damage): # __init__ : 셍성자
        self.name = name # self.?? : 멤버 변수 : 클래스네에서 정의된 변수
        self.hp = hp
        self.damage = damage
        print("{0} 유닛이 생성 되었습니다.".format(self.name))
        print("체력 {0}, 공격력 {1}".format(self.hp, self.damage))

# 클래스로 부터 만들어지는 것을 객체라고 표현 함
marine1 = Unit("마린", 40, 5)
marine2 = Unit("마린", 40, 5)
tank1 = Unit("탱크", 150, 35)

# 외부에서 멤버변수 사용하기
wraith1 = Unit("레이스", 80, 5)
print("{0}의 공격력은 {1} 입니다.".format(wraith1.name, wraith1.damage)) # wraith1.name, damage : 멤버 변수 사용

# 외부에서 변수 추가 할당
# but 해당 객체에만 추가 됨 같은 객체여도 다른객체에는 추가 할당 되지 않음
wraith2 = Unit("빼앗은 레이스", 80, 5)
wraith2.clocking = True # 변수 추가

if wraith2.clocking == True:
    print("{0}는 현재 투명상탱 입니다.".format(wraith2.name))
