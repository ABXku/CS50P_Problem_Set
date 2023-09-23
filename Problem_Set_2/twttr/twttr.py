str = input("Input: ")
print("Output: ", end="")
for s in str:
    s_t = s.lower()
    if s_t != "a" and s_t != "e" and s_t != "i" and s_t != "o" and s_t != "u":
        print(s, end="")
print()
