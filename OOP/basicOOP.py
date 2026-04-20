#ชื่อ, เงินเดือน
class Employee: #make class (ตัวพิมพ์ใหญ่)
    #make method
    def detail(self): #self คือ ตัวอ้างอิงถึง object ที่เรียกใช้งาน method
        self.name = "moomanow" #make atrribute name for object
        self.salary = 25000
        print(f"ชื่อพนักงาน {self.name} มีเงินเดือน {self.salary:.2f}")

# make object 
emp1 = Employee() #สร้าง object จาก class
emp1.detail() #เรียกใช้งาน method บน object emp1