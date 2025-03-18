def calculate_discount(price, discount_percent):
    
   #This method Calculates the final price after applying a discount.
    
   #parameter price is the original price of the item
   #parametr discount_percent is Discount percentage to be allowed
   # the function returns the final price after discount (if applicable)
    
    if discount_percent >= 20:
        discount_amount = (discount_percent / 100) * price
        final_price = price - discount_amount
        return final_price
    else:
        return price

# Prompting the user for input

original_price = float(input("Enter the original price of the item: "))
discount_percentage = float(input("Enter the discount percentage: "))

# Calculate and display the final price
final_price = calculate_discount(original_price, discount_percentage)
print(f"Final price after discount: ksh.{final_price:.2f}")


