import sys

if len(sys.argv) <= 2:
    try:
        if sys.argv[1].endswith(".py"):
            count = 0
            with open(sys.argv[1]) as file:
                for line in file:
                    if not line.lstrip().startswith("#") and not line.lstrip() == "":
                        count += 1
                print(f"{count}")

        else:
            sys.exit("Not a Python file")
    except IndexError:
        sys.exit("Too few command-line arguments")
    except FileNotFoundError:
        sys.exit("File does not exist")
else:
    sys.exit("Too many command-line arguments")