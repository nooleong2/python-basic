# 리스트 [] : 연속적인것을 하나로 묶음
dogs = ["백구", "누렁이", "흑구"]
print(dogs)

# 누렁이의 현재 위치
print(dogs.index("누렁이"))

# 점박이 추가
dogs.append("점박이") # append : 맨 뒤에 추가
print(dogs)

# 청구 추가
dogs.insert(1, "청구") # insert : 1번째 인자 값의 경우 넣고 싶은 위치(index)
print(dogs)

# 리스트 맨 뒤에서 하나씩 삭제
dogs.pop()
print(dogs)

# 이름이 같은 강아지 몇개 인지
print(dogs.count("누렁이"))

# 정렬
num_list = [3, 5, 1, 4, 2]
num_list.sort()
print(num_list)
# 순서 거꾸로
num_list.reverse()
print(num_list)
# 값 모두 삭제
num_list.clear()
print(num_list)

# 다양한 자료형 함께 사용 가능
mix_list = ["nooleong", 2, True]
print(mix_list)
# 리스트 확장
mix_list1 = [1, 2, 3]
mix_list2 = ["nooleong2", True]
mix_list1.extend(mix_list2)
print(mix_list1)