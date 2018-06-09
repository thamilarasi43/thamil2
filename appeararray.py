k1=int(input())
n=[]
n1=[]
for i in range(k1):
    a=int(input())
    n.append(a)
for i in range(k1):
    b=int(input())
    n1.append(b)
s=set(n)
s1=set(n1)
print(s&s1)
