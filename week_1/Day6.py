#map()and filter()
#practice of map:
def add(n):
    return n+10

numbers=[1,2,3,4,5]
addednbr=list(map(add,numbers))
print("the numbers in a list after adding 10:",addednbr)

#using lambda:
addnbr=list(map(lambda n:n+10,numbers))
print("using lambda:",addnbr)

#practice for filter:
def check(n):
    return n>12

filternbr=list(filter(check,addednbr))
print("the number after filtering:",filternbr)

#using lambda:
filtnbr=list(filter(lambda n:n>12,addednbr))
print("using lambda:",filtnbr)