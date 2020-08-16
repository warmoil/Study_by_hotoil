# jumin="990120-1234567"

# print("성별:"+jumin[7])
# print("연:"+jumin[0:2])#0번째부터 2직전까지
# print("월:"+jumin[2:4])
# print("일:"+jumin[4:6])
# print("생년월일:"+jumin[:6])
# print("뒤 7자리:"+jumin[7:])


# python="Python is Amaing"
# print(python.lower())
# print(python.upper())
# print(python[0].isupper())
# print(len(python))
# print("zllls".upper())
# print("python"[0].isupper())
# print(python.replace("Python","Java"))

url="http://naver.com"
n=url.find("/")
url=url[n+2:]
n=url.find(".")
url=url[:n]
print("{0}{1}{2}!".format(url[0:3],len(url),url.count("e")))