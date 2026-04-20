def save_employee(name, position, salary = 25000):
    print(f"Employee Name: {name}")
    print(f"Position: {position}")
    print(f"Salary: ${salary}")
    print("-----------------------------")

save_employee("Bob", "Manager", 50000)
save_employee("Alice", "Developer") # salary จะใช้ค่า default คือ 25000 เพราะเราไม่ได้ส่ง argument สำหรับ salary เมื่อเรียกใช้งานฟังก์ชัน save_employee