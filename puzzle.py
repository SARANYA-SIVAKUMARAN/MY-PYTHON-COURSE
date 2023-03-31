print("welcome to puzzle!!")
print("Puzzle: 5+2= ")

i=0
while i<3:
    ans=input("Answer: ")
    if ans=="7":
        print("You are won!!")
        exit()
    if i==0:
        print("clue 1: The answer between 1 t0 10")   
    elif i==1:
        print("clue2:The answer between 1 to 7 ") 
    i+=1    
        
print("you are a looser!!")
           