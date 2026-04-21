#Setter & Getter

class Employee: 
    #Constructor (private method)
    def __init__(self,name,salary,department):
        #private attribute
        self.__name = name 
        self.__salary = salary #private
        self.__department = department #private
        
    #protected method
    # def _showData(self):
    #     print(f"ชื่อพนักงาน {self.__name} มีเงินเดือน {self.__salary:.2f} ตำแหน่ง {self.__department}")

    #protected method, การเรียกใช้อีกวิธีหนึ่ง
    def _showData(self):
        print(f"ชื่อพนักงาน {self.getName()} มีเงินเดือน {self.getSalary():.2f} ตำแหน่ง {self.getDepartment()}")

    # setter method
    def setName(self, newname):
        self.__name = newname

    def setSalary(self, newsalary):
        self.__salary = newsalary

    def setDepartment(self, department):
        self.__department = department

    # getter method
    def getName(self):
        return self.__name
    
    def getSalary(self):
        return self.__salary
    
    def getDepartment(self):
        return self.__department
    
# make object  
obj1 = Employee("Fuse", 20000, "Accountant") 
obj1.setName("จอมมาร")
obj1.setSalary(99999)
obj1.setDepartment("ทาส")
obj1._showData() 

obj2 = Employee("Nana", 45000, "Teacher")
#print(obj2.getName())
#print(obj2.getSalary())
#print(obj2.getDepartment())
obj1._showData()
print(obj2.getName())