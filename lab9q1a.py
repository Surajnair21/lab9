count=int(input("enter length of the list: "))
l2=[]
l=[]
for i in range(count):
    n=int(input("enter the no.: "))
    l.append(n)
for p in l:
    if p not in l2:
        l2.append(p)
print("the original list",l)
print("the sorted list",l2)