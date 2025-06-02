#first day code of leapfrog challenge
print("hello world!!")


#variables


Name="sandesh khadkda"
age=19
Profession="student"
Status="single"
isMarried=False
print(Name,'\n',age,'\n',Profession,'\n',Status,'\n',isMarried)


a,b,c=1,2,3
print(a)
print(b)
print(c)

#type conversion
x=123
y=1.23
s=x+y
print(s)#implict conversion

str="12"
num=12
print(type(str))
str=int(str)
sum=str+num
print(sum)#explicit conversion


#outputs
print('Good',end='')
print('morning')

print('hey',5,'sandesh',sep='-')

print("sandesh"+"khadka")

#inputs
x=int(input("enter number"))
print("entered number:",x)

 #operators
a=2**3 
print(a)#8

print(3==4)

xi=[1,2,3]
yi=[1,2,3]
print(xi is yi)#false as they are not identical (either eqal)

#datatypes
integer=1234
floatnbr=1.23
print(integer+floatnbr)#typeconversion into float
print(0xFB+0b10)#conversion of hexa to deci and binary to deci

#python random module
import random
list1=[1,2,3,4,5,6,7,8,9]
print(random.choice(list1))
random.shuffle(list1)
print(list1)
print(random.random())#print random element

#python mathematics
import math
radius = 5
areaCircle = math.pi * radius * radius
print(round(areaCircle, 2))#rounding upto2 digits after the decimal
print(f"{areaCircle:.2f}")#recomended in mordern python




#project for the day:
#simple calculator
X=int(input("enter first num:"))
Y=int(input("enter second num:"))
print("sum:",X+Y)
print("sub:",X-Y)
print("mul:",X*Y)
print("div:",X/Y)

#swap two number:
print("before swapping:")
numb1=1
numb2=2
print(numb1,numb2)
swap=numb1
numb1=numb2
numb2=swap
print("after swapping:")
print(numb1,numb2)





