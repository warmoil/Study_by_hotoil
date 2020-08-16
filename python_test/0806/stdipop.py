#표준 입출력
# import sys 
# print("python","java","javascript",sep=",",end="?")
#sep=""  <콤마안에 무엇을 넣을까
# print("무엇이 더 재밌을까요?")
# print("python","java",file=sys.stdout)
# print("python","java",file=sys.stderr)
 
# scores={"수학":0,"영어":50,"코딩":100}#key와 value
# for subject,score in scores.items():
#     #print(subject,score)
#     print(subject.ljust(8),str(score).rjust(4),sep=":")


#은행 대기순번표
# 001 , 002 ,003 ....
# for num in range(1,21):
#     print("대기번호:"+str(num).zfill(3)) #3자리를 확보하는데 남는공간은 0으로 채워라

answer=input("아무 값이나 입력하세요:")
print("입력하신 값은"+answer+"입니다")
print(type(answer))