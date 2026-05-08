import time
username = input("Enter username")        
password = input("Enter password")
user = "Vijay"
passw = 1234
if username == user and password == passw:
    time.sleep(2)
    loginfor() # type: ignore
else:
     time.sleep(2)
     loginform1()
 
def loginfor():
    for num in range(10,100):
        print(num)

def loginform1():
     name = "hello"
     print(name *40)


