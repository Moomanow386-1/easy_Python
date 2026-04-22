#Class variable

class Employee: 
    #class variable  อ้างอิงถึงได้เลยไม่ต้องสร้าง object
    _minSalary = 12000
    _maxSalary = 50000

    def __init__(self,name,salary,department):
        #instance variable #must make object first
        self.__name = name 
        self.__salary = salary #private
        self._department = department #private

    #protected method, การเรียกใช้อีกวิธีหนึ่ง
    def _showData(self):
        print(f"ชื่อพนักงาน {self.__name} มีเงินเดือน {self.__salary:.2f} ตำแหน่ง {self._department}")

# make object  
obj1 = Employee("Fuse", 20000, "Accountant") 
obj1._showData() 
print(obj1._department)

print(f"เงินเดือนต่ำสุดของพนักงานคือ {Employee._minSalary}")

#print(Employee.__name) #error

obj2 = Employee("Nana", 45000, "Teacher")
obj2._showData()
