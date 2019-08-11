d1={1:'m',2:'s',3:'d'}
d2={4:'D',5:'h',6:'o',7:'n',8:'i'}
d=dict(d1)
d.update(d2)
print(d)
re={**d1,**d2}#** implies that the argument is a dictionary. Using ** [double star] is a shortcut that allows you to pass multiple arguments to a function directly using a dictionary. 
d3=re
print(d3)
