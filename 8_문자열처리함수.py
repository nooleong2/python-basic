python = "Python is Amazing"
print(python.lower()) # 소문자
print(python.upper()) # 대문자
print(python[0].isupper()) # 대문자인지 확인
print(python[0].islower()) # 소문자인지 확인
print(len(python)) # 문자 전체 길이
print(python.replace("Python", "Java")) # 대소문자 모두 동일해야됨

index = python.index("n") # n문자의 index 위치 값
print(index) # 5
index = python.index("n", index + 1) # 두번째 인자는 찾는 시작 위치
print(index) # 15

print(python.find("n")) # index 함수랑 동일 하지만 find 함수는 반환값을 -1을 던져줌 :: index 함수의 경우 error를 반환 함
print(python.count("n")) # 해당 문자열에서 n이라는 글자가 얼마나 나오는지 수를 반환