
def insertcoin(money):
    
    fman=int(money/50000)
    man=(money%50000)/10000
    a=(money%50000)%10000
    fchun=a/5000
    a=a%5000
    chun=a/1000
    a=a%1000
    fbak=a/500
    a=a%500
    bak=a/100
    a=a%100
    fsib=a/50
    a=a%50
    sib=a/10
    fi=a/5
    il=a%5
    print("5만원:{0}장\n 1만원:{1}장 \n5천원:{2}장 천원:{3}장 5백원:{4}장".format(fman,man,fchun,chun,fbak))
    print("백원:{0}장\n50원:{1}장\n10원:{2}장\n5원{3}장\n1원{4}장".format(bak,fsib,sib,fi,il))

insertcoin(int(input("얼마나있나?")))

