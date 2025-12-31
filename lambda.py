calculate_square_area = lambda side_length: side_length ** 2
calculate_rectangle_area = lambda length, width: length * width
calculate_triangle_area = lambda base, height: 0.5 * base * height

sqs = int(input("Enter the side of square: "))
print("Enter the base and height of triangle:")
bs = int(input("Base: "))
ht = int(input("Height: "))

print("Enter the length and breadth of rectangle:")
l = int(input("Length: "))
b = int(input("Breadth: "))

square_area = calculate_square_area(sqs)
print("Area of the square:", square_area)

triangle_area = calculate_triangle_area(bs, ht)
print("Area of the triangle:", triangle_area)

rectangle_area = calculate_rectangle_area(l, b)
print("Area of the rectangle:", rectangle_area)
