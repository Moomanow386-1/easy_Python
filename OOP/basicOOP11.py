#การพ้องรูป (Polymorphism)
#overloading method

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
    # def _showData(self):
    #     print(f"ชื่อพนักงาน {self.__name} มีเงินเดือน {self.__salary:.2f} ตำแหน่ง {self._department}")

    #income per year
    def _getIncome(self):
        return self.__salary * 12

    def __str__(self):
        return (f"ชื่อพนักงาน {self.__name}, แผนก {self._department}, เงินเดือน {self.__salary}, รายได้ต่อปี {self._getIncome()}")

class Accounting(Employee):
    __departmentName = "Accountant"
    def __init__(self,name,salary):
        super().__init__(name,salary,self.__departmentName)
        # super()._showData()

class Programmer(Employee):
    __departmentName = "Seller"
    def __init__(self,name,salary):
        super().__init__(name,salary,self.__departmentName)
        # super()._showData()

class sale(Employee):
    __departmentName = "Stock"
    def __init__(self,name,salary):
        super().__init__(name,salary,self.__departmentName)
        # super()._showData()

account = Accounting("Fuse", 12000)
print(account.__str__())

programmer = Programmer("JOJO", 40000)
print(programmer.__str__())

sale = sale("Nana", 500000)
print(sale.__str__())