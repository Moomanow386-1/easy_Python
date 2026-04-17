#literal pattern matching คือ การจับคู่ค่าคงที่ เช่น ตัวเลข สตริง หรือ None เป็นต้น โดยใช้คำสั่ง match-case ในการตรวจสอบค่าของตัวแปรและทำงานตามกรณีที่ตรงกัน
service = 1
match service:
    case 1:
        print("ฝากเงิน")
    case 2:    
        print("ถอนเงิน")
    case 3:
        print("สอบถามยอดคงเหลือ")
    case None:
        print("ข้อมูลไม่ถูกต้อง")