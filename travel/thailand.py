# 클래스 생성
class ThailandPackage:
    def detail(self):
        print("태국 3박 5일 코끼리 여행 50만원")

# 패키지 모듈 직접 실행
if __name__ == "__main__":
    print("Thailand 모듈을 직접 실행")
    print("이 문장은 모듈을 직접 실행할 때만 실행됩니다.")
    trip_to = ThailandPackage()
    trip_to.detail()

else:
    print("Thailand 외부에서 모듈 호출")