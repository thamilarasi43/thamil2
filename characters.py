a1=raw_input()
for c in range (0,a1):
if(any(c.isalpha for c in a1) and any(c.isdigit for c in a1)):
    print("YES")
else:
    print("nO")
