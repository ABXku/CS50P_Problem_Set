import random

while True:
    try:
        level = int(input("Level: "))
        assert level > 0
        break

    except (ValueError, AssertionError):
        pass

real_answer = random.randint(1, level)

while True:
    try:
        user_answer = int(input("Guess: "))
        assert level > 0
        if user_answer == real_answer:
            print("Just right!")
            break
        elif user_answer > real_answer:
            print("Too large!")
        else:
            print("Too small!")

    except (ValueError, AssertionError):
        pass
