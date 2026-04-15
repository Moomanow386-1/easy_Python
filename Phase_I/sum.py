# total = 0
# for i in range(1, 6):
#     total += i
# print("ผลรวมของตัวเลขคือ : ", total)

# total = 0
# for i in range(1, 6):
#     number = int(input("ป้อนตัวเลขที่ " + str(i) + " : ")) 
#     total += number       
# print("ผลรวมของตัวเลขคือ : ", total)

total = 0
while True:
    number = int(input("ป้อนตัวเลข: "))
    if number <= 0: #ถ้าป้อนเลข 0 จะหยุดการทำงานของ loop
        break
    total += number
print("ผลรวมของตัวเลขคือ : ", total)
        