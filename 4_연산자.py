# 연산자
print(1 + 1) # 더하기
print(3 - 2) # 빼기
print(5 * 2) # 곱하기
print(6 / 3) # 나누기

print(2 ** 3) # 2의 3승 2^3 = 8
print(5 % 3) # 나머지 = 2
print(20 / 5)# 몫 = 4

# 비교 연산
print(10 > 3) # 크다
print(4 >= 7) # 크거나 같다
print(10 < 3) # 작다
print(5 <= 5) # 작거나 크다
print(3 == 3) # 똑같다 : True, 똑같지 않다 : False
print(3 != 2) # 똑같지 않다 : True , 똑같다 : False
print(3 + 4 == 7) # True

# not 반대
print(not(1 != 3)) # 괄호 제일 안에거 부터 하나씩 1과 3은 같지 않다 True 하지만 not이 존재하기 때문애 True의 반대 False 출력

# and(&), or(|) 
# & : 앞뒤 조건이 모두 참이면 True, 하나라도 거짓이면 False
# | : 앞뒤 조건 중 하나라도 True면 True, 두개다 거짓이면 False
print(1 == 1 and 2 == 2) # true
print(1 == 1 and 2 == 1) # false
print(1 == 2 & 2 == 3) # false
print(1 == 1 or 3 == 1) # true
print(3 == 2 or 5 == 5) # true
print(5 == 4 | 3 == 2) # false