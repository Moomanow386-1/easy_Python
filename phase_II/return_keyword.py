balance = 1000 #global variable to store the balance

def display_balance():
    print(f"Your current balance is: {balance:.2f} บาท")

def deposit(value):
    money = value #local variable to store the deposit amount
    global balance #ใช้ global variable balance เพื่อให้สามารถแก้ไขค่าได้

    if money <= 0:
        print("ไม่สามารถฝากเงินได้")
        return 
    else:
        print("ฝากเงินจำนวน: ", money)
        balance += money

def withdraw(value):
    #local variable to store the withdrawal amount
    global balance #ใช้ global variable balance เพื่อให้สามารถแก้ไขค่าได้

    if value <= 0:
        print("ไม่สามารถถอนเงินได้")
        return
    elif value > balance:
        print("ยอดเงินในบัญชีไม่เพียงพอสำหรับการถอน")
        return
    else:
        print("ถอนเงินจำนวน: ", value)
        balance -= value

display_balance()
deposit(500)
display_balance()
withdraw(1500)
display_balance()