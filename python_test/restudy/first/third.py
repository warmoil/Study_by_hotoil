# weather=input("오늘 날씨는 어때요?")

# if weather =="비"or"눈":
#     print("우산을 챙기세요")
# elif weather =="미세먼지":
#     print("마스크를 챙기세요")
# else:
#     print("준비물은 필요없어요")

# temp=int(input("기온은 어때요?"))
# if temp>=30:
#     print("더우니 나가지마세요")

# elif temp >=10 and temp <30:
#     print("괜찮은 날씨네요")

# elif 0<= temp and temp <10:
#     print("추워요 외투를 챙기세요")
# else:
#     print("너무 추워요 막걸리를 챙기세요")

# print("대기번호:1")
# print("대기번호:2")
# print("대기번호:3")
# print("대기번호:4")

# for waiting_no in range(1,5):
#     print("대기번호:{0}".format(waiting_no+1))


# i =list(range(1,6))
# print(i)

# starbobs=["아이언맨","토르","아이엠 그루트"]

# for customer in starbobs:
#     print("{0},밥 다됐다".format(customer))

# customer="토르"
# index =5
# while index>=1:
#     print("{0},커피가 준비되었습니다.{1}번 남았어요".format(customer,index))
#     index-=1
# if index==0:
#     print("{0}님의 커피가 폐기되었습니다".format(customer))


# customer="토르"
# person="왓"
# while person != customer:
#     print("{0},커피가 준비되었습니다.".format(customer))
#     person=input("이름이?")
# if person=="토르":
#     print("왤케 오래걸렸냐?")


# run=[2,13]
# no_book=[7]
# for student in range(1,21):
#     if student in run:
#         continue
   
#     elif student in no_book:
#         print("{0}너는 안돼겠다 따라와".format(student))
#         break

#     print("{0},책을 읽어보게".format(student))

# 출석 번호 1,2,3,4 앞에 100을 붙이기로함 -->101,102,103,104
# student=[1,2,3,4,5]
# student=[i+100 for i in student]
# print(student)

#학생 이름을 길이로 변환
# students=["Iron man","Thor","I am groot"]
# students=[len(i) for i in students]
# print(students)

#학생이름을 대문자로

# students=["Iron man","Thor","I am groot"]
# students=[i.upper() for i in students]
# print(students)

#from random import *

# cnt=0
# for i in range(1,51):
#     call=randint(5,51)
#     if call<=15:
#         print("[O]{0}번째손님 (소요시간:{1}분".format(i,call))
#         cnt+=1
#     else:
#         print("[ ]{0}번째손님 (소요시간:{1}분".format(i,call))
# print(f"총 탑승 승객:{cnt}분")

from random import *

#로또로 인생 역전하자
for i in range(1,6):
    lotto=list(range(1,46))
    shuffle(lotto)
    print(sample(lotto,6))

    cnt_1="qq"
    i=1
    print(cnt_i)