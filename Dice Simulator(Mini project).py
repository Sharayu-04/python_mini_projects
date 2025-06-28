import random

die=random.randint(1,6)
print("you rolled dice..:-",die)

while True:
    user=input("Do they want to roll dice Again?")
    if user == 'yes':
        die=random.randint(1,6)
        print(die)
        
    elif user=="no":
        print("GAME OVER!!!")
        break
        
    else:
        print("Invalid..")