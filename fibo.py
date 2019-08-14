a=int(input(""))
f1=0
f2=1
i=0
print(f1,end="")
print(",",f2,end="")
while i<(a-1):
    f=f1+f2
    f1=f2
    f2=f
    i+=1
    print(",",f,end="")
