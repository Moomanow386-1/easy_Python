# parameter คือ ตัวแปรที่ใช้ในการส่งข้อมูลเข้าไปในฟังก์ชัน เพื่อให้ฟังก์ชันสามารถทำงานได้ตามที่เราต้องการ โดย parameter จะถูกกำหนดไว้ในวงเล็บหลังชื่อฟังก์ชัน และสามารถมีหลายตัวแปรได้ โดยแต่ละตัวแปรจะถูกคั่นด้วยเครื่องหมายจุลภาค (,)

# argument คือ ค่าที่เราส่งเข้าไปในฟังก์ชันเมื่อเราเรียกใช้งานฟังก์ชันนั้นๆ โดย argument จะถูกส่งเข้าไปในตำแหน่งที่ตรงกับ parameter ที่กำหนดไว้ในฟังก์ชัน

def say_hello(name,age): # name และ age คือ parameter เพราะมันเป็นตัวแปรที่ใช้ในการรับค่าจาก argument ที่เราส่งเข้าไปเมื่อเรียกใช้งานฟังก์ชัน
    print(f"Hello, {name}!")
    print(f"You are {age} years old.")

def save_employee(name, position, salary):
    print(f"Employee Name: {name}")
    print(f"Position: {position}")
    print(f"Salary: ${salary}")

save_employee("Bob", "Manager", 50000)

def show_table(num):
    for i in range(1, 13):
        print(f"{num} x {i} = {num * i}")

say_hello("Alice",15) # "Alice" คือ argument เพราะมันเป็นค่าที่เราส่งเข้าไปในฟังก์ชัน say_hello เมื่อเราเรียกใช้งานฟังก์ชันนั้นๆ
show_table(5) # 5 คือ argument เพราะมันเป็นค่าที่เราส่งเข้าไปในฟังก์ชัน show_table เมื่อเราเรียกใช้งานฟังก์ชันนั้นๆ