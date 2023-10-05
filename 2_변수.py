# 변수 Variable
animal = "강아지"
name = "누렁이"
age = 4
hobby = "산책"
is_adult = age >= 3

# ex : 애완동물 소개해 주세요~
print("우리집 강아지의 이름은 누렁이입니다")
print("누렁이는 4살이며, 산책을 아주 좋아합니다.")
print("누렁이는 어른일까요? True")

# 변수를 이용한 애완동물 소개
print("우리집" +  animal + "의 이름은 " + name + "입니다")
print(name + "는 " + str(age) + "살이며," + hobby + "을 아주 좋아합니다.")
print(name + "는 어른일까요? " + str(is_adult))

# + 가 아닌 ,로 표시 문자열 연결 가능
# 단, 를 이용할 시 뛰어쓰기 하나 포함
print(name, "는 ", age, "살이며,", hobby, "을 아주 좋아합니다.")
