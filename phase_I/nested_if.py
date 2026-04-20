#Bank
username = input("Username: ")
password = input("Password: ")

if username == "admin" and password == "1234":
    print("ยินดีต้อนรับเข้าสู่ระบบธนาคาร")
    num = int(input("กรุณาป้อนหมายเลขบริการที่ต้องการใช้ (1: ถอนเงิน, 2: ฝากเงิน) : "))
    if num == 1:
        print("ถอนเงิน")
    elif num == 2:
        print("ฝากเงิน")
    else:
        print("หมายเลขบริการไม่ถูกต้อง")    
else:
    print("ไม่พบบัญชี")