# score = [20, 30, 40]
# print(len(score))    
# print(score[0])    
# print(score[1])
# print(score[2])
# score[0] = 100
# print(score)


# color1 = ["red", "green", "blue"]
# color2 = ["yellow", "pink", "purple"]
# color = color1 + color2
# print(color)


colors = ["red", "green", "blue"]
colors.append("yellow")   
print(colors)

colors.extend(["pink", "purple", "orange"])   
print(colors)

colors.insert(1, "orange")    
print(colors)

print(colors.count("orange"))

colors.remove("red")
print(colors)

#colors.clear()

colors.sort()
print(colors)

colors.reverse()
print(colors)


