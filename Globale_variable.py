import time

list12 =[10,20,30,40,50,60,70]

views = isinstance(list12,list)

j = 0 

def hastutorial():
    if views == True:
        for i in list12:
                global j
                j += 1
                print(f"Index is {j} and value is {i}")
        else:
               print("sart again")
    else:
          for k in range(1,11):
            if k == 3:
                 continue
            print(k)           
hastutorial()            
        