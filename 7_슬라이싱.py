jumin = "990120-1234567"
# index == 문자 길이의 현재 위치 번호
print("성별 : " + jumin[7]) # index는 0부터 시작
print("년도 : " + jumin[0:2]) # index 2 전 까지 (2미포함)
print("월 : " + jumin[2:4])
print("일 : " + jumin[4:6])
print("생년월일 : " + jumin[:6]) # 처음부터 6 직전 까지
print("뒤 7자리 : " + jumin[7:]) # 7부터 끝까지
print("뒤 7자리 (뒤에서부터) : " + jumin[-7:]) # 맨 뒤에서 7번째 부터 끝까지 뒤에서는 -1부터 시작
