import sys
import csv
from tabulate import tabulate

contents = []

if len(sys.argv) <= 2:
    try:
        if sys.argv[1].endswith(".csv"):
            with open(sys.argv[1]) as file:
                reader = csv.reader(file)
                for row in reader:
                    contents.append(row)
            print(tabulate(contents, headers="firstrow", tablefmt="grid"))
        else:
            sys.exit("Not a CSV file")
    except IndexError:
        sys.exit("Too few command-line arguments")
    except FileNotFoundError:
        sys.exit("File does not exist")
else:
    sys.exit("Too many command-line arguments")