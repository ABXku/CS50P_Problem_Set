def main():
    while True:
        try:
            user_input = input("Fraction: ")
            print(gauge(convert(user_input)))
            break

        except (ZeroDivisionError, ValueError):
            pass


def convert(fraction):
    x, y = fraction.split("/")
    return round((int(x) / int(y) * 100))


def gauge(percentage):
    Z = percentage
    if Z <= 1:
        return "E"
    elif Z >= 99:
        return "F"
    else:
        return f"{Z}%"


if __name__ == "__main__":
    main()
