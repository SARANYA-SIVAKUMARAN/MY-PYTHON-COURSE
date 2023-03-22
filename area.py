def rectangle(length,breadth):
    area=length*breadth
    print("Area of Rectangle is "+str(area))
def square(length,breadth):
    area=length*breadth
    print("Area of square is "+str(area)) 
l=int(input("Enter length: "))
b=int(input("Enter breadth: "))
if l==b:
    print("This is square")
    square(l,b)
else:    
    rectangle(l,b)