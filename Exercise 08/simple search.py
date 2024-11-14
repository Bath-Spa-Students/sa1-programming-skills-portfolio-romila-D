'''
Exercise 8: Simple Search - 30 Marks
Write a program that searches for a specific string within a list of strings. The list
is initialized with specific names (“Jake” “Zac”, “Ian”, “Ron”, “Sam”, “Dave”).
, and your task is to search for “Sam”.
'''

# names list
names = ["Jake", "Zac", "Ian", "Ron", "Sam", "Dave"]
#searching sam in  list(names) 
print("Names in the list :")
print("Names:", names)
search = "Sam"
#using if else statment
if search in names:
    print(f"'{search}' found in the list.")
else:
    print(f"'{search}' not found in the list.")
