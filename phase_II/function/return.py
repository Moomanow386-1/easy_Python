def get_capital(city):
    if city == "Bangkok":
        return "Bangkok is the capital of Thailand."
    elif city == "Paris":
        return "Paris is the capital of France."
    elif city == "Tokyo":
        return "Tokyo is the capital of Japan."
    else:
        return "Capital information not available for this city."
    
city = get_capital("Bangkok")
print(city)


def pi():
    return 3.14
result = pi() * 5**2
print(f"Area of circle is {result} m^2")


def summation(*numbers):
    total = 0
    for n in numbers:
        total += n
    return total

print(summation(1, 2, 3, 4, 5)) # ผลลัพธ์จะเป็น 15 เพราะฟังก์ชัน summation จะรับ argument ที่ไม่จำกัดจำนวนและทำการบวกค่าทั้งหมดที่ส่งเข้ามาในฟังก์ชัน