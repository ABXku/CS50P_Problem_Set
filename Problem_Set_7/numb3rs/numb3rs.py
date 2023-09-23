import re
import sys


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    if re.search(r"^[0-9]+\.[0-9]+\.[0-9]+\.[0-9]+$", ip):
        first, second, third, forth = re.split(r"\.", ip, maxsplit=3)
        # print(f"First = {first} Second = {second} Third = {third}")
        if (
            int(first) <= 255
            and int(second) <= 255
            and int(third) <= 255
            and int(forth) <= 255
        ):
            return True
        else:
            return False
    else:
        return False


if __name__ == "__main__":
    main()
