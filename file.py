f=open("text.txt","w")
user="saran"
password="1234"
line=user+":"+password
f.write(line)
f.close()
with open("text.txt","w") as f:
    f.write("test")
print("test")    