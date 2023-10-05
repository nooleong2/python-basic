# dictionary {} : key = 중복 불가능, value =  중복 가능
cabinet = {
    3: "누렁이",
    100: "청구",
    "A-1": "빡구"
}

# value 값 가져오기
print(cabinet[3])
print(cabinet[100])
print(cabinet.get(3))

# but []의 경우 값이 없으면 error를 던지지만 get()의 경우 None을 반환한다
print(cabinet.get(5))
print(cabinet.get(5, "사용 가능")) # 5의 키 값의 없으면 2번째 인자의 값을 반환
print("get() ... ing") # 실행 계속 됨

# print(cabinet[5])
# print('[] ...ing') # 실행 되지 않음

# 해당 변수(딕셔너리)의 key가 있는지 (숫자, 문자 가능)
print(100 in cabinet) # True
print("A-1" in cabinet) # True

# 딕셔너리 키:밸류 추가
cabinet["A-4"] = "백구"
print(cabinet)
# 딕셔너리 키:밸류 삭제
del cabinet["A-4"]
print(cabinet)

# 키 들만 출력
print(cabinet.keys())
# 밸류 들만 출력
print(cabinet.values())
# 키, 밸류들 출력
print(cabinet.items())

# 딕셔너리 삭제
cabinet.clear()
print(cabinet)
