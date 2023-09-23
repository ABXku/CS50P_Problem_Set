import random


def main():
    level = get_level()
    score = 0
    for _ in range(1, 11):
        x = generate_integer(level)
        y = generate_integer(level)
        ans = x + y
        error = 0
        for _ in range(1, 4):
            try:
                user_ans = int(input(f"{x} + {y} = "))
                if user_ans == ans:
                    score += 1
                    break
                else:
                    print("EEE")
                    error += 1
            except ValueError:
                print("EEE")
                error += 1
                pass
            if error == 3:
                print(f"{x} + {y} = {ans}")
    print("Score:", score)


def get_level():
    while True:
        try:
            level = int(input("Level: "))
            assert 1 <= level <= 3
            return level

        except (ValueError, AssertionError):
            pass


def generate_integer(level):
    if level == 1:
        return random.randint(0, 9)
    elif level == 2:
        return random.randint(10, 99)
    elif level == 3:
        return random.randint(100, 999)


if __name__ == "__main__":
    main()
