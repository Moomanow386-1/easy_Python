# *args คือ การใช้ *args ในการรับ argument ที่ไม่จำกัดจำนวนในฟังก์ชัน ซึ่งจะถูกเก็บไว้ในรูปแบบของ tuple (แบบลำดับ)
# **kwargs คือ การใช้ **kwargs ในการรับ argument ที่ไม่จำกัดจำนวนในฟังก์ชัน ซึ่งจะถูกเก็บไว้ในรูปแบบของ dictionary โดยที่ key จะเป็นชื่อของ parameter และ value จะเป็นค่าที่เราส่งเข้าไปในฟังก์ชัน (แบบกำหนดชื่อ parameter)

def save_employee(*args): #tuple ที่เก็บ argument ที่ส่งเข้าไปในฟังก์ชัน save_employee

    print(f"Employee Name: {args[0]}") # args[0] คือ name
    print(f"Position: {args[1]}") # args[1] คือ position
    print(f"Salary: ${args[2]}") # args[2] คือ salary
    print(f"Address: {args[3]}") # args[3] คือ address
    print("-----------------------------")

save_employee("Bob", "Manager", 50000, "ภูเก็ต")
save_employee("Alice", "Developer",20000, "กรุงเทพฯ")
save_employee("Charlie", "Designer", 30000, "เชียงใหม่")


def save_employee(**kwargs): # dictionary ที่เก็บ argument ที่ส่งเข้าไปในฟังก์ชัน save_employee

    print(f"Employee Name: {kwargs['name']}") 
    print(f"Position: {kwargs['position']}") 
    print(f"Salary: ${kwargs['salary']}") 
    print(f"Address: {kwargs['address']}") 
    print("-----------------------------")

save_employee(name="Bob", position="Manager", address="ภูเก็ต", salary=50000) 
save_employee(name="Alice", position="Developer", salary=20000, address="กรุงเทพฯ")
save_employee(salary=30000, position="Designer", name="David", address="เชียงใหม่")