# 함수 생성
def deposit(balance, money):
    balance += money
    print(f"{money}를 입금하였습니다. 현재 총 금액 : {balance}원입니다.")
    return balance

def withdraw(balance, money):
    if balance < money:
        print(f"잔액이 부족합니다. 현재 총 잔액 : {balance}원 입니다.")
    else:
        balance -= money
        print(f"출금 금액은 : {money}원이며, 총 남은 잔액은 : {balance}원 입니다.")
        return balance
    
def withdraw_night(balance, money):
    commission = 100
    return commission, balance - money - commission # 리턴이 두개일 때 튜플 형식으로 전달 함
    
balance = 0
balance = deposit(balance, 1000)
balance = withdraw(balance, 300)

commission, balance = withdraw_night(balance, 500) # 튜플 형식으로 받음
print(f"수수료 {commission}원 이며, 잔액은 {balance}원 입니다.")
print(type(commission))
print(type(balance))