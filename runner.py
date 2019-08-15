#importing module
import man
m=max(man.li)
if man.li.count(m)!=1:
    while man.li.count(m)!=0:
        man.li.remove(m)
else:
    man.li.remove(m)
print(max(man.li))
