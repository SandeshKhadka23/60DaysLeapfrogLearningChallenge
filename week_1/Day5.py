#practice for the loops and functions in python
#practice 1:check if a number is prime
def check(number):
    count=0
    for i in range(1,number+1):#if +1 is not given it treats as tuple and only iterates over two values
        if number%i == 0:
            count +=1
    
    if count == 2 :
        print(f"the {number} is prime")
    else :
        print("the number is not prime")

check(10);

#practice 2:function to calculate factorial using loop
def checkfac(number):
   factorial=1
   for i in range(1,number+1):
       factorial=factorial*i

   return factorial  

fac=checkfac(5)
print("the factorial of given number is:",fac)