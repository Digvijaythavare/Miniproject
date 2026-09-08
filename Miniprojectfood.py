print("================================")
print("       FOOD ORDER SYSTEM")
print("================================")

menu = {
    1: ("Pizza", 250),
    2: ("Burger", 120),
    3: ("Sandwich", 80),
    4: ("French Fries", 100),
    5: ("Cold Drink", 50)
}

total = 0

while True:
    print("\n--------- MENU ---------")

    for number, item in menu.items():
        print(f"{number}. {item[0]} - ₹{item[1]}")

    print("0. Finish Order")

    choice = int(input("\nEnter item number: "))

    if choice == 0:
        break

    if choice in menu:
        quantity = int(input("Enter quantity: "))

        item_name = menu[choice][0]
        price = menu[choice][1]

        amount = price * quantity
        total += amount

        print(f"{item_name} x {quantity} = ₹{amount}")

    else:
        print("Invalid choice!")

# GST calculation
gst = total * 0.05
final_amount = total + gst

print("\n================================")
print("            BILL")
print("================================")
print(f"Food Total : ₹{total:.2f}")
print(f"GST (5%)   : ₹{gst:.2f}")
print(f"Final Bill : ₹{final_amount:.2f}")
print("================================")
print("      Thank You! Visit Again")
print("================================")