import time

# Product Database
products = {
    1: {"name": "Rice", "price": 60},
    2: {"name": "Wheat", "price": 40},
    3: {"name": "Sugar", "price": 45},
    4: {"name": "Milk", "price": 30},
    5: {"name": "Oil", "price": 150},
    6: {"name": "Tea", "price": 120},
    7: {"name": "Soap", "price": 35},
    8: {"name": "Biscuits", "price": 20}
}

# Shopping Cart
cart = {}

# Total Bill
total = 0

print("=" * 45)
print("       WELCOME TO SUPERMARKET")
print("=" * 45)

customer = input("Enter customer name: ")

# Main While Loop
while True:

    print("\n========== MAIN MENU ==========")
    print("1. Show Products")
    print("2. Add Product to Cart")
    print("3. View Cart")
    print("4. Remove Product")
    print("5. Generate Final Bill")
    print("6. Exit")

    choice = input("Enter your choice: ")

    # Show Products
    if choice == "1":

        print("\n------ AVAILABLE PRODUCTS ------")

        for product_id, details in products.items():
            print(
                f"{product_id}. {details['name']} "
                f"- Rs.{details['price']}"
            )

    # Add Product
    elif choice == "2":

        print("\n------ ADD PRODUCT ------")

        for product_id, details in products.items():
            print(
                f"{product_id}. {details['name']} "
                f"- Rs.{details['price']}"
            )

        try:
            product_id = int(input("Enter product ID: "))
            quantity = int(input("Enter quantity: "))

            if product_id in products and quantity > 0:

                if product_id in cart:
                    cart[product_id] += quantity

                else:
                    cart[product_id] = quantity

                print("Product added successfully!")

            else:
                print("Invalid product ID or quantity!")

        except ValueError:
            print("Please enter a valid number!")

    # View Cart
    elif choice == "3":

        print("\n========== YOUR CART ==========")

        if not cart:
            print("Your cart is empty!")

        else:
            total = 0

            for product_id, quantity in cart.items():

                name = products[product_id]["name"]
                price = products[product_id]["price"]

                amount = price * quantity
                total += amount

                print(
                    f"{name} | Qty: {quantity} | "
                    f"Price: Rs.{price} | "
                    f"Amount: Rs.{amount}"
                )

            print("-" * 35)
            print(f"Total Amount: Rs.{total}")

    # Remove Product
    elif choice == "4":

        print("\n------ REMOVE PRODUCT ------")

        if not cart:
            print("Your cart is empty!")

        else:
            for product_id, quantity in cart.items():
                print(
                    f"{product_id}. "
                    f"{products[product_id]['name']} "
                    f"- Qty: {quantity}"
                )

            try:
                remove_id = int(
                    input("Enter product ID to remove: ")
                )

                if remove_id in cart:

                    del cart[remove_id]

                    print("Product removed successfully!")

                else:
                    print("Product not found in cart!")

            except ValueError:
                print("Please enter a valid product ID!")

    # Generate Final Bill
    elif choice == "5":

        print("\n========== FINAL BILL ==========")

        if not cart:
            print("Your cart is empty!")

        else:
            total = 0

            print(f"Customer Name: {customer}")
            print("-" * 45)

            print(
                f"{'Product':<15}"
                f"{'Qty':<8}"
                f"{'Price':<8}"
                f"{'Amount':<10}"
            )

            print("-" * 45)

            for product_id, quantity in cart.items():

                name = products[product_id]["name"]
                price = products[product_id]["price"]

                amount = price * quantity
                total += amount

                print(
                    f"{name:<15}"
                    f"{quantity:<8}"
                    f"{price:<8}"
                    f"{amount:<10}"
                )

            print("-" * 45)
            print(f"TOTAL BILL: Rs.{total}")

            print("\nThank you for shopping!")

            time.sleep(2)

            cart.clear()

            print("Bill generated successfully!")

    # Exit
    elif choice == "6":

        print("\nThank you for visiting!")
        print("Exiting Billing System...")

        break

    # Invalid Choice
    else:
        print("Invalid choice! Please try again.")

    time.sleep(1)

print("\nProgram Closed.")
