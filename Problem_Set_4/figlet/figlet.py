import sys
import random
from pyfiglet import Figlet

figlet = Figlet()

if len(sys.argv) == 1:
    s = input("Input: ")
    figlet.setFont(font=random.choice(figlet.getFonts()))
    print(figlet.renderText(s))

elif len(sys.argv) == 3:
    if sys.argv[1] != "-f" and sys.argv[1] != "--font":
        sys.exit("Invalid usage")
    if not sys.argv[2] in figlet.getFonts():
        sys.exit("Invalid usage")
    else:
        s = input("Input: ")
        figlet.setFont(font=sys.argv[2])
        print(figlet.renderText(s))
else:
    sys.exit("Invalid usage")
