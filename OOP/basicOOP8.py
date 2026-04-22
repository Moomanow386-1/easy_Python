#Inheritance => การสืบทอดคุณสมบัติม เอาที่มีอยู่แล้วนำมาต่อยอดหรือมาใช้

class Employee: 
    #class variable (public attribute)
    minSalary = 12000
    maxSalary = 50000
    companyName = "XYZ company"

    def __init__(self,name,salary,department):
        #instance variable #must make object first
        self.__name = name 
        self.__salary = salary #private
        self._department = department #private

    #protected method, การเรียกใช้อีกวิธีหนึ่ง
    def _showData(self):
        print(f"ชื่อพนักงาน {self.__name} มีเงินเดือน {self.__salary:.2f} ตำแหน่ง {self._department}")

class Accounting(Employee):
    __departmentName = "Accountant"
    def __init__(self):
        pass

class Programmer(Employee):
    __departmentName = "Seller"
    def __init__(self):
        pass

class sale(Employee):
    __departmentName = "Stock"
    def __init__(self):
        pass

account = Accounting()
print(account.companyName)

programmer = Programmer()
#print(programmer.__minSalary) #error
print(programmer.minSalary)

#print(programmer._Employee__minSalary)

sale = sale()

