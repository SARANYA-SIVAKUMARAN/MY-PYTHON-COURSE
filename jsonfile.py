import json
# f=open("emp_details.json","r")
with open("emp_details.json") as f:
    data=json.load(f)
    print(data)


