

# def std_weight(height,gender):
#     if gender=="m":
#         swight=height*height*22
#         print("남자기준:{0}kg입니다".format(round(swight,2)))
#     elif gender=="w":
#         swight=height*height*21
#         print("여자 기준으로는{0}kg입니다".format(round(swight,2)))
#     return round(swight,2)

# a=std_weight(1.75,"m")
# b=std_weight(1.6,"w")
# print(a)
# print(b)

def std_weight (height,gender):#키는 m단위 (실수) 
    if gender=="남자":
        return height * height *22
    else:
            return height *height *21

height=175
gender="남자"
weght=std_weight(height/100,gender)
print("키 {0}cm{1}의 표준 체중은 {2}kg입니다.".format(height,gender,round(weght,2)))