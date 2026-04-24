#from employee import Employee คือ การนำเข้า class Employee จากไฟล์ employee.py เพื่อให้สามารถใช้งาน class Employee ได้ในไฟล์นี้
from employee import Employee

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