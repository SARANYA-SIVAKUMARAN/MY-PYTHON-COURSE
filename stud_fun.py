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
    
# def update_student():
    
        
    