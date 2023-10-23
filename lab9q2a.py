count=int(input("enter length of the list: "))
count2=int(input("enter length of the list: "))
l2=[]
l=[]
for i in range(count):
    n=int(input("enter the no.: "))
    l.append(n)
for j in range(count2):
    m=int(input("enter thr no.: "))
    l2.append(m)
a=set(l)
b=set(l2)
print("the list 1 ",l)
print("the list 2 ",l2)
print("set 1",a)
print("set 2",b)