while True:
    try:
        x, y = input("Fraction: ").split("/")
        if int(x) <= int(y):
            answer = round((int(x) / int(y) * 100))
            if answer <= 1:
                print("E")
            elif answer >= 99:
                print("F")
            else:
                print(f"{answer}%")
            break
    except (ValueError, ZeroDivisionError):
        pass
