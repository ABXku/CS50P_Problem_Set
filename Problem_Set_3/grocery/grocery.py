grocery_list = {}

while True:
    try:
        item = input().upper()
        if item in grocery_list:
            grocery_list[item] += 1
        else:
            grocery_list.update({item: 1})
    except KeyError:
        pass
    except EOFError:
        print()
        sorted_list = sorted(grocery_list)
        for i in sorted_list:
            print(f"{grocery_list[i]} {i}")
        break
