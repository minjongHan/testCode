import pickle

#with를 쓰면 파일을 알아서 별도로 닫아주지 않아도 됨
with open("profile.pickle", "rb") as profile_file:      # 파일을 열고 profile_file에 저장
    print(pickle.load(profile_file))                    # pickle.load로 파일을 출력해줌

#파일을 쓰기
with open("stude.txt", "w", encoding="utf-8") as study_file:        # w는 파일을 씀
    study_file.write("파이썬을 열심히 공부하고 있어요")     #파일에 내용을 적음

#쓴 파일을 읽기
with open("stude.txt", "r", encoding="utf-8") as study_file:
    print(study_file.read())            #파일을 읽어서 프린트
