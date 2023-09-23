def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if 2 <= len(s) <= 6:
        for i in range(0, 2):
            if not s[i].isalpha():
                return False
        for i in range(2, len(s)):
            if not s[i].isalpha() and not s[i].isdigit():
                return False
            elif s[0:i].isalpha() and s[i].isdigit():
                if s[i] == "0":
                    return False
                else:
                    for j in s[i : len(s)]:
                        if (j.isdigit()) == False:
                            return False
        return True
    else:
        return False


if __name__ == "__main__":
    main()
