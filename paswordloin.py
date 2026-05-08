user = "Admin"
passwprd = 1234

def login():
    attempts = 0
    max_attempts = 3
    while attempts < max_attempts:
        username = input("Enter username: ")
        pw = input("Enter password: ")
        if username == user and pw == passwprd:
            print("Access Granted")
            break
        else:
            attempts += 1 
            print("Incorrect login",attempts - max_attempts,"Attempts made")
            if attempts == max_attempts:
                print("Message sent")
                send_message()
def send_message():
     with open("faild login.txt","w") as file_object:
      file_object.write("Someone tried to login to your account")
login()                    