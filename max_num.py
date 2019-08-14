a=int(input(""))
i=a
li=[]
count=0
j=0
while i>0:
    rem=int(i%10)
    i=i//10
    count=count+1
    li.insert(j,rem)
    j+=1
for k in range(len(li)):
    b=max(li)
    print(b,end="")
    li.remove(b)
