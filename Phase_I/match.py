#Bank
username = input("Username: ")
password = input("Password: ")

if username == "admin" and password == "1234":
    print("ยินดีต้อนรับเข้าสู่ระบบธนาคาร")
    service = input("กรุณาป้อนหมายเลขบริการที่ต้องการใช้ (1: ถอนเงิน, 2: ฝากเงิน) : ")
    match service:
        case "1":
            print("ถอนเงิน")
        case "2":
            print("ฝากเงิน")
        case "":
            print("หมายเลขบริการไม่ถูกต้อง")    
else:
    print("ไม่พบบัญชี")