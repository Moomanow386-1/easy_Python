#capture pattern คือ การใช้ตัวแปรเพื่อจับค่าที่ตรงกับกรณีที่กำหนดไว้ใน match-case statement ซึ่งจะช่วยให้เราสามารถนำค่าที่จับได้ไปใช้งานต่อได้
service = 0
match service:
    case 1:
        print("ฝากเงิน")
    case 2:    
        print("ถอนเงิน")
    case 3:
        print("สอบถามยอดคงเหลือ")
    case service:
        print(f"ไม่มีบริการหมายเลข {service}")