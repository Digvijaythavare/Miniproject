people = {"jay": "developer" , "vijay": "engineer"}


def intro():
    print("Welcome to the Data Base \n")
    print("To get access enter your password")
    enter_password()

def enter_password():
    password = "123abc"
    entry1 = input("Enter Password: ")
    if (len(entry1)<3 and (entry1 != password)):
        print("Access Denied!")
    else:
        print("Access Grented!")
        data_base()

def data_base():
    x = int(input("Clear(1) ,Update(2),Print(3)"))
    if x == 1:
        people.clear()
        print(people)
        print("Data base cleared")
    elif x == 2:
        update_dictionary()
    elif x == 3:
        print(people)

def update_dictionary():
    for i in range(3):
        name = input("Enter name: ")
        job = input("Enter job: ")
        people[name] = job
        print(people)
intro()        
