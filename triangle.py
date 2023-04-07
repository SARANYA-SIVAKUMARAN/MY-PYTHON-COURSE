# *
# **
# ***
# ****
# *****

# n=int(input("Enter your triangle size:"))
# i=1
# while i<=n:
#     j=0
#     while j<i:
#         print("*",end="")
#         j+=1
#     print()
#     i+=1     
    
# *****
# ****
# ***
# **
# * 

n=int(input("enter your triangle size: "))
i=0
while i<=n:
    j=n
    while j>i: 
        print("*",end="")
        j-=1
    print()
    i+=1 
          