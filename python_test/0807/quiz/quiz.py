for i in range(1,51):
    with open("{0}weekend.txt".format(i),"w",encoding="utf8") as weekend_file:
        weekend_file.write("{0}주차보고 \n부서:\n이름:\n업무 요약:".format(i))  #==이거랑 아래는 같은역활을함
        #print(weekend_file.write("{0}주차보고 \n부서:\n이름:\n업무 요약:".format(i)))
print(weekend_file)
print(len("10주차보고 \n부서:\n이름:\n업무 요약:"))
