#if
wather=input("오늘 날씨는 어때요?")
if wather=="비"or "눈":
    print("우산을 챙기세요")
elif wather =="미세먼지":
    print("마스크를 챙기세요")
else:
    print("준비물 필요 없어요.")

temp=int(input("기온은 어때요?"))
if 30 <= temp:
    print("너무 더워요 삼겹살을 드세요")
elif 10<=temp and temp<30:
    print("괜찮은 날씨네요 삼결살을 드세요")
else:
    print("너무추워요 막걸리를 드세요")