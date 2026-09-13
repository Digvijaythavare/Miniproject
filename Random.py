import random

while True:
    print("-------Welcome to Ai Mind reading project-------")


    number = int(input("Enter a number between 1 and 10: "))
    if number  < 1 or number > 10:
        print("Please enter a valid number between 1 and 10.")

    ai = random.randint(1, 10)

    print("Ai is thinking......")
    print("Your number is: ", number)
    print("AI guessed: ", ai) 

    if number == ai:
        print("AI read your mind correctly!")
    else:
        print("You win! this game")


    choise = input("Do you want to play again? (yes/no): ")
    if choise.lower() != "yes":
        print("Thank you for playing! Goodbye.")
        break    