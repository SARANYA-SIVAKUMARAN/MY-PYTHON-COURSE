# *****
#  ****
#   ***
#    **
#     *

n=int(input("Enter your triangle size: "))
i=0
while i<n:
    s=0
    j=n
    while s<i:
        print(" ",end="")
        s+=1
    while j>i:
        print("*",end="")
        j-=1 
    print()     
    i+=1