def main():
	n1=int(input())
	l=[]
	for i in range(n1):
		l.append(int(input()))
	l.sort(reverse=True)
	for i in l:
		print(i)
try:
  main()
except:
  print('invalid')
