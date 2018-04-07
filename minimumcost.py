a1=list(input())
b=list(input())
d=len(a1)
e=len(b)
i=0
j=0
c=[]
while d>0:
  if a1[i]==b[j]:
    c.append(a1[i])
  j=j+1
  i=i+1
  d=d-1
print(e-len(c))
