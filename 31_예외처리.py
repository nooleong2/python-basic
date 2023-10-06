# 예외 처리
# 나누기 계산기
try:
    nums = []
    nums.append(int(input("첫번째 값을 적어주세요 >> ")))
    nums.append(int(input("두번째 값을 적어주세요 >> ")))
    nums.append(nums[0] / nums[1])
    print("{0} / {1} = {2}".format(nums[0], nums[1], nums[2]))

except ValueError: # 한글로 값을 넣었을 때 나는 에러 직접 에러를 찾아서 명시적으로 예외처리 하는 방법
    print("에러! 잘못된 값을 입력하였습니다.")

except Exception as e: # 모든 에러를 다 받을 수 있음
    print(e)


# 예외 발생시키기
# 한자리 수 나누기 계산기
try:
    num1 = int(input("첫번째 값을 적어주세요 >> "))
    num2 = int(input("첫번째 값을 적어주세요 >> "))

    # 만약 2자리 값이 들어온다면 에러 발생 시키기
    if num1 >= 10 or num2 >= 10:
        raise ValueError # raise -> 에러 발생

    print("{0} / {1} = {2}".format(num1, num2, int(num1 / num2)))

except ValueError: # 발생 된 에러 받아서 처리
    print("한자리 수 이상은 값을 입력 할 수 없습니다")
