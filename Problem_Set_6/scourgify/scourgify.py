import sys
import csv
from tabulate import tabulate

new_data = []

if len(sys.argv) <= 3:
    try:
        with open(sys.argv[1]) as file:
            reader = csv.DictReader(file)
            for row in reader:
                last, first = row["name"].split(",")
                house = row["house"]
                new_data.append({"first":first.strip(), "last":last.strip(), "house":house})
            #print(tabulate(new_data, headers="firstrow", tablefmt="grid"))

    except IndexError:
        sys.exit("Too few command-line arguments")
    except FileNotFoundError:
        sys.exit(f"Could not read {sys.argv[1]}")

    with open(sys.argv[2], "w") as file:
        writer = csv.DictWriter(file, fieldnames = ["first", "last", "house"])
        writer.writeheader()
        for line in new_data:
            writer.writerow({"first": line["first"], "last": line["last"], "house": line["house"]})
else:
    sys.exit("Too many command-line arguments")