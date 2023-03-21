def greater_3_numbers(a,b,c):
    if a>b and a>c:
        print(str(a)+" is greater") 
    elif b>c and b>a:
        print(str(b)+" is greater")
    elif c>a and c>b:
        print(str(c)+" is greater")
    else:
        print("numbers are equal")   
print("Enter 3 numbers to find greater number :")
numbers=[input(),input(),input()]
greater_3_numbers(numbers[0],numbers[1],numbers[2])
        