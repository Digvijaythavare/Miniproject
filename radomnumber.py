from random import randint
from turtle import Turtle

print("----Guess the number game----")

def lucky_number():
    number = randint(1,3)
    Guess = int(input("Pick a number between 1 and 3:"))

    if number != Guess:
        print("You guessed wrong number")
        print("Correct number was:", number)
        booby_prize()

    else:
        print("You guessed the right number")
        your_Prize()


def booby_prize():        
    print("You get a poke in the eye!" * 3)
    lucky_number()


def your_Prize():
    t = Turtle()      # turtle object create
    t.pendown()
    t.forward(50)
    t.left(78)
    t.right(45)
    t.forward(66)
    t.left(78)


lucky_number()