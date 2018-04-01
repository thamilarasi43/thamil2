num=int(input("enter any number:"))
if num>1:
  for i in range(2,num):
    if(num%i)==0:
      print(num,"is not a prime number")
      break
  else:
    print(num,"is a prime number")
elif num==0 or 1:
  print(num,"is a neither prime nor composite number")
else:
  print(num,"is not a prime number it is a composite number")
      
      
