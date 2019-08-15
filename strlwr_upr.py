a=str(input())
li=list(a)
l=[]
for i in li:
    if i.islower()==True:
        i=i.upper()
        l.append(i)
    else:
        i=i.lower()
        l.append(i)
for i in l:
    print(i,end="")
    
