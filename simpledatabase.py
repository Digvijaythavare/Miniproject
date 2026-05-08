import time

names = []
addresses= []
jods = []

def welcome():
    print("Enter deatils into the database")
    enter_name()

def enter_name():
    entry1 = input("Enter Name: ")
    names.append(entry1)
    enter_addresses()

def enter_addresses():
    entry2 = input("Enter Addresses: ")    
    addresses.append(entry2)
    enter_jobs()

def enter_jobs():
    entry3 = input("Enter Jobs: ")
    jods.append(entry3)
    show_details()

def show_details():
    print("Searching wait....")
    time.sleep(1)
    print(names)
    print(addresses)
    print(jods)
    clear_database()

def clear_database():
    print("Delete details")
    answer = input("Yes No")    
    if answer.lower() == ("yes" or "y"):
        names.clear()
        addresses.clear()
        jods.clear()
        print("DELETED",names,addresses,jods)
    else:
        print("You chose not to delete your info")
        quit()

welcome()   
