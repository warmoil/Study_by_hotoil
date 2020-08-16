cabinet={3:"유재석",100:"김태호"}
print(cabinet)
print(cabinet[3])
print(cabinet[100])
#print(cabinet[5])  <<없는것은 오류
print(cabinet.get(5))#get()를사용하면 오류없이 출력
print(cabinet.get(5,"사용가능"))
print("hi")

print(3 in cabinet)  #키가 있는지 확인
print(4 in cabinet)
#키값으로 스트링도가능 
cabinet={"a-3":"유재석","b-100":"김태호"}
print(cabinet["a-3"])

#새 손님
print(cabinet)
cabinet["a-3"]="김종국"
cabinet["c-20"]="조세호"
print(cabinet)

# 간손님
del cabinet["a-3"]
print(cabinet.get("a-3"))

# key들만 출력
print(cabinet.keys())

#value 들만 출력
print(cabinet.values())

#key value 쌍으로 출력 
print(cabinet.items())

#목욕탕 폐점
cabinet.clear()
print(cabinet)