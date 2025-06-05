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

fac=checkfac(5)#practice for the loops and functions in python
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
print("the factorial of given number is:",fac)

#practice 3:menu-driven calculator using functions
def sum(num1,num2):
    sum=num1+num2
    return sum
def sub(num1,num2):
    sub=num1-num2
    return sub
def div(num1,num2):
    div=num1/num2
    return div
def mul(num1,num2):
    if(num2 !=0):

      mul=num1*num2
      return mul
    else:
        print("can't divide by 0")
     
while True:

   print("1.+")
   print("2.-")
   print("3./")
   print("4.*")
   print("5.exit")
   choice=int(input( "enter your choice:"))

   if choice == 5:
    exit(0)

   num1=int(input("enter first number:"))
   num2=int(input("enter second number:"))

   if choice == 1:
       sum=sum(num1,num2)
       print("sum:",sum)
       break
   elif choice == 2:
       sub=sub(num1,num2)
       print("sub:",sub)
       break
   elif choice == 3:
       div=div(num1,num2)
       print("div:",div)
       break
   elif choice == 4:
       mul=mul(num1,num2)
       print("mul:",mul)
       break
   else :
       print("enter valid choice")

    
       
#practice 4:function that reverses a string
def reverse(string):
    return string[::-1]  # This is a simple and Pythonic way to reverse a string

string = input("Enter a string to reverse: ")

def count_alphabets(string):
    count = 0
    for char in string:
        if char.isalpha():
            count += 1
    return count

rev = reverse(string)
print("The reversed string is:", rev)

coun = count_alphabets(string)
print("The number of alphabets in the string is:", coun)
