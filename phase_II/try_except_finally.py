#exception คือ ข้อผิดพลาดของข้อมูล

try:
    num1 = int(input("ป้อนตัวเลขตัวที่ 1 : "))
    num2 = int(input("ป้อนตัวเลขตัวที่ 2 : "))

    result = num1/num2
    print(result)
except ValueError:
    print("ข้อมูลไม่ถูกต้อง กรุณาป้อนช้อมูลเฉพาะตัวเลขเท่านั้น")
except ZeroDivisionError:
    print("หารด้วย 0 ไม่ได้")

finally:
    print("---------------")
    print("End Program")
    print("--------------")