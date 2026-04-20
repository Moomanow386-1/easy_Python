#exception คือ ข้อผิดพลาดของข้อมูล

try:
    num1 = int(input("ป้อนตัวเลขตัวที่ 1 : "))
    num2 = int(input("ป้อนตัวเลขตัวที่ 2 : "))
    if num1 < 0 or num2 < 0:
        raise Exception("ข้อมูลตัวเลขต้องเป็นค่าบวกเท่านั้น") #โยนข้อผิดพลาด (raise an exception) เมื่อเงื่อนไขไม่ตรงตามที่กำหนด เช่น ในโค้ดนี้ ถ้าตัวเลขที่ป้อนเป็นค่าลบ จะใช้ raise Exception("ข้อมูลตัวเลขต้องเป็นค่าบวกเท่านั้น") เพื่อหยุดการทำงานและแสดงข้อความผิดพลาดนั้นออกมา
    result = num1/num2
    print(result)
except ValueError:
    print("ข้อมูลไม่ถูกต้อง กรุณาป้อนช้อมูลเฉพาะตัวเลขเท่านั้น")
except ZeroDivisionError:
    print("หารด้วย 0 ไม่ได้")
finally:
    print("---------------")
    print("End Program")
    print("---------------")