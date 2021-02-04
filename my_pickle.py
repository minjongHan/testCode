import pickle
#프로그램 상에서 사용하는 데이터를 파일 형태로 저장하는것
profile_file = open("profile.pickle", "wb") #b는 바이너리를 의미
profile = {"이름" : "박명수", "나이":30, "취미" : ["축구", "골프", "코딩"]}
print(profile)
#pickle로 파일에 데이터 쓰기
pickle.dump(profile, profile_file) #profile에 있는 정보를 file에 저장
profile_file.close()

profile_file = open("profile.pickle", "rb")
profile_r = pickle.load(profile_file) # 파일에 있는 정보를  profile에 불러오기
print(profile_r)
profile_file.close()