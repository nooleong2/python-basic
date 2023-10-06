# pickle : 프로그램 상에서 우리가 사용하는 데이터를 파일 형태로 저장해주는 역활
import pickle

# 픽클 쓰기
profile_file = open("profile.pickle", "wb", ) # wb -> 쓰기 형태 바이너리 타입 (픽클에서는 꼭 사용)
profile = {
    "이름" : "누렁이",
    "나이" : 2,
    "취미" : [
        "축구", "골프", "코딩"
    ]
}

print(profile)
pickle.dump(profile, profile_file) # profile에 있는 정보를 file에 저장
profile_file.close()

# 픽클 읽기
profile_file = open("profile.pickle", "rb")
profile = pickle.load(profile_file) # 파일정보를 profile에 불러오기
print(profile)
profile_file.close()

