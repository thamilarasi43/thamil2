a1=input("\nEnter the N number")
b=input("\nEnter the K number")
c=list(str(a1))
e=b
while e>0:
    e=e-1
    del(c[e])
print(''.join(c))
