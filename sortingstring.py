my_str1 = input("Enter a string: ")
words = my_str1.split()
words.sort()
print("The sorted words are:")
for word in words:
   print(word)
