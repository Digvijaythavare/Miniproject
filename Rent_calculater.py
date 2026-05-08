Room_rent = int(input("Enter your Rent /- "))
food_amout = int(input("Enter the amount of food /- "))
electricity_spend = int(input("Enter the total electricity spend /- "))
charge_per_unit = int(input("Enter the charge per unite /- "))
person = int(input("Enter the of person living in the room /-"))

total_bill = electricity_spend * charge_per_unit

amount = (Room_rent + food_amout + total_bill )// person

print("each person will pay /-",amount)
