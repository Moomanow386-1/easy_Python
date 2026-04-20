animals = {"cat", "dog", "rabbit"} #ไม่เรียงลำดับ(ตอนปริ้น)และไม่ซ้ำกัน
animals2 = {"cat", "dog", "rabbit", "cat"} #ไม่เรียงลำดับ(ตอนปริ้น)และไม่ซ้ำกัน
print(animals)
print(animals2) #จะไม่แสดง "cat" ซ้ำกัน
animals.add("hamster") #เพิ่ม "hamster" เข้าไปใน set
print(animals)
animals.remove("dog") #ลบ "dog" ออกจาก set
print(animals)
animals.update({"hamster", "parrot"}) #เพิ่ม "hamster" และ "parrot" เข้าไปใน set
print(animals)

pets = {"cat", "dog", "hamster", "dragon"}
print(animals.intersection(pets)) #แสดงสมาชิกที่มีอยู่ในทั้งสอง set
print(animals.union(pets)) #แสดงสมาชิกทั้งหมดที่มีอยู่ในทั้งสอง set
print(animals.difference(pets)) #แสดงสมาชิกที่มีอยู่ใน animals แต่ไม่มีใน pets
print(pets.difference(animals)) #แสดงสมาชิกที่มีอยู่ใน pets แต่ไม่มีใน animals