str = input("camelCase: ")
print("snake_case: ", end="")
for s in str:
    if s.isupper():
        print("_" + s.lower(), end="")
    else:
        print(s, end="")
print()
