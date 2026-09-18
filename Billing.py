bill = float(input("Enter the bill amount: "))
if bill > 1000:
    discount = bill * 0.1
    final_amount = bill - discount
    print(f"Discount applied: {discount}")
    print(f"Final amount to be paid: {final_amount}")
elif bill > 3000:
    discount = bill * 0.05
    final_amount = bill - discount
    print(f"Discount applied: {discount}")
    print(f"Final amount to be paid: {final_amount}")   
elif bill > 5000:
    discount = bill * 0.02
    final_amount = bill - discount
    print(f"Discount applied: {discount}")
    print(f"Final amount to be paid: {final_amount}")
elif bill > 0:
    discount = 0
    final_amount = bill
    print(f"No discount applied.")
    print(f"Final amount to be paid: {final_amount}")

else:
    print("Invalid bill amount.")