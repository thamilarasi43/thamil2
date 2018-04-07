a1=list(input())
b=list(input())
c=len(a1)
d=0
i=0
while c>0:
    d=d+(ord(b[i])-ord(a1[i]))
    i=i+1
    c=c-1
print(d)
