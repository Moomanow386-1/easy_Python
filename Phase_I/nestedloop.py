# for i in range(5):
#     for j in range(5):
#         print(i, j)

num1,num2 = int(input("ป้อนตัวเลขตัวที่ 1: ")), int(input("ป้อนตัวเลขตัวที่ 2: "))
for i in range(num1, num2 + 1):
    for j in range(1, 13):
        print(i, "x", j, "=", i * j)  
