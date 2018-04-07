str1 = "Computers are useless. They can only give you answers"  
dic = {}  
for char in str1:  
   dic[char] = 0  
for char in str1:  
    dic[char]+= 1  
for char, count in dic.items():  
       if count > 1 and char != ' ':  
         print("%c is repeated %d times" % (char, count))  
