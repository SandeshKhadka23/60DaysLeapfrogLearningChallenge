# #today i will be learning about if else elif etc
# #practice
# #1.
# #suppose there are 6 subjects and we are calculating grade in aggregate
#grade checker
Applied_Math=int(input("enter marks in applied math:"))
Java=int(input("enter marks in java:"))
ComputerArchitecture=int(input("enter marks in computer architecture:"))
Toc=int(input("enter marks in applied toc:"))
NM=int(input("enter marks in applied nm:"))
researchfundamental=int(input("enter marks in research fundamental:"))

total_marks=(Applied_Math+Java+ComputerArchitecture+Toc+NM+researchfundamental)/600
percentage=total_marks*100


# #control flow
if percentage>=90:
    print("Grade:A")
elif percentage>=85 and percentage<90:
    print("Grade:A-")
elif percentage>=80 and percentage<85:
    print("Grade:B+")
elif percentage>=75 and percentage<80:
    print("Grade:B")
elif percentage>=70 and percentage<75:
    print("Grade:B-")
elif percentage>=65 and percentage<70:
    print("Grade:C+")
elif percentage>=60 and percentage<65:
    print("Grade:C")
elif percentage>=55 and percentage<60:
    print("Grade:C-")
else:
    print("Failed")


# #practice_2:
num=int(input("enter number to check even or odd:"))

if num%2==0 and num>0:
    print("the number ",num," is even")
else:
    print("the number :",num," is odd")

# #practice 3:
if num>0:
    print("the given number is positive")
else:
    print("the number is negative")


# #mini_challenge:number guessing game
min=1
max=20
import random
computerGuess=random.randrange(min,max)



# #user's guess

def guess():
     uGuess = int(input("enter number to guess:"))
    
     if uGuess==computerGuess:
        print("congratulations!!,you have guessed it right.")
        print("The number was:",computerGuess)
     else:
        print("your guess is wrong:(,Try again")
        guess()

guess()