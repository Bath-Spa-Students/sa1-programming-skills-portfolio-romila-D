'''
Exercise 4: Primitive Quiz - 30 Marks
In this exercise, you’ll create a simple program that asks the user a question,
evaluates their answer, and provides feedback.
Steps:
1. Write a program that asks the user “What is the capital of France?” and
waits for their response.
2. If the user’s answer is correct (i.e., “Paris”), the program should print a
message saying the answer is correct.
3. If the answer is incorrect, the program should print a message saying the
answer is wrong.
Advanced Requirements:
Ignore Capitalization: Modify your program to accept answers regardless of
the capitalization (e.g., “paris”, “Paris”, and “PaRis” should all be considered
correct). Multiple Questions: Extend the program into a quiz that asks for the
capitals of 10 European countries. Provide feedback for each question.
'''
#1st country
#giving user space to input
france = str (input("What is the capital of France? "))
# assining if statemnet
if france .strip().lower() == "paris":
    print ('your answer in correct.')
#assining else statement
else:
    print ('your answer in wrong !\n The Capital Of France is Paris.') 

#2nd country
#giving user space to input
austria = str (input("What is the capital of Austria? "))
# assining if statemnet
if austria .strip().lower() == "vienna":
    print ('your answer in correct.')
#assining else statement
else:
    print ('your answer in wrong !\n The Capital Of Austria is vienna.') 


#3rd country
#giving user space to input
italy = str (input("What is the capital of Italy? "))
# assining if statemnet
if italy .strip().lower() == "rome":
    print ('your answer in correct.')
#assining else statement
else:
    print ('your answer in wrong !\n The Capital Of Italy is rome.') 

#4rth country
#giving user space to input
Monaco = str (input("What is the capital of Monaco? "))
# assining if statemnet
if Monaco .strip().lower() == "monaco":
    print ('your answer in correct.')
#assining else statement
else:
    print ('your answer in wrong !\n The Capital Of Monaco is Monaco.') 

#5th country
#giving user space to input
Portugal = str (input("What is the capital of Portugal? "))
# assining if statemnet
if Portugal .strip().lower() == "lisbon":
    print ('your answer in correct.')
#assining else statement
else:
    print ('your answer in wrong !\n The Capital Of Portugal is lisbon.') 

#6th country
#giving user space to input
Russia = str (input("What is the capital of Russia ? "))
# assining if statemnet
if Russia .strip().lower() == "moscow":
    print ('your answer in correct.')
#assining else statement
else:
    print ('your answer in wrong !\n The Capital Of Russia is Moscow.') 

#7th country
#giving user space to input
Spain = str (input("What is the capital of Spain? "))
# assining if statemnet
if Spain .strip().lower() == "madrid":
    print ('your answer in correct.')
#assining else statement
else:
    print ('your answer in wrong !\n The Capital Of Spain is Madrid.') 

#8th country
#giving user space to input
United_Kingdom = str (input("What is the capital of United Kingdom? "))
# assining if statemnet
if United_Kingdom .strip().lower() == "london":
    print ('your answer in correct.')
#assining else statement
else:
    print ('your answer in wrong !\n The Capital Of United Kingdom is London.') 

#9th country
#giving user space to input
Switzerland = str (input("What is the capital of Switzerland? "))
# assining if statemnet
if Switzerland .strip().lower() == "bern":
    print ('your answer in correct.')
#assining else statement
else:
    print ('your answer in wrong !\n The Capital Of Switzerland is Bern.') 

#10th country
#giving user space to input
Turkey = str (input("What is the capital of Turkey? "))
# assining if statemnet
if Turkey .strip().lower() == "ankara":
    print ('your answer in correct.')
#assining else statement
else:
    print ('your answer in wrong !\n The Capital Of Turkey is Ankara.') 