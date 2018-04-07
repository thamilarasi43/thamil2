def zero():
	N=int(input())
	l=[]
	for i in range(N):
		l.append(int(input()))
	for i in range(N):
		for j in range(i+1,N):
			if l[i]+l[j]==0 :
				print(l[i],l[j])
try:
	zero()
except:
	print('invalid')
