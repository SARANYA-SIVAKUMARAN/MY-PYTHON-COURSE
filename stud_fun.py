import json
from tabulate import tabulate
def read_file():
    f=open("stud_data.json","r")
    data=json.load(f)
    f.close()
    return data
    
def write_file(stud_data):
    f=open("stud_data.json","w")
    json.dump(stud_data,f,indent=4)
    f.close()   
     
def register():
    print("Welcome to Registration Module!!")
    name=input("Enter your name: ")
    age=input("Enter your age: ")
    add=input("Enter your address: ")
    course=input("Enter your course: ")
    tem_dict={
        "name":name,
        "age":age,
        "add":add,
        "course":course
    }
    data=read_file()  
    data["stud_data"].append(tem_dict)
    write_file(data)
    print("Register Sucessfully!")
    
def view_student():
    view=read_file()
    sno=1
    table=[["S.NO","NAME","AGE","ADDRESS","COURSE"]]
    for table1 in view["stud_data"]:
    #     # print(f"{table['name']}\t{table['age']}\t{table['add']}\t\t{table['course']}") 
        tmp_list=[sno,table1['name'],table1['age'],table1['add'],table1['course']]
        table.append(tmp_list)
        sno+=1    
    print(tabulate(table,headers="firstrow"))
    
def update_student():
    view_student()
    update_student =read_file()
    update_stud=input("Enter the serial number of student for updation : ")
    choice=input("1.Name\t2.Age\t3.Address\t4.Course\t5.All\nWhat you want to update : ")
    sno=1
    for update in update_student['stud_data']:
        if str(sno)==update_stud:
            if choice=="1":
                name=input("enter updated name : ")
                update['name']=name
                print("Updated Sucessfully")
            elif choice=="2":
                age=input("enter updated age : ")
                update['age']=age
                print("Updated Sucessfully")
            elif choice=="3":
                add=input("enter updated address : ")
                update['add']=add
                print("Updated Sucessfully")
            elif choice=="4":
                course=input("enter updated course : ")
                update['course']=course
                print("Updated Sucessfully")
            elif choice=="5":
                name=input("enter updated name : ")
                update['name']=name
                age=input("enter updated age : ")
                update['age']=age  
                add=input("enter updated address : ")
                update['add']=add
                course=input("enter updated course : ")
                update['course']=course
                print("Updated Sucessfully")
                
            else:
                print("invalid choice")
                break    
        sno+=1  
    write_file(update_student)  
    
def delete_student():
    delete_student=read_file()
    view_student()
    choice=input("Enter the serial number of student you want to delete : ")
    sno=1
    for delete in delete_student['stud_data']:
        if str(sno)==choice:
            delete_student['stud_data'].remove(delete)
            print("Deleted Sucessfully")
        sno+=1
    write_file(delete_student)                 
    