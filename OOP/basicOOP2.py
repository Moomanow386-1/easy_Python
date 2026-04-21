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

    def __del__(self): #ไม่ระบุก็ได้, เมธอดพิเศษที่เรียกใช้อัตโนมัติเมื่อวัตถุถูกทำลาย (เช่น เมื่อโปรแกรมจบหรือวัตถุถูกลบ)
        print("Call Destructor")

# make object  
obj1 = Employee("Fuse", 20000, "Accountant") #ข้อมูลจะถูกกำหนดทันที ไม่ต้องเรียกเมธอดเพิ่มเติม
obj1.salary = 70000
obj1.showData()

obj2 = Employee("Nana", 45000, "Teacher")
obj2.showData()
