# sample=["aba","xy","ab","1221"]
# print(sample)
# count=0
# if len(sample[0])>=2 and sample[0][0]==sample[0][-1]:
#     count=count+1
# if len(sample[1])>=2 and sample[1][0]==sample[1][-1]:
#     count=count+1
# if len(sample[2])>=2 and sample[2][0]==sample[2][-1]:
#     count=count+1
# if len(sample[3])>=2 and sample[3][0]==sample[3][-1]:    
#     count=count+1
# if count==0:
#     print("Fisrt and last character are not same from a given list of strings")
# print("Result= "+str(count))  

sample=["aba","1221","xy","ab","sdf"]
length=len(sample)
count=0
i=0
while i<length:
    if len(sample[i])>2 and sample[i][0]==sample[i][-1]:
        count+=1 
    i+=1
print(count)               