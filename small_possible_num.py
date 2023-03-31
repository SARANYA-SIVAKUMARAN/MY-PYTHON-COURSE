list_1=[3,40,41,43,74,9]
print(list_1)
count=len(list_1)
i=0
list_2=[]
while i<count:
    tem_length=len(str(list_1[i]))
    j=0
    while j<tem_length:
        list_2.append(int(str(list_1[i])[j]))
        j+=1  
    i+=1
list_2.sort()
# print(list_2)
print("smallest possiblle number is:",end="")
length=len(list_2)
i=0
while i<length:
    print(list_2[i],end="")
    i+=1
# name="40"
# length=len(name)  
# i=0
# while i<length:
#     print(name[i])
#     i+=1