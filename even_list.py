n = int(input("Enter number of elements : "))
lst=[]
count=0
for i in range(0, n): 
    ele = int(input()) 
    lst.append(ele) 
for i in lst:
    if i%2!=0:
        count=1
        break
print("NO")if count==1  else print("YES")
