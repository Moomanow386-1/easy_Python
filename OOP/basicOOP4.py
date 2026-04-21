#Encapsulation = การห่อหุ้ม

class Employee: #make class (ตัวพิมพ์ใหญ่)
    #make method

    #Constructor (private method)
    def __init__(self,name,salary,department):
        #protected attribute
        self._name = name 
        self._salary = salary 
        self._department = department

    #protected method
    def _showData(self):
        print(f"ชื่อพนักงาน {self._name} มีเงินเดือน {self._salary:.2f} ตำแหน่ง {self._department}")

# make object  
obj1 = Employee("Fuse", 20000, "Accountant") 
obj1.salary = 399999 #not changed
obj1._salary = 400000 #changed

obj1._showData()
obj2 = Employee("Nana", 45000, "Teacher")