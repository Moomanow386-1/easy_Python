balance = 1000 #global variable to store the balance

def display_balance():
    print(f"Your current balance is: {balance:.2f} บาท")

def deposit(value):
    money = value #local variable to store the deposit amount
    global balance #ใช้ global variable balance เพื่อให้สามารถแก้ไขค่าได้
    print("ฝากเวินจำนวน: ", money)
    balance += money 

def withdraw(value):
    #local variable to store the withdrawal amount
    global balance #ใช้ global variable balance เพื่อให้สามารถแก้ไขค่าได้
    print("ถอนเงินจำนวน: ", value)
    balance -= value

display_balance()
deposit(500)
display_balance()
withdraw(200)
display_balance()