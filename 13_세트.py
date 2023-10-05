# 세트 {} : 집합 = 중복 X, 순서 X
java = {"누렁이", "흑구", "백구"}
python = ["청구", "누렁이"]
python = set(python) # type이 다르기때문에 맞춰 줌

# 교집합 (자바, 파이썬 모두 할 수 있는 강아지)
print(java & python)
print(java.intersection(python))

# 합집합 (자바 할 수 있거나, 파이썬 할 수 있는 강아지)
print(java | python)
print(java.union(python))

# 차집합 (자바는 할 수 있지만 파이썬은 할 줄 모르는 강아지)
print(java - python)
print(java.difference(python))
