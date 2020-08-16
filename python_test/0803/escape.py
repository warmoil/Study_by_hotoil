#\n탈출문자
print("백문이 불여일견 \n백견이 불여일타")
#저는 "JOY"입니다
print("저는 'JOY'입니다 ")
print('저는 "JOY"입니다')
print("저는  \"JOY\" 입니다")
print("저는 \'JOY\'입니다 ")
#\\:문장 내에서\
print("C:\\User\\JOY\\Desktop\\")
#\r:커서를 맨 앞으로 이동
print("Red Apple\rPine")

#\b:백스페잇그(한 글자 삭제)
print("redd\bApple")
#\t:탭 
print("Red\tApple")

url="http://naver.com"
my_str=url.replace("http://","")
my_str=my_str[0:my_str.find(".")]
first=my_str[0:3]
secon=len(my_str)
third=my_str.count("e")
password=first+str(secon)+str(third)+"!"
print("비번은"+password)
