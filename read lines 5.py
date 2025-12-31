filepath = input("Enter the file path: ")
try:
    with open(filepath, "r") as file:
        lines_list = file.readlines()
    print("Lines in the list:")
    print(lines_list)
except FileNotFoundError:
    print("Error: File not found!")
except Exception as e:
    print("An error occurred:", e)