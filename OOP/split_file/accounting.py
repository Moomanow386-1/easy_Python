from employee import Employee

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