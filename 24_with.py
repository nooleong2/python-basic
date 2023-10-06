import pickle

# with as 간편하게 파일을 읽고 쓰는 기능
# 장점 close를 따로 안해줘도 됨

with open("profile.pickle", "rb") as profile_file: # open으로 열어러 profile_file변수에 저장 한 후
    print(pickle.load(profile_file)) # pickle을 이용해 출력 함

# pickle 없이 with as 사용
with open("study.txt", "w", encoding="utf8") as study_file:
    study_file.write("파이썬을 열심히 공부하고 있어요")

with open("study.txt", "r", encoding="utf8") as study_file:
    print(study_file.read())

