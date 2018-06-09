n1=int(input("enter n1"))
l1=[]
l2=[]
c=0
for i in range(n1):
  a=int(input("enter your elements"))
  l1.append(a)
for i in range(n1):
  if (i%2!=0 and l1[i]%2==0) or (i%2==0 and l1[i]%2!=0):
    l2.append(l1[i])
    c=c+1
	
print(c)
