def rev_calculation(price, quantity):
    return price * quantity


product_dict = {
    'Laptop': 100,
    'Mouse': 50,
    'Keyboard': 50,
    'Display': 150,
    'Printer': 200
}

total_revenue = 0

for product in product_dict:
    selling = int(input(f"How many {product} have you sold today? "))
    revenue = rev_calculation(product_dict[product], selling)
    print(f'The revenue for the {product} today is {revenue}')
    total_revenue += revenue

print(f'The total revenue for all products for today is {total_revenue}')
