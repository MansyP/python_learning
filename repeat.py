tu=tuple(input("")).split("")
li=list(tu)
lis=li
for i in lis: 
    if tu.count(i)!=1:
        print("",i,end="")
        lis=lis.remove(i)
