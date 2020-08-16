# absent=[2,5] #결석
# no_book=[7] # 책을 깜빡했습니다
# for student in range(1,11): #1,2,3,4,5,...10
#     if student in absent:
#         continue
#     elif student in no_book:
#         print("오늘 수업 여기 까지 .{0}는 교무실로 따라와".format(student))
#         break
#     print("{0},책을 읽어봐".format(student))
students=[1,2,3,4,5]
print(students)
students=[i+100 for i in students]
print(students)

#학생 이름을 길이로 변환
# students =["Iron man","Thor","I am groot"]
# students=[len(i) for i in students]
# print(students)

# 학생 이름을 대문자로 변환
students =["Iron man","Thor","I am groot"]
students=[i.upper() for i in students]
print(students)