# # #   *
# # #  ***
# # # *****     

n=int(input("Enter your triangle size: "))
i=0
if n%2==0:
  k=2
else:
  k=1 
j=n/2   
while i<n:
  s=0
  while s<j:
    print(" ",end="")
    s+=1
  l=0  
  while l<k:
    print("*",end="")
    l+=1
  print()
  k+=2
  j-=1
  i+=2
# try:
#   n=int(input("Enter your triangle size: "))
# except:
#   print("invalid input !")
#   print("we are assigning standard value of 5")
#   n=5
# i=n//2
# if n%2==0:
#   k=2 
# else:
#   k=1  
# for line in range(0,n,2):
#     for space in range(i):
#       print(" ",end="")
#     i-=1  
#     for star in range(k):
#       print("*",end="")
#     k+=2
#     print()
    
# n=int(input("Enter your triangle size: ")) 
# i=n//2
# if n%2==0:
#   k=2 
# else:
#   k=1  
# for line in range(0,n,2):
#   for star in range(k):
#     print("*",end="")
#   k+=2
#   for space in range(i):
#    print(" ",end="")
#   i-=1  
#   print()