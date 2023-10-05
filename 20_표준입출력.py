# sep : , 를 원하는것으로 치환
# end : print 함수가 종료 될때 어떤식으로 마무리 할지
print("Python", "Java", "Javascript", sep=" vs ")

print("nooleong", end=" ")
print("2")

scores = {
    "영어": 3,
    "수학": 50,
    "국어": 100
}

# ljust(n) : n(자리수) 왼쪽 정렬
# rjust(n) : n(자리수) 오른쪽 정렬
for subject, score in scores.items():
    print(subject.ljust(6), str(score).rjust(4), sep=":")

# zfill(n) : n(자리수) 빈공간을 숫자 0 으로 채움
for num in range(1, 21):
    print("대기번호 : " + str(num).zfill(3))