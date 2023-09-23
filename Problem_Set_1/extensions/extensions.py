file = input("File name: ").strip().lower()
if "." in file:
    extension = file.split(".")[-1]
    if extension == "jpg" or extension == "jpeg":
        print("image/jpeg")
    elif extension == "png" or extension == "gif":
        print("image/" + extension)
    elif extension == "pdf" or extension == "zip":
        print("application/" + extension)
    elif extension == "txt":
        print("text/plain")
    else:
        print("application/octet-stream")
else:
    print("application/octet-stream")
