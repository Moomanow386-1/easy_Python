#ชื่อ, เงินเดือน
class Employee: #make class (ตัวพิมพ์ใหญ่)
    #make method
    def detail(self,name,salary,department): #self คือ ตัวอ้างอิงถึง object ที่เรียกใช้งาน method
        self.name = name #make atrribute name for object = parameter
        self.salary = salary 
        self.department = department
        print(f"ชื่อพนักงาน {self.name} มีเงินเดือน {self.salary:.2f} ตำแหน่ง {self.department}")

# make object 
obj1 = Employee() #สร้าง object จาก class
obj1.detail("แหลม", 50000, "ผู้จัดการ") #เรียกใช้งาน method บน object obj1

obj2 = Employee()
obj2.detail("กล้วย", 70000, "ผู้ช่วย")

