print("a" + "b")
print("a", "b")

# 방법 1
# %d == 정수
# %s == 문자
# %c == 한글자(charactor)
print("나는 %d살입니다." % 20)
print("나는 %s을좋아합니다." % "누렁이")
print("Apple은 %c로 시작합니다." % "A")

# but %s의 경우 모든걸 자동 문자로 치환
print("나는 %s살입니다." % 20)
print("Apple은 %s로 시작합니다." % "A")

# 2개 일 때
print("나는 %s와 %s색을 좋아합니다." % ("노랑", "파랑"))

# 방법 2
print("나는 {}살입니다.".format(20))
print("나는 {}와 {}색을 좋아합니다.".format("노랑", "파랑"))
print("나는 {0}와 {1}색을 좋아합니다.".format("노랑", "파랑")) # 뒤에 인자값 위치 변경 가능
print("나는 {1}와 {0}색을 좋아합니다.".format("노랑", "파랑")) # 뒤에 인자값 위치 변경 가능

# 방법 3
print("나는 {age}이며, {animal}를 좋아합니다.".format(age = 20, animal = "누렁이"))

# 방법 4 (v3.6 이상)
age = 20
animal = "누렁이"
print(f"나는 {age}살이며, {animal}을 좋아합니다.")