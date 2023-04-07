# *****
#  ***
#   * 

n=int(input("Enter your triangle size: "))
i=0
s=0
for line in range(0,n,2):
    for space in range(s):
        print(" ",end="") 
    for star in range(n-line):
        print("*",end="")
    s+=1    
    print()    

