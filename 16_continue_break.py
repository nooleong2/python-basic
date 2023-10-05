absent = [2, 5] # 결석
no_book = [7] # 책 없음
for student in range(1, 11):
    if student in absent:
        continue
    elif student in no_book:
        print(f"오늘 수업 종료 {student}번은 교무실로 따라와")
        break
    print(f"{student}, 책 읽어봐")