a = int(input("Enter side A of the triangle: "))
b = int(input("Enter side B of the triangle: "))
c = int(input("Enter side C of the triangle: "))
if a + b < c or a + c < b or b + c < a:
    print("Triangle cannot exist with such sizes")
else:
    if a == b and a == c and b == c:
        print('Equilateral triangle')
    elif a == b or a == c or b == c:
        print('Isosceles triangle')
    elif a != b and a != c and b != c:
        print('Scalene triangle')