print("Welcomr To The Game!\n")
print("----------------------------------------------")
print("You are lin Deehli Belly Curry House")
print("----------------------------------------------")
print("\nAnswer orrectly To Win")


def first_question():
    entry1 = input("Do you want a vindaloo or korma? ")
    if entry1.lower() == "pizaa":
        print("Your are a real man - next questionm ")
        second_question()
    elif entry1.lower() == "korma":
        print("You lose - bye bye")   
        quit() 
    else:
        print("Answer not recognised")    


def second_question():
    entry2 = input("Want a drink (Beer or lemonade)?")
    if entry2.lower() == "beer":
        print("You chose wisely. Only a beer can kill a vindaloo")
        third_question()
    elif entry2.lower() == "tea":
        print("You big girls blouse ! bye")
        quit()
    else:
        print("Error occured!")


def third_question():
    entry3 = input("Did you put the toilet roll in the fridge last night (Y or N)")
    if entry3.lower() == "y":
        print("Phew, no bum burner for you tomorrow! - next question...")
        fourth_question()
    elif entry3.lower() == "no":
        print("You are curry light weight bye bye")
        quit()
    else:
        print("An error occured")    

def fourth_question():
    entry4 = input("Have you got to go to work tomorrow (Y or N)")
    if entry4.lower() == "yes":
      print("oh no, make sure you a nappy! ")
      fifth_question()
    elif entry4.lower() == "no":
        print("ok but make sure you stay near a toilet! ")
        fifth_question()
    else:
        print("An error occured")    

def  fifth_question():
      entry5 =input("Can you pay the bill (Y N)")
      if entry5.lower() == "yes":
          print("Congrats you'r a star!")
          winner()
      elif entry5.lower() == "no":
          print("Well, get ready to do the washing up!")
      else:
          print("An error occured")

def winner():
    x = "Congrats you'r won the game----"*30
    print(x.upper())          

first_question()