python="Python is Amazing"
print(python.lower())
print(python.upper())
print(python[0].isupper())
print(len(python))
print(python.replace("Python","java"))

index=python.index("n")#몇번째에 n이있나
print(index)
index=python.index("n",index + 1)#그 n다음엔은어디인가
print(index)

print(python.find("Java"))#그값이없으면 -1을 반환
#print(python.index("Java")) 그값이없으면 오류를 반환하며 종료
print(python.replace("Amazing","very Amaing"))

print(python.count("n"))