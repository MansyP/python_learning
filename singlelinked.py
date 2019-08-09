class Ab:
   def __init__(self,data):
    self.data=data
    self.nextt=None
class Sll:
    def __init__(self):
        self.head=None
    def ins_beg(self,data):
        temp=Ab(data)
        temp.nextt=self.head
        self.head=temp
    def del_beg(self):
        temp=self.head
        self.head=self.head.nextt
        temp.nextt=None
    def display(self):
        temp=self.head
        while temp!=None:
            print(temp.data,"==>",end='')
            temp=temp.nextt
        print("None")
obj=Sll()
a=0
while a!=4:
    print("1.insert 2.delete 3.display 4.exit")
    a=int(input(""))
    if a==1:
        b=int(input(""))
        obj.ins_beg(b)
    elif a==2:
        obj.del_beg()
    elif a==3:
        obj.display()
    elif a==4:
        print("exit")
    
        
        
        
        
        

        
        


    
