from accounting import Accounting
from programmer import Programmer
from sale import sale

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