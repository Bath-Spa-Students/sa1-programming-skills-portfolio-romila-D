'''
Exercise 10: Is it even? - 35 Marks
Write a program that tests if a value is even or odd. Follow the instructions
outlined below:
Instructions:
• The program should ask the user for a number from within the main
function.
• The entered number should be passed to a function that determines if the
value is even or odd.
• The function should return a message indicating whether the number is
even or odd.
• The message returned by the function should be printed from within the
main function.
'''
# defining function to check even or odd
def check_even_odd(num):
   
    # Use this operator (%) to check if the number is even
    if num % 2 == 0:
        # Return a message that number is even
        return f"{num} is even."
    else:
        # Return a message that number is odd
        return f"{num} is odd."

# Define the main function
def main():
    
    # Asking user input a number
    num = int(input("Enter a number: "))
    
    # Passing the user number to the check_even_odd function
    result = check_even_odd(num)
    
    # Print the result
    print(result)

# Checking the programs runs
if __name__ == "__main__":
    # Calling the main function
    main()
