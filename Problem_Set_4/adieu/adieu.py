import inflect

p = inflect.engine()

name_list = []

while True:
    try:
        new_name = input("Input: ")
        name_list.append(new_name)
    except EOFError:
        print()
        break
print(f"Adieu, adieu, to", p.join(name_list))
