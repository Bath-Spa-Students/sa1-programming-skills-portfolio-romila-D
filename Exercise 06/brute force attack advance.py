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

Optional Requirements:
Modify the program to include a maximum of 5 password attempts. If the
user enters the wrong password, inform them of the remaining attempts. If the
maximum number of attempts is reached, inform the user that the authorities
have been alerted.

'''

# assinging correct password
orignal_password = "12345"
#giving count for incorrect password
allowed_attempts = 5
incorrect_password = 0

# Using a while loop to ask for password
while incorrect_password < allowed_attempts:
    # Asking user for password
    password = input("Enter your PASSWORD: ")
    
    # giving 2nd chance
    incorrect_password += 1
    
    # Checking if password is correct
    if password == orignal_password:
        print("Password correct!")
        break
    else:
        remaining_attempts = allowed_attempts - incorrect_password
        print("Sorry,Incorrect password.")
else:
    print("Maximum attempts reached. please try again later.")