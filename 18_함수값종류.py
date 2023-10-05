# 기본 값 : 값을 넣지 않으면 자동으로 들어감
def profile_default(name, age = 4, type = "강아지"):
    print(f"My name is {name} I'm {age} years old, My type is {type}")

profile_default("누렁이")
profile_default("백구")

# 키워드 값 : 순서와 상관없이 키워드 값으로 해당 값에 들어감
def profile_keyword(name, age, type):
    print(name, age, type)

profile_keyword(name = "누렁이", age = 2, type ="강아지")
profile_keyword(age = 2, type ="강아지", name = "누렁이")

# 가변 인자 값
def profile_arguments(name, age, *langs):
    print(f"이름: {name}, 나이: {age}", end=" ") # end --> print함수가 종료될 때 개행이 아니라 띄어쓰기로 변경한다는 뜻
    for lang in langs:
        print(lang, end=" ")
    print()

profile_arguments("누렁이", 2, "java", "python", "c")
profile_arguments("백구", 2, "linux")