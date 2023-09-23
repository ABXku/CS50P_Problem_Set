months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December",
]


while True:
    try:
        date = input("Date: ").strip()
        if "/" in date:
            if months[int(date.split("/")[0]) - 1]:
                element = date.split("/")
                day = int(element[1])
                if 1 <= day <= 31:
                    print(f"{element[2]}-{int(element[0]):02}-{day:02}")
                    break
        elif " " in date and "," in date:
            if date.split(" ")[0] in months:
                element = date.split(" ")
                converted_month = months.index(element[0]) + 1
                converted_day = int(element[1].strip(","))
                if 1 <= converted_day <= 31:
                    print(f"{element[2]}-{converted_month:02}-{converted_day:02}")
                    break
    except (KeyError, IndexError, ValueError):
        pass
