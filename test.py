# original_list=["Red color","orange#","Green","Orange@","White"]
# character=["#","color","@"]
# new_list=["Red","orange","Green","White"]

# print("Remove Words")
# original_list=["Red color","orange#","Green","Orange@","White"]
# new_list=[]
# character=["#","color","@"]
# for ele in original_list:
#     temp_word=""
#     for char in ele:
#         if char==" ":
            
#         temp_word=temp_word+char

print("Remove Words")
original_list=["Red color","orange#","Green","Orange@","White"]
new_list=[]
character=["#","color","@"]
i=0
for ele in original_list:
    for char in character:
        if char in ele:
            i=1
            print(ele,char)
            new_list.append(ele.replace(char,""))
    if i==0:
        new_list.append(ele)
    i=0           
print(new_list)            
while char==ele[i]:
    character.remove(char)
    i+=1    
    

    
    