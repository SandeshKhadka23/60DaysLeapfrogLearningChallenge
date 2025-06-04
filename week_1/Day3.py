# Day 3: Loops in Python

# for loop to print 1 to 5
for i in range(1, 6):
    print("For Loop:", i)

# while loop to print 1 to 5
count = 1
while count <= 5:
    print("While Loop:", count)
    count += 1

# break statement
for i in range(10):
    if i == 3:
        break
    print("Break at:", i)

# continue statement
for i in range(5):
    if i == 2:
        continue
    print("Continue skips 2:", i)

# pass statement
for i in range(3):
    pass  # Placeholder
