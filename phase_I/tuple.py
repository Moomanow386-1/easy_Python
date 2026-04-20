#tuple
product = ("red", "blue", "green")
#product[0] = "yellow"    #ไม่สามารถเปลี่ยนแปลงค่าในทูเพิลได้ เพราะทูเพิลเป็นข้อมูลที่ไม่สามารถแก้ไขได้ (immutable) ซึ่งหมายความว่า เมื่อสร้างทูเพิลแล้ว เราไม่สามารถเปลี่ยนแปลงค่าของมันได้อีกต่อไป
print(product[0])
print(product[1])
print(product[2])
print(type(product))


product = ("red", "blue", "green")
color, color2, color3 = product    #การแยกค่าจากทูเพิลออกมาเป็นตัวแปรต่าง ๆ เรียกว่า การ unpacking
print(color)
print(color2)
print(color3)
print(type(product))
print(product*2)    #การทำซ้ำค่าของทูเพิล โดยการใช้เครื่องหมาย * ตามด้วยจำนวนครั้งที่ต้องการทำซ้ำ
print(product.index("blue"))    #การค้นหาตำแหน่งของค่าที่ต้องการในทูเพิล โดยใช้เมธอด index() ซึ่งจะคืนค่าตำแหน่งของค่าที่พบเป็นจำนวนเต็ม (integer) โดยเริ่มนับจาก 0
print(product.count("red"))    #การนับจำนวนครั้งที่ค่าที่ต้องการปร