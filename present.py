n1=int(input("enter n1"))
l=[]
l1=[]
for i in range(n1):
    a=int(input())
    l.append(a)
for i in range(n1):
    if (i%2!=0 and l[i]%2==0) or (i%2==0 and l[i]%2!=0):
        l1.append(l[i])
print(l1)
© 2018 GitHub, Inc.
