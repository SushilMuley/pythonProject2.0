side1=float(input("Enter the side1 number\n"))
side2=float(input("Enter the side2 number\n"))
side3=float(input("Enter the side3 number\n"))
if side1==side2==side3:
    print("Equivalance")
elif side1==side2 or side2==side3 or side1==side3:
    print("Isoalator")
else:
    print("Scalene")