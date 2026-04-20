#main program
import calculator
print(calculator.add(10, 20))
print(calculator.subtract(42, 17))
print(calculator.multiply(10, 20))
print(calculator.power(10, 2))


import calculator as cal
print(cal.add(10, 20))
print(cal.subtract(42, 17))
print(cal.multiply(10, 20))
print(cal.power(10, 2))


import database as db
db.insert()
print(db.name)


from calculator import multiply,add as cal, subtract
print(multiply(5, 2))
print(cal(20, 17))
print(subtract(10, 5))


from calculator import *
print(multiply(5, 2))
print(add(20, 17))
print(subtract(10, 5))