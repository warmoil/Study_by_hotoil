#집합(set)
#중복 안됨,순서 없음
my_set={1,2,3,4,4}
print(my_set)

java={"유재석","김태호","양세형"}
python={"유재석","박명수"}

#교집합 (java 와 python 모두 할수있는 사람)
print(java & python)
print(java.intersection(python))

# 합집합 (java를 할수있거나 python을 할수있는 사람)
print(java|python)
print(java.union(python))

#차집합(java는 할수있지만 python은 할줄모르는 개발자)
print(java-python)
print(java.difference(python))