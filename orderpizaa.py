import time

def hello_message():
    print("Welcome to my pizaa restautant")
    print("We are here to take your order")
    pizza_topping()

def pizza_topping():
    topping = ["mushroom","onions","anchovies"]
    request = input("please enter a topping:  ")
    if request in topping:
        print(request,"Are available")
        soft_drink()
    else:
        print("Processing....")
        time.sleep(1)
        print(request,"Sorry not available")
        quit()


def soft_drink():
    print("Please enter your drink")        
    drink = ["cola","coffe","juice"]
    request = input("Your drink:  ")
    if request not in drink:
        print(request,"Is available")
        thank_customer()
    else:
         print("Processing....")
         time.sleep(2)
         print(request,"is not currently available here")
   

def thank_customer(): 
    print("Enjoy your meal!")


hello_message()
