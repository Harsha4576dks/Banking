def banking():
    print("welcome to HM banking")
    print("1:add money")
    print("2:withdraw money")
    print("3:check balance")
    amount = int(input("enter your choice:"))
    balance =  1000
    while True:
        if amount == 1:
            money = int(input("enter the amount to be added:"))
            balance = balance + money
            print(f"your current balance is: {balance}")
            amount = int(input("enter your choice:"))

        elif amount == 2:
            money = int(input("enter the amount to be withdrawn:"))
            if money > balance:
                print("insuffienct money")
            else:
                balance = balance - money
                print(f"your current balance is: {balance}")
            amount = int(input("enter your choice:"))

        elif amount == 3:
            print(f"your current balance is: {balance}")
            amount = int(input("enter your choice:"))

        else:
            print("invalid choice")
            exit()

banking()
