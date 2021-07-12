f=open("sample.log")
x=f.readlines()
count=0
l=[]
res=[]
s=""
for i in x:
    if 'rules violated' in i:
        l.append(i)
for i in l:
    for j in i.split():
        if j.isdigit():
            res.append(j)
for i in res:
    count=count+int(i)
print("rules violated:",count)

