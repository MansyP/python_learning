l=[12,24,35,24,88,120,155]
for i in range(len(l)):
    if l[i]%5==0 and l[i]%7==0:
        continue
    else:
         print("",l[i],end="")
