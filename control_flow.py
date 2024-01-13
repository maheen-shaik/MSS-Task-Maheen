original_price=int(input("What is the original price of the item?"))
discount_price=original_price*0.1
discounted_price=original_price-discount_price
print("the price after discount is",discounted_price)
if discounted_price<50:
   print("Low-cost item.") 
elif discounted_price>50 and discounted_price<100:
   print("Moderate-cost item.")  
else:
   print("High-cost item.")
   mixed_data=["hello",1,1.1,'m',66,3.14,"MJCET",3]
for element in mixed_data:
   print("The type of ",element,"is",type(element))