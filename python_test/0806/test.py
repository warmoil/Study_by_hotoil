for i in range(2,10):
    for j in range(2,10):
        print(str(j)+"*"+str(i)+"=",end='')
        if(i*j<10):
            print(" ",end="")
        print(str(i*j)+" ",end='')
    print()