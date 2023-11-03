name = input("Enter your name: ")
original_price = float(input("Enter the original price of the product: "))
discount_percentage = float(input("Enter the discount percentage: "))

if discount_percentage >= 100:
    print("Error: Invalid discount percentage.")
else:
    final_price = original_price - (original_price * (discount_percentage / 100))
    print(f"{name}, the final price is: {final_price:.2f}")