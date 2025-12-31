class Rectangle:
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def area(self):
        return self.length * self.breadth

    def perimeter(self):
        return 2 * (self.length + self.breadth)

print("Enter details for Rectangle 1:")
l1 = int(input("Enter length: "))
b1 = int(input("Enter breadth: "))

print("\nEnter details for Rectangle 2:")
l2 = int(input("Enter length: "))
b2 = int(input("Enter breadth: "))

r1 = Rectangle(l1, b1)
r2 = Rectangle(l2, b2)

print("\nRectangle 1 : Area =", r1.area(), ", Perimeter =", r1.perimeter())
print("Rectangle 2 : Area =", r2.area(), ", Perimeter =", r2.perimeter())

if r1.area() > r2.area():
    print("\nRectangle 1 has a larger area.")
elif r1.area() < r2.area():
    print("\nRectangle 2 has a larger area.")
else:
    print("\nBoth rectangles have equal area.")