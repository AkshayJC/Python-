source = input("Enter source file path: ")
destination = input("Enter destination file path: ")

try:
    with open(source, "r") as src, open(destination, "w") as dst:
        lines = src.readlines()
        for i in range(len(lines)):
            if (i + 1) % 2 != 0:  
                dst.write(lines[i])
    print("Odd lines copied successfully!")
except FileNotFoundError:
    print("Error: Source file not found!")
except Exception as e:
    print("An error occurred:", e)