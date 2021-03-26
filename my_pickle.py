import pickle
# pickle란 프로그램 상에서 사용하는 데이터를 파일 형태로 저장하는것
profile_file = open("profile.pickle", "wb") #b는 바이너리를 의미,  w는 파일을 쓰겠다는 의미
profile = {"이름" : "박명수", "나이":30, "취미" : ["축구", "골프", "코딩"]}
print(profile)

#pickle로 파일에 데이터 쓰기
pickle.dump(profile, profile_file) #profile에 있는 정보를 profile_file에 저장함  pickle.dump는 pickle로 파일에 저장
profile_file.close()


#저장된 파일을 읽어 오기
profile_file = open("profile.pickle", "rb")  # r은 파이을 읽음 b로 적어 바이러리라는것을 명시해줌
profile_r = pickle.load(profile_file) # profile_file에 파일에 있는 정보를  profile_r에 불러오기
print(profile_r)
profile_file.close()