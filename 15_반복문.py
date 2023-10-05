# # 반복문 for
for waiting_no in range(1, 6):
    print("대기번호 : {0}".format(waiting_no))

# # 한 줄 for 문
dogs = ["yello", "red", "blue"]
dogs = [i.upper() + " DOG" for i in dogs]
print(dogs)

# # 구구단
for i in range(2, 10):
    for j in range(1, 10):
        print(f"{i} x {j} = {i * j}")
    print("")

# # 반복문 while
customer = "누렁이"
index = 5
while index >= 1:
    print(f"{customer}님 커피 나왔습니다. 총 남은 횟 수 : {index}")
    index -= 1

    if index == 0:
        print("커피는 폐기처분 되었습니다.")