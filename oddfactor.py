import math
def sumofoddFactors( n1 ):
     res = 1
     while n1 % 2 == 0:
        n1 = n1 // 2
     for i in range(3, int(math.sqrt(n1) + 1)):
        count = 0
        curr_sum = 1
        curr_term = 1
        while n1 % i == 0:
            count+=1
             
            n1 = n1 // i
            curr_term *= i
            curr_sum += curr_term
         
        res *= curr_sum
     if n1 >= 2:
        res *= (1 + n1)
     return res
n1 = 30
print(sumofoddFactors(n1))
 
