import itertools
print(list(itertools.permutations([1,2,3])))

def permutation(lst): 
     if len(lst)==0: 
        return [] 
     if len(lst)==1:
        return [lst]  
     l = [] 
     for i in range(len(lst)):
            m = lst[i]
            remLst = lst[:i] + lst[i+1:]
            for p in permutation(remLst):
                l.append([m] + p)         
     return l    
data = list('123') 
for p in permutation(data):
    print(p) 

