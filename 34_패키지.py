# 패키지 모듈을 모아두는 곳
# 사용 방법 module이랑 동일
from travel import thailand
thailand_trip_to = thailand.ThailandPackage() # 클래스 생성
thailand_trip_to.detail() # 클래스 내 메소드 호출

from travel import vietnam
vietnam_trip_to = vietnam.VietnamPackage() # 클래스 생성
vietnam_trip_to.detail() # 클래스 내 메소드 호출

# *을 쓰기위해서는 공개범위를 설정해줘야함
# __init__.py file 수정
from travel import *
trip_to_v = vietnam.VietnamPackage()
trip_to_v.detail()

trip_to_t = thailand.ThailandPackage()
trip_to_t.detail()


# 패키지 파일 위치 호출
import inspect
import random
print(inspect.getfile(vietnam))