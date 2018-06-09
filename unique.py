n1=int(input("enter n1"))
l=[]
l1=[]
b=0
for i in range(n1):
    a=int(input())
    l.append(a)
for i in range(n1):
    b=l.count(l[i])
    if b==2:
        l1.append(l[i])
        break
l1.sort()
s=set(l1)
if len(s)!=0:
    print(s)
else:
    print("unique")
