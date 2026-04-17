# Mapping Pattern คือ การจับคู่กับโครงสร้างข้อมูลที่มีลักษณะเป็นแผนที่ (mapping) เช่น dictionary โดยสามารถจับคู่กับคีย์และค่าของแผนที่ได้


data = {"name": "Alice", "age": 30}
match data:
    case {"name": "Alice", "age": 30}:
        print("ข้อมูลตรงกับรูปแบบที่กำหนด")
    case _:
        print("ข้อมูลไม่ถูกต้อง")


customer = [{"name": "John", "type": "VIP"},
           {"name": "Max", "type": "Regular"},
           {"name": "Bob", "type": "Regular"}]

id = int(input("กรุณาใส่หมายเลขลูกค้า (0-2): "))
print(f"ลูกค้าหมายเลข {id} คือ {customer[id]['name']}") #การเข้าถึงข้อมูลใน dictionary โดยใช้คีย์ 'name' เพื่อแสดงชื่อของลูกค้า

match customer[id]:
    case {"type": "VIP"}:
        print("ลูกค้าเป็น VIP")
    case {"type": "Regular"}:
        print("ลูกค้าเป็น Regular")
    case _:
        print("ข้อมูลไม่ถูกต้อง")