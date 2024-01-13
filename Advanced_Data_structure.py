# Implement the customer_info dictionary
customer_info = {
    'name': 'Maheen',
    'age': 19,
    'purchase_history': ['Product 1', 'Product 2', 'Product 3']
}

# Retrieving and print the customer's name
customer_name = customer_info['name']
print("Customer's Name:" ,customer_name)
# Retrieve and print the customer's second purchase from the purchase history
purchase_history = customer_info['purchase_history']
second_purchase=purchase_history[1]
print("second puchase is",second_purchase)


