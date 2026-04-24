from employee import Employee

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