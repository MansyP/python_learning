l1=[1,3,6,78,35,55]
l2=[12,24,35,24,88,120,155]
s=set(l1)
p=set(l2)
for i in l1:
    if i in l2:
        print("",i,end="")
