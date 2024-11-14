'''
Exercise 8: Simple Search - 30 Marks
Write a program that searches for a specific string within a list of strings. The list
is initialized with specific names (“Jake” “Zac”, “Ian”, “Ron”, “Sam”, “Dave”).
, and your task is to search for “Sam”.
Optional Requirements:
1. Allow the user to input the search term instead of using a predefined value.
2. Implement the search functionality based on user input.
'''
#this program in case sensitive as required in the assingment

# creating list of names
names = ["Jake", "Zac", "Ian", "Ron", "Sam", "Dave"]
#taking input from the user
name = input("Enter your name to search: ")
#using if elif else statement
#assining if statemnet
if name in names:
    print(f"'{name}' found in the list.")
#assining elif statment
elif name == "":
    print("Please enter a valid name.")
#assining else statment
else:
    print(f"'{name}' not found in the list.")