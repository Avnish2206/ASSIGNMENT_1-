def right_angle_triangle(b,p,h):
    if b**2 + p**2 == h**2:
        print("The triangle is a right-angled triangle")
    else:
        print("The triangle is not a right-angled triangle")


b = int(input("Enter the base of the triangle: "))
p = int(input("Enter the perpendicular of the triangle: "))
h = int(input("Enter the hypotenuse of the triangle: "))
right_angle_triangle(b, p, h)