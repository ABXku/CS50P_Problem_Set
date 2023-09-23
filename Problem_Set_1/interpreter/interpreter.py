exp = input("Expression: ")
x = float(exp.split(" ")[0])
y = exp.split(" ")[1]
z = float(exp.split(" ")[2])
if y == "+":
    print(x + z)
elif y == "-":
    print(x - z)
elif y == "*":
    print(x * z)
elif y == "/":
    print(x / z)
