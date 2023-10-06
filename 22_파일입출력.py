score_file = open("score.txt", "w", encoding="utf8") # 파일명, 사용방식, 인코딩
print("수학 : 0", file=score_file) # 파일 내용, 텍스트 저장 파일 위치
print("영어 : 50", file=score_file)
score_file.close() # 항상 닫아 줄 것

score_file = open("score.txt", "a", encoding="utf8") # a -> 기존 파일에 추가해서 글 쓰기
score_file.write("과학 : 80\n") # write 함수 일 경우 줄바꿈 없기 때문에 항상 개행 문자 정의
score_file.write("코딩 : 100")

score_file = open("score.txt", "r", encoding="utf8") # r -> 파일 읽기
print(score_file.read()) # 한번에 다 읽기
score_file.close()

score_file = open("score.txt", "r", encoding="utf8")
print(score_file.readline(), end="") # 한줄 씩 출력 한줄 읽고 커서 아래 이동
print(score_file.readline(), end="")
print(score_file.readline(), end="")
print(score_file.readline(), end="")
score_file.close()

# 다른 방식으로 읽는 방법
score_file = open("score.txt", "r", encoding="utf8")
while True:
    line = score_file.readline()
    if not line:
        break
    print(line)
score_file.close()

score_file = open("score.txt", "r", encoding="utf8")
lines = score_file.readlines() # list 형태로 저장
for line in lines:
    print(line, end="")
score_file.close()