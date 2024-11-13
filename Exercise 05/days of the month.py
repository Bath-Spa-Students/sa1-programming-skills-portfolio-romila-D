'''
Exercise 5: Days of the Month - 30 Marks
Write a program that tells a user how many days there are in a specific month.
Use a dictionary to map the month numbers (1-12) to the number of days in
each month.
Instructions:

1. Create a Dictionary: Define a dictionary where the keys are month num-
bers and the values are the number of days in those months.

2. Input Handling: Ask the user to input the month number.
3. Check and Output: Use an if-else statement to check if the input is valid
and print the number of days in the corresponding month.
'''

#creating a dictionery 

days_in_months={
    1: 31,  # January
    2: 29,  # February
    3: 31,  # March
    4: 30,  # April
    5: 31,  # May
    6: 30,  # June
    7: 31,  # July
    8: 31,  # August
    9: 30,  # September
    10: 31,  # October
    11: 30,  # November
    12: 31  # December
}

#taking input

months = input("Enter the month number from 1 to 12 : ")

#checking output

months = int(months)
if months< 1 or months > 12:
        print("Please enter a number between 1 and 12.")
else:
        print(f"In month {months} there are {days_in_months[months]} days .")