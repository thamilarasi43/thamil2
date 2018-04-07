def zero():
	N1=int(input())
	l=[]
	for i in range(N1):
		l.append(int(input()))
	for i in range(N1):
		for j in range(i+1,N1):
			if l[i]+l[j]==0 :
				print(l[i],l[j])
try:
	zero()
except:
	print('invalid')
