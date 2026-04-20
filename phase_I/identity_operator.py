#identity operator
colorA = ("red", "green", "blue")
colorB = ("red", "green", "blue")
data = colorA
print(colorA is not colorB)    #การใช้ตัวดำเนินการ is เพื่อเปรียบเทียบว่า colorA และ colorB เป็นวัตถุเดียวกันในหน่วยความจำหรือไม่ ซึ่งจะคืนค่า True ถ้าเป็นวัตถุเดียวกัน และ False ถ้าไม่ใช่
print(colorA is data)    #การใช้ตัวดำเนินการ is เพื่อเปรียบเทียบว่า colorA และ data เป็นวัตถุเดียวกันในหน่วยความจำหรือไม่ ซึ่งจะคืนค่า True ถ้าเป็นวัตถุเดียวกัน และ False ถ้าไม่ใช่