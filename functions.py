def calculate_discount(original_price,discount_percentage):
    discount_price=original_price*discount_percentage
    discounted_price=original_price-discount_price
    return discounted_price
original_price=1000
print("The original price is:",original_price)
discount_percentage=0.1
discounted_price=calculate_discount(original_price,discount_percentage)
print("The price after discount is :",discounted_price)
