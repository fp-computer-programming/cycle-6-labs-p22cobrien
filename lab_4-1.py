# Author: CMOB 11/12/2021

colors = ["blue", "purple", "red", "black"]
print(colors)

colors.extend(["yellow", "green", "white"])
print(colors)

print(colors.count("yellow"))

colors.insert(3, "teal")
print(colors)

colors.clear()
print(colors)

print(colors.count("red"))
