def main():
    time = input("What time is it? ")
    meal = convert(time)
    if 7 <= meal <= 8:
        print("breakfast time")
    elif 12 <= meal <= 13:
        print("lunch time")
    elif 18 <= meal <= 19:
        print("dinner time")


def convert(time):
    hours, minutes = time.split(":")
    minutes = float(minutes) / 60
    hours = float(hours)
    return hours + minutes


if __name__ == "__main__":
    main()
