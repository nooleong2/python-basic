print(abs(-5)) # 절대값
print(pow(4, 2)) # 제곱(4^2)
print(max(5, 12)) # 최대값
print(min(5, 12)) # 최소값
print(round(3.14)) # 반올림 : 3
print(round(3.99)) # 반올림 : 4

# math library를 이용한 숫자 함수
from math import *
print(floor(4.99)) # 내림 : 4
print(ceil(3.14)) #  올림 : 4 ceil 경우 소숫점이 존재한다면 무조건 올림
print(sqrt(25)) # 제곱근 : 25는 몇의 제곱근 인지

# 난수 랜덤 난수
from random import *
print(random()) # 0.0 ~ 1.0 미만의 난수 발생
print(random() * 10)  # 0.0 ~ 10.0 미만의 난수 발생
print(int(random() * 10)) # 0 ~ 10 미만의 난수 발생
print(int(random() * 10) + 1) # 1 ~ 10 미만의 난수 발생
print(randrange(1, 46)) # 1 ~ 46 미만의 난수 발생 46미포함
print(randint(1, 45)) # 1 ~ 45 까지의 난수 발생