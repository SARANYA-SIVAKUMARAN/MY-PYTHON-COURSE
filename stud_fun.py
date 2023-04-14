import json
from tabulate import tabulate
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
    try:
        f=open("stud_data.json","r")
    except FileNotFoundError as error:
        f=open("stud_data.json","w")  
        initial_data={"stud_data":[]}
        json.dump(initial_data,f,indent=4)
        f.close()  
        f=open("stud_data.json","r") 
    stud=json.load(f)
    stud["stud_data"].append(tem_dict)
    f.close()
    f=open("stud_data.json","w")
    json.dump(stud,f,indent=4)
    f.close()
    print("Register Sucessfully!")
    
def view_student():
    f=open("stud_data.json","r")
    view=json.load(f)
    f.close()
    # print("NAME\t"+"AGE\t"+"ADD\t"+"COURSE" )
    sno=1
    table=[["S.NO","NAME","AGE","ADDRESS","COURSE"]]
    for table1 in view["stud_data"]:
        # print(f"{table['name']}\t{table['age']}\t{table['add']}\t\t{table['course']}") 
        tmp_list=[sno,table1['name'],table1['age'],table1['add'],table1['course']]
        table.append(tmp_list)
        sno+=1    
    print(tabulate(table,headers="firstrow"))
    
def update_student():
    f=open("stud_data.json","r+")
    update=json.load(f)
    f.close()
        
    