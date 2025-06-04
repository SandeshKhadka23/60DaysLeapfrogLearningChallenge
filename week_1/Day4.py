#practice for lists,tuples,set and dictionaries

#practice 1:Student Grade storage system using Dictionary

students = [
    {"Name": "Sandesh Khadka", "Grade": "A"},
    {"Name": "Ramesh Hamal", "Grade": "A+"},
    {"Name": "Rama Shrestha", "Grade": "B+"},
    {"Name": "Hari Gopal", "Grade": "A-"},
    {"Name": "Alexender", "Grade": "A+"},
    {"Name": "Shyam Sunder Lal Bahadur Gharti", "Grade": "A"},
    {"Name": "Sita Naran", "Grade": "C+"}
]

#adding new data:
students.append({"Name":"apple singh","Grade":"B+"})
#removing the existing one
students.pop(1)
#editing existing one
students[2]={"Name":"banana"}

print("Students grade Information:")
for s in students:
    print(s)


#practice -2:
#simple contact Book using dictionary
Contacts=[{"Name":"Sandesh Khadka","Phone_no":102},
          {"Name":"Hari","Phone_no":456},
           {"Name":"Sita","Phone_no":789},
            {"Name":"Ram","Phone_no":1011},
             {"Name":"Shyam","Phone_no":1213},
              {"Name":"Ravi","Phone_no":1415},
               {"Name":"Rabi","Phone_no":1617},
                {"Name":"Science","Phone_no":1819},
          
         
]
#asking from users
isnew=input("do you want to add new contact?(Y for yes and N for no)")
if isnew.lower() == 'y':
    uName= input("enter name:")
    uContact=input("enter contact number:")
    Contacts.append({"Name":uName,"Phone_no":uContact})

else:
    print("thank you!!")


for c in Contacts:
    print(c)

#practice :3:
#create a set of unique course name from a list

course=["python","AI","java","JavaScript","python"]#list
unique_course=set(course)#removes duplicates
print('unique courses from lists are:')
print(unique_course)

#practice :4
#for tuples
numbers=(1,2,3,4,5,6,7,8,9)
numbers[-1]#last value
numbers[0]#first value
number=(10,11)

combined=numbers+number
print("combined tuple:",combined)

#tuples unpacking
student = ("Ram", "A+", 18)
name, grade, age = student
print(f"Student {name} got {grade} and is {age} years old.")

#nested tuples
students = (("Ram", "A"), ("Sita", "B+"), ("Hari", "A-"))
for student in students:
    print(f"Name: {student[0]}, Grade: {student[1]}")
