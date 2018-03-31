def is_isogram(word):
  word=word.lower()
  try:
    if len(word)>0:
      for letter in word:
        if word.count(letter)>1:
          return(word,False)
      retutn(word,True)    
    else:
      retutn('argument',False)
except TypeError as e:
  return "argument should be string:"+str(e)
print is_isogram(" ")
