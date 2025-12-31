import csv

data = [
    {"Name": "Abhi", "Age": 22, "Branch": "MCA"},
    {"Name": "Nandana", "Age": 21, "Branch": "BCA"},
    {"Name": "Akshay", "Age": 21, "Branch": "Bcom"}
]

filename = "output.csv"

try:
    with open(filename, "w", newline='', encoding="utf-8") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=data[0].keys())
        writer.writeheader()
        writer.writerows(data)
    print("Dictionary written to CSV successfully!\n")

    print("Reading CSV content:")
    with open(filename, "r", encoding="utf-8") as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            print(row)

except Exception as e:
    print("An error occurred:", e)