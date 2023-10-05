# 전역 변수 : 코드 전체에서 사용하는 변수
# 지역 변수 : 함수 안에서 사용하는 변수

gun = 10

def check_point(soliders):
    global gun # 전역 변수 사용
    gun -= soliders
    print("[함수 내] 남은 총 : {0}".format(gun))

def checkpoint(gun, soliders):
    gun -= soliders # gun 지역 변수 사용
    print("[함수 내] 남은 총 : {0}".format(gun))

print("전체 총 : {0}".format(gun))

# 전역변수 사용 함수
check_point(2) # 경계근무 2명 출동
print("남은 총 : {0}".format(gun))

# 지역변수 사용 함수
checkpoint(5, 2) # 경계근무 2명 출동
print("남은 총 : {0}".format(gun)) # 여기서 남은 총으 위에 전역변수에서 사용됬던 값으로 출력 됨