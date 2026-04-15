#username = input("Enter your username: ")
#password = input("Enter your password: ")

#if not username == "admin" or not password == "1234": #ถ้า username ไม่ใช่ admin หรือ password ไม่ใช่ 1234 จะเข้าสู่เงื่อนไขนี้
    #print("Welcome, admin!")
#else :
    #print("Invalid username or password.")

#โปรแกรมตัดเกรด
score = int(input("กรุณากรอกคะแนนของคุณ : "))
print("คะแนนของคุณคือ = ",score)
if 100 >= score >= 80:
    print("คุณได้เกรด A")
elif 79 >= score >= 70:
    print("คุณได้เกรด B")
elif 69 >= score >= 0:
    print("คุณได้เกรด F")
else:
    print("N (Invalid score)")
    

