# import json
# myfile=open("userdetails.json")
# opened_file=json.load(myfile)
# for i in opened_file['user']:
#     print(i)
l=[[4,5,6],[7,8,9],[1,2,3]]
list=[]
i=0
while i<len(l):
    j=0
    k=i
    a=[]
    while j<len(l[i]):
        a.append(l[j][k])
        j=j+1
    list.append(a)
    i=i+1
print(list)



