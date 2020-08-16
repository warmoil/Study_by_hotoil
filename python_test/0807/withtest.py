# import pickle
#pickle 은 b를써야함
# with open("profile.pickle","rb") as profile_file:
#     print(pickle.load(profile_file)) #with는 클로즈 딱히 필요없음

# with open("study.txt","w",encoding="utf8") as study_file:
#     study_file.write("파이썬을 열실히 공부하고 있어요")

# with open("study.txt","r",encoding="utf8") as study_file:
#     print(study_file.read())

# with open("study.txt","w",encoding="utf8") as study_file:
#     study_file.write("열공중입니다.")    

with open("study.txt","r",encoding="utf8") as study_file:
    print(study_file.read())