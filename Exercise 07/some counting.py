'''
Exercise 7: Some Counting - 20 Marks
Use your newly acquired knowledge of the for loop to complete the following
tasks. Print all values to the console in each case. * Write a loop that counts
up from 0 to 50 in increments of 1. * Write a loop that counts down from 50 to
0 in decrements of 1. * Write a loop that counts up from 30 to 50 in increments
of 1. * Write a loop that counts down from 50 to 10 in decrements of 2. * Write
a loop that counts up from 100 to 200 in increments of 5. You may include all
loops in a single project
'''
#1st loop Count from 0 to 50 with increments of 1
print("1st loop counting from 0 to 50")
for i in range(51):
    print(i)

#2nd loop count down from 50 to 0 with decrements of 1
# using \n to break line
print("\n2nd loop counting  from 50 to 0")
for i in range(50, -1, -1):
    print(i)

#3rd loop count  from 30 to 50 with increments of 1
print("\n3rd loop counting  from 30 to 50")
for i in range(30, 51):
    print(i)

#4rth loop count from 50 to 10 with decrements of 2
print("\n4rth loop counting  from 50 to 10")
for i in range(50, 9, -2):
    print(i)

#5th loop count from 100 to 200 with increments of 5
print("\n5th loop counting  from 100 to 200")
for i in range(100, 201, 5):
    print(i)
