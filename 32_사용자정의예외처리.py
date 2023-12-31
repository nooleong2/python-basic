class CustomExceptionError(Exception):
    def __init__(self, msg):
        self.msg = msg

    def __str__(self): # 문자열로 출력
        return self.msg
    
try:
    print("한 자리 숫자 나누기 전용 계산기")
    num1 = int(input("첫 번째 값을 입력하세요 >> "))
    num2 = int(input("두 번째 값을 입력하세요 >> "))

    if num1 >= 10 or num2 >= 10:
        raise CustomExceptionError("입력값 : {0}, {1}".format(num1, num2))

    print("{0} / {1} = {2}".format(num1, num2, int(num1 / num2)))

except CustomExceptionError as erm:
    print("잘못된 값을 입력하였습니다.")
    print(erm)

finally: # finally 정상적이든, 에러를 발생하던 무조건 실행되는 부분
    print("계산기를 이용해 주셔서 감사합니다.")

