# if else elif
# input <- 사용자 입력 받는 메소드
weather = input("오늘 날씨 어때요? ")
if (weather == "비") | (weather == "눈"):
    print("우산을 챙기세요.")
elif weather == "미세먼지":
    print("마스크 챙기세요.")
else:
    print("아무것도 안 챙겨도 됩니다.")

temp = int(input("오늘은 몇도 인가요? "))
if (30 <= temp):
    print("너무 더워요 나가지 마세요")
elif (10 <= temp) & (temp < 30):
    print("괜찮은 날씨 입니다.")
elif (0 <= temp) & (temp < 10):
    print("추워요 외투 챙기세요.")
else:
    print("나가면 못 돌아옵니다.")