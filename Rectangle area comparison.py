class Rectangle:
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def area(self):
        return self.length * self.breadth

    def __lt__(self, other):
        return self.area() < other.area()

print("Rectangle 1")
l1 = int(input("Enter the length: "))
b1 = int(input("Enter the breadth: "))
r1 = Rectangle(l1, b1)

print("\nRectangle 2")
l2 = int(input("Enter the length: "))
b2 = int(input("Enter the breadth: "))
r2 = Rectangle(l2, b2)

print("\n")
if r1 < r2:
    print("r1 has smaller area")
else:
    print("r2 has smaller area")