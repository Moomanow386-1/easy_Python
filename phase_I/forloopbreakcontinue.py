#break and continue statements in for loop

for i in range(1, 11):
    if i == 5:
        break #หยุดการทำงานของ loop ทันทีเมื่อ i เท่ากับ 5
    print(i)


for j in range(1, 11):
    if j == 5:
        continue #ข้ามการทำงานในรอบนั้นๆ เมื่อ j เท่ากับ 5 และไปทำงานในรอบถัดไป
    print(j)