#ฟังก์ชันเสริม

#การสร้าง Constructor
class Employee: #make class (ตัวพิมพ์ใหญ่)
    #make method

    #Constructor
    def __init__(self,name,salary,department):
        self.name = name 
        self.salary = salary 
        self.department = department

    def showData(self):
        print(f"ชื่อพนักงาน {self.name} มีเงินเดือน {self.salary:.2f} ตำแหน่ง {self.department}")


# make object  
obj1 = Employee("Fuse", 20000, "Accountant") 
obj2 = Employee("Nana", 45000, "Teacher")

print(isinstance(obj1, Employee)) #check
print(isinstance(obj1, int)) 

print(dir(obj1)) #ฟังก์ชันสำหรับแสดงรายชื่อแอตทริบิวต์ (attributes) และเมธอด (methods) ทั้งหมดที่วัตถุ obj มี (รวมทั้ง built-in ของ Python)
"""Output: ลิสต์ยาวๆ เช่น ['__class__', '__delattr__', ..., 'department', 'name', 'salary', 'showData']
__class__, __init__, __delattr__ ฯลฯ: แอตทริบิวต์/เมธอดพิเศษของ Python (magic methods) ที่ทุกวัตถุมี
'department', 'name', 'salary': แอตทริบิวต์ที่กำหนดเองในคลาส Employee
'showData': เมธอดที่กำหนดเอง
ใช้ทำไม: ช่วยสำรวจว่าวัตถุมีอะไรบ้าง สะดวกตอน debug หรือเรียนรู้ API ของวัตถุ"""

print(obj1.__class__)
