sample=["abc","xy","ab","1221"]
print(sample)
count=0
if int(len(sample[0])>=2) and sample[0][0]==sample[0][-1]:
    count=count+1
if int(len(sample[1])>=2) and sample[1][0]==sample[1][-1]:
    count=count+1
if int(len(sample[2])>=2) and sample[2][0]==sample[2][-1]:
    count=count+1
if int(len(sample[3])>=2) and sample[3][0]==sample[3][-1]:    
    count=count+1
if count==0:
    print("Fisrt and last character are not same from a given list of strings")
print("Result= "+str(count))        