



account_balance=int(input("enter your account balance: "))
withdrawal_amount=int(input("enter your withdrawal amount:"))
balance= abs(account_balance-withdrawal_amount)


if withdrawal_amount>0:
    print("welcome")
    if withdrawal_amount>account_balance:
        print("insufficient funds")
    if balance<=100000:
        print("warning, so close to insufficient funds")
    else:
        print(f"your account balance is {balance} toman")
else:
    print("error")
