# 외장함수 : import를 사용해서
# random : 난수를 만들 때 많이 사용 됨
import random
print(random.randint(1, 50))

# glob : 경로 내의 폴더 / 파일 목록 조회 (윈도우 dir)
import glob
print(glob.glob("*.py")) # 경로 내에 확장자가 .py 파일들 출력

# os : 운영체제에서 제공하는 기본 기능
import os
print(os.getcwd()) # 현재 디록토리 표시

# folder = "sample_dir"
# if os.path.exists(folder): # folder 변수명의 폴더가 있다면
#     print("이미 존재하는 폴더입니다.")
#     os.rmdir(folder) # 폴더 삭제
#     print(folder, "폴더를 삭제하였습니다.")
# else:
#     os.mkdir(folder) # 폴더 생성
#     print(folder, "폴더를 생성하였습니다.")

# time : 시간 관련 함수
import time
print(time.localtime())
print(time.strftime("%Y-%m-%d %H:%M:%S"))

# datetime : 날짜 시간 관련 함수
import datetime
print("오늘 날짜 : {0}".format(datetime.date.today()))

# timedelta : 두 날짜 사이의 간격
