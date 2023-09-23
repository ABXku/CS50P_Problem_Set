def main():
    greeting = input("Greeting: ")
    print(f"${value(greeting)}")


def value(greeting):
    n_greeting = greeting.lower().strip()
    if n_greeting[0:5] == "hello":
        return 0
    elif n_greeting[0:1] == "h":
        return 20
    else:
        return 100


if __name__ == "__main__":
    main()
