try:
    with open("sample1.txt", "a+", encoding="utf-8") as file:
        file.writelines(["\nthis is a new line", "\nthis is a new line"])
        file.seek(0)
        print(file.read())
        file.writelines("\nappended")
except PermissionError:
    print("permission issue")
except IsADirectoryError:
    print("specifies path a directory")
except OSError as e:
    print(f"an os error occoured: {e} ")
