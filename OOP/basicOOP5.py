#Encapsulation = การห่อหุ้ม

class Employee: #make class (ตัวพิมพ์ใหญ่)
    #make method

    #Constructor (private method)
    def __init__(self,name,salary,department):
        #private attribute
        self._name = name 
        self.__salary = salary #private
        self.__department = department #private
        self.__showData()
    #private method
    def __showData(self):
        print(f"ชื่อพนักงาน {self._name} มีเงินเดือน {self.__salary:.2f} ตำแหน่ง {self.__department}")

# make object  
obj1 = Employee("Fuse", 20000, "Accountant") 
obj1.__salary = 300000000 #not changed
#obj1.__showData() #error

obj2 = Employee("Nana", 45000, "Teacher")