import random  # Importing the random module to generate random numbers

# Generate a random number between 1 to 6 to simulate the first dice roll
die = random.randint(1, 6)
print("You rolled the dice..:-", die)

# Start an infinite loop to allow repeated dice rolls
while True:
    # Ask the user if they want to roll the dice again
    user = input("Do you want to roll the dice again? (yes/no): ")
    
    if user.lower() == 'yes':  # If user enters 'yes'
        die = random.randint(1, 6)  # Roll the dice again
        print("You rolled:-", die)
        
    elif user.lower() == "no":  # If user enters 'no'
        print("GAME OVER!!!")  # Exit message
        break  # Exit the loop
        
    else:
        # If input is not 'yes' or 'no'
        print("Invalid input. Please type 'yes' or 'no'.")
