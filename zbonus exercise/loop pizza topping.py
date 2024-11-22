'''
Loops- Pizza Toppings :
Write a loop that prompts the user to enter a series of pizza toppings until they enter a
'quit' value. As they enter each topping,
Print a message saying you’ll add that topping to their pizza.
'''
# creating empty list to store pizza toppings
pizza_toppings = []

# creating a variable to store the user's input
topping = ""

# Loop until the user enters 'quit'
while topping.lower() != 'quit':
    # asaking the user to enter all pizza topping
    topping = input("Enter a pizza topping ('quit' to finish): ")
    
    # Check if the user is done
    if topping.lower() == 'quit':
        break
    
    # Add the user toppings to the list we create
    pizza_toppings.append(topping)
    
    # Printing a message 
    print(f"Adding {topping} to your pizza!")

# Print the final list of pizza toppings
print("\nYour pizza toppings:")
for topping in pizza_toppings:
    print(topping)