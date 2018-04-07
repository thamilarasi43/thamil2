from string import ascii_lowercase as asc_lower
def check(s):
    return set(asc_lower) - set(s.lower()) == set([])
str=input("Enter string:")
if(check(str)==True):
      print("The string is a pangram")
else:
      print("The string isn't a pangram")
