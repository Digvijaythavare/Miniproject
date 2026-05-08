import random
def create_random_email():
    rand_num = random.randint(100,999)
    ramd_email = "vijay{}@gmail.com".format(rand_num)
    print(ramd_email)
    print("Generate Another")
    entry = input(">> ")
    if entry.lower() == "y":
        create_random_email()
    else:
        print("You chose to exit")
        quit()
create_random_email()            