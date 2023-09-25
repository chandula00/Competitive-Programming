import math


def isPrime(n):
    if n<=1:
        return False
    if n<=3:
        return True
    
    if(n%2==0 or n%3==0):
        return False
    
    else:
        
        for i in range(5,int(math.sqrt(n))):
            if(n%i ==0 or n%(i+2)==0):
                return False
            i=i+6
        return True