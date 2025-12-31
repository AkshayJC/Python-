import csv

filepath = input("Enter CSV file path: ")
col_names = input("Enter column names to read (e.g., Name,Age): ").split(",")

try:
    with open(filepath, "r", encoding="utf-8-sig") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            selected = [row[col] for col in col_names if col in row]
            print(selected)
except FileNotFoundError:
    print("Error: File not found!")
except Exception as e:
    print("An error occurred:", e)