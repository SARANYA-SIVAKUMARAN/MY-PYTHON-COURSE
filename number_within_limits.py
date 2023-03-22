def range_of_numbers(a):
    if a!=0 and a<=100:
        print(str(a)+" is between 1 to 100")
    elif a!=0 and a<=1000:
        print(str(a)+" is between 101 to 1000")
    elif a!=0 and a<=2000:
        print(str(a)+" is between 1001 to 2000")  
    else:
        print("The number is zero")                                  
n=int(input("Enter the number: "))
range_of_numbers(n)