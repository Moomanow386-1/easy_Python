#การพ้องรูป (Polymorphism)
#overloading method คือ การเขียน method ที่มีชื่อเดียวกัน แต่มีพารามิเตอร์ที่แตกต่างกัน

class Employee: 
    #class variable (public attribute)
    minSalary = 12000
    maxSalary = 50000
    companyName = "XYZ company"

    def __init__(self,name,salary,department):
        #instance variable #must make object first
        self.__name = name 
        self.__salary = salary #private
        self._department = department 

    def _showData(self):
        print(f"ชื่อพนักงาน {self.__name} มีเงินเดือน {self.__salary:.2f} ตำแหน่ง {self._department}")

    #income per year
    def _getIncome(self):
        return self.__salary * 12
    
    #overloading method คือ การเขียน method ที่มีชื่อเดียวกัน แต่มีพารามิเตอร์ที่แตกต่างกัน
    def _getIncome(self,bonus = 0):
        return self.__salary * 12 + bonus

    def __str__(self):
        return (f"ชื่อพนักงาน {self.__name}, แผนก {self._department}, เงินเดือน {self.__salary}, รายได้ต่อปี {self._getIncome()}")

class Accounting(Employee):
    __departmentName = "Accountant"
    def __init__(self,name,salary,age):
        super().__init__(name,salary,self.__departmentName)
        self.__age = age

    #overiding method คือ การเขียน method ที่มีชื่อเดียวกันกับ method ใน class แม่ แต่มีการทำงานที่แตกต่างกัน
    def _showData(self):
        super()._showData() #เรียก method ของ class แม่
        print(f"อายุ {self.__age} ปี")
        print("------------------")

    def __str__(self):
        return (super().__str__() + f", อายุ {self.__age} ปี")

class Programmer(Employee):
    __departmentName = "Seller"
    def __init__(self,name,salary,experience,skill):
        super().__init__(name,salary,self.__departmentName)
        self.__experience = experience
        self.__skill = skill

    def _showData(self):
        super()._showData() #เรียก method ของ class แม่
        print(f"ประสบการณ์ {self.__experience} ทักษะ {self.__skill}")
        print("------------------")

    def __str__(self):
        return (super().__str__() + f", ประสบการณ์ {self.__experience}, ทักษะ {self.__skill}")

class sale(Employee):
    __departmentName = "Stock"
    def __init__(self,name,salary,area):
        super().__init__(name,salary,self.__departmentName)
        self.__area = area

    def _showData(self):
        super()._showData() #เรียก method ของ class แม่
        print(f"โซน {self.__area}")
        print("------------------")

    def __str__(self):
        return (super().__str__() + f", โซน {self.__area}")

account = Accounting("Fuse", 12000, 30)
#account._showData()
print(account.__str__())
print(account._getIncome(5000)) #เรียก method ที่มีการ overloading

programmer = Programmer("JOJO", 40000, "2 years", "developer")
#programmer._showData()
print(programmer.__str__())
print(programmer._getIncome(10000)) #เรียก method ที่มีการ overloading

sale = sale("Nana", 500000, "Bankok")
#sale._showData()
print(sale.__str__())
print(sale._getIncome()) #เรียก method ที่มีการ overloading