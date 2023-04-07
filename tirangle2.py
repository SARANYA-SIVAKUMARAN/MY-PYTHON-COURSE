#     *
#    **
#   ***
#  ****
# *****              

n=int(input("Enter your triangle size: "))
i=1
while i<=n:
    s=0
    j=0
    while s<n-i:
        print(" ",end="")
        s+=1
    while j<i:
        print("*",end="")
        j+=1
    print()    
    i+=1