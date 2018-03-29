def is_multiple(x,y):
  return x and (y%x)==0
x=int(input("enter a number:"))
y=int(input("enter its multilpe:"))
if is_multiple(x,y):
  print("true")
else:
  print("false")
  
