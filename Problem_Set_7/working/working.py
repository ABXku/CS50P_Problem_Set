import re
import sys

def main():
    print(convert(input("Hours: ")))

def convert(s):
    reg = "([1-9]|1[0-2]):?([0-5][0-9])? (AM|PM)"
    if match := re.search(r"^" + reg + " to " + reg + "$", s):
        if match.group(3) == "AM" : first = convert_am(match.group(1), match.group(2))
        elif match.group(3) == "PM": first = convert_pm(match.group(1), match.group(2))
        if match.group(6) == "AM" : second = convert_am(match.group(4), match.group(5))
        elif match.group(6) == "PM": second = convert_pm(match.group(4), match.group(5))
        return first + " to " + second
    else:
        raise ValueError

def convert_am(hour, min):
    if hour == "12":
        if min: return f"00:{min}"
        else : return "00:00"
    else:
        if min : return f"{int(hour):02}:{min}"
        else :  return f"{int(hour):02}:00"

def convert_pm(hour, min):
    if hour == "12":
        if min: return f"12:{min}"
        else: return "12:00"
    else:
        if min: return f"{(int(hour) + 12):02}:{min}"
        else :  return f"{(int(hour) + 12):02}:00"

if __name__ == "__main__":
    main()