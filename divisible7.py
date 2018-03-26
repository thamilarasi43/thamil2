def isDivisibleBy7(num1) :
     
   
    if num1 < 0 :
        return isDivisibleBy7( -num1 )
 
   
    if( num1 == 0 or num1 == 7 ) :
        return True
     
    if( num1 < 10 ) :
        return False
         
   
    return isDivisibleBy7( num1 / 10 - 2 * ( num1 - num1 / 10 * 10 ) )
     

num1 = 616
if(isDivisibleBy7(num1)) :
    print ("Divisible")
else :
    print ("Not Divisible")
