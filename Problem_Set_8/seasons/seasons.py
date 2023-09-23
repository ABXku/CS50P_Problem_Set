from datetime import date
import sys
import inflect

p = inflect.engine()

def main():
    try:
        birthday = date.fromisoformat(input("Date of Birth: "))
    except ValueError:
        sys.exit("Invalid date")
    print(f"{convert(birthday)} minutes")

def convert(birthday):
    today = date.today()
    minutes = (today - birthday).days * 24 * 60
    return (p.number_to_words(minutes, andword="")).capitalize()


if __name__ == "__main__":
    main()