import areacalc_fun
print("Welcome To My Area Calculator!!")
print("choose shape to find area")
print("1. rectangle\n2. square\n3. circle\n4. triangle")
choice=input("Enter your choice[1,2,3,4] : ")
if choice=="1":
    length=int(input("Enter length of rectangle:"))
    breadth=int(input("Enter height of rectangle:"))
    print("area of rectangle = "+str(areacalc_fun.rectangle(length,breadth)))
elif choice=="2":
    length=int(input("Enter length of square:"))
    print("area of square= "+str(areacalc_fun.square(length)) )
elif choice=="3":
    radius=int(input("Enter radius of circle:"))
    print("area of circle = "+str(areacalc_fun.circle(radius)))
elif choice=="4":
    length=int(input("Enter height of triangle:"))
    height=int(input("Enter height oif triangle:"))
    print("area of triangle = "+str(areacalc_fun.triangle(length,height)))
else:
    print("invalid choice")          
    