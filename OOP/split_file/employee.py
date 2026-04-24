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