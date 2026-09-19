a = int(input("Enter your first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter your third number: "))
if a>b and a>c:
    print("a is the greatest number")
elif b>a and b>c:
    print("b is the greatest number")
elif c>a and c>b:
    print("c is the greatest number")
elif a==b and b>c:
    print("a and b are the greatest")
elif a==c and c>b:
    print("a and c are the greatest")
elif c==b and b>a:
    print("c and b are the greatest")
else:
    print(" a b and c are equal and greatest")