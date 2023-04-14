import stud_fun

print("Welcome to student manager!!")
while True:
    print("You can perform the following operations : ")

    print("1. Register Student\n2.View student\n3.Update Student\n4.Delete Student\n")

    option=input("Enter your choice: ")
    if option=="1":
        stud_fun.register()
    elif option=="2":
        stud_fun.view_student()
    else:
        print("Invalid choice")
    option1=input("Do you want to continue?(Y/N): ")    
    if option1=="Y":
        continue 
    elif option1=="N":
        print("Thanks for visiting student manager!!")
    else:
        print("invalid choice")
    exit()

