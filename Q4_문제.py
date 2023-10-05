# Quiz) 당신의 학교에서는 파이썬 코딩 대회를 주최합니다.
# 참석률을 높이기 위해 댓글 이벤트를 진행하기로 했습니다.
# 댓글 작성자들 중에 추첨을 통해 1명은 치킨, 3명은 커피 쿠폰을 받게 됩니다.
# 추첨 프로그램을 작성하시오.

# 조건1 : 편의상 댓글은 20명이 작성하였고 아이디는 1 ~ 20 이라고 가정
# 조건2 : 댓글 내용과 상관 없이 무작위로 추첨하되 중복 불가
# 조건3 : random 모듈의 shuffle 과 sample을 활용

# (출력 예제)
# -- 당첨자 발표 --
# 치킨 당첨자 : x
# 커피 당첨자 : [x, y, z]
# -- 축하합니다 --

# (활용 예제)
from random import *
lst = [1, 2, 3, 4, 5]
print(lst)
shuffle(lst) # 무작위 섞기
print(lst)
print(sample(lst, 1)) # 2번째 인자 : 뽑을 개수

ids = range(1, 21) # 1 ~ 21 직전까지 숫자 생성
ids = list(ids) # range의 경우 type이 range이기 때문에 list로 변경
shuffle(ids)
winners = sample(ids, 4)
chicken = winners[0]
coffee = winners[1:]

print("-- 당첨자 발표 --")
print("치킨 당첨자 : {}".format(chicken))
print("치킨 당첨자 : {}".format(coffee))
print("-- 축하합니다 --")