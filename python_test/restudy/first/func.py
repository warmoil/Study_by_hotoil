def open_account():
    print("계좌가 생성되었습니다")

open_account()

def deposit(balance,money):
    print("{1}원이 입금이 완료되엇습니다. 잔액은{0}원입니다".format(balance+money,money))
    return balance+money


def withdraw(balance,money):#출금
    if(balance>=money):
        print("{0}원 출금이 완료되었습니다. 잔액은{1}원입니다."\
        .format(money,balance-money))
        return balance-money
    else:
        print("돈이없어 출금이안됩니다.잔액은{0}원입니다".format(balance))
        return balance

balance=deposit(1000,1200)

balance=withdraw(balance,1040)


balance=withdraw(balance,1040)

