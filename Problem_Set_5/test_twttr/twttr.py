def main():
    str = input("Input: ")
    print(f"Output: {shorten(str)}")


def shorten(word):
    shorten_word = ""
    s_t = w.lower()
    if s_t != "a" and s_t != "e" and s_t != "i" and s_t != "o" and s_t != "u":
        shorten_word += w
    return shorten_word


if __name__ == "__main__":
    main()
