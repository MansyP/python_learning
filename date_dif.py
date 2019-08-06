import datetime
def dte():
    y=int(input("year:"))
    m=int(input("month:"))
    d=int(input("date:"))
    dat=datetime.date(y,m,d)
    return dat
print("enter the first date")
fd=dte()
print("enter the second date")
ld=dte()
dif=abs(ld-fd)
print(dif.days)
