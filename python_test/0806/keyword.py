#키워드 값 순선가 뒤죽박죽이어도 가능함
# def profile(name,age,main_lang):
#     print(name,age,main_lang)

# profile(name="유재석",main_lang="파이썬",age=20)
# profile(main_lang="자바",age=25,name="김태호")

#가변인자
#def profile(name,age,lang1,lang2,lang3,lang4,lagn5):
#   print("이름:{0} \t나이:{1}\t".format(name,age),end=" ")
#   print(lang1,lang2,lang3,lang4,lang5)
def profile(name,age,*language):
    print("이름:{0} \t나이:{1}\t".format(name,age),end=" ")
    for lang in language:
            print(lang,end=" ")
    print()

profile("유재석",20,"python","java","c","c++","c#","javaScript")
profile("김태호",25,"kotlin","swift","","","")