#exception handeling and file io
#practice:exception handeling
#practice 1:
try:
    num=int(input("enter the number :"))
    num2=int(input("enter the second number:"))
    div=num/num2
    print("the result is:",div)
except ValueError:
    print("the number you provided is zero")

finally:
    print("--------------------------------------")


#practice 2:
try:
    integer=int(input("enter number"))
    print("the number you have entered is:",integer)
except ValueError:
    print("please enter integer")
finally:
    print("-----------------------------------------")#this is cleanup message it runs without scanning any error

#practice:file io
with open ("example.txt","w") as file:
    file.write("hello world!")

with open("example.txt","r") as file:
    content=file.read()
    print("the content in a file is:",content)

with open("example.txt","a") as file:
    file.write("i am appended content")



with open("example.txt","r") as file:
    content=file.read()
    print("the content in a file after appending is :",content)
