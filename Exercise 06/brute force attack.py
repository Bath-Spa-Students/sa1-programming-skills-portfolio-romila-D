'''
Exercise 6: Brute Force Attack - 30 Marks
Write a program that simulates a password entry system. The correct password
is defined as 12345. The program should keep asking the user to enter the
password until they provide the correct one.
Basic Requirements:
1. Define the correct password.
2. Use a while loop to repeatedly ask the user for the password until the
correct one is entered.
3. Output an appropriate message when the correct password is entered.
'''

# assinging correct password
orignal_password = "12345"
# Using a while loop to ask for password
while True:
# Asking user for password
    password = input("Enter your PASSWORD: ")
    
    # Checking if password is right
    if password == orignal_password:
        print("Password correct!")
        break
    else:
        print("Incorrect password. Please try again.")