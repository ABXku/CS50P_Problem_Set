import sys
from PIL import Image, ImageOps

extension = (".jpg", ".jpeg", ".png")

if len(sys.argv) == 3:
    try:
        if sys.argv[1].endswith(extension) and sys.argv[2].endswith(extension):
            if sys.argv[1].split(".")[1] == sys.argv[2].split(".")[1]:
                shirt = Image.open("shirt.png")
                image = Image.open(sys.argv[1])
                new_image = ImageOps.fit(image, shirt.size)
                new_image.paste(shirt, shirt)
                new_image.save(sys.argv[2])
            else:
                sys.exit("Input and output have different extensions")
        else:
            sys.exit("Invalid output")
    except IndexError:
        sys.exit("Too few command-line arguments")
else:
    sys.exit("Too many command-line arguments")