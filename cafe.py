# Creating the menu list and the stock and price dictionaries:
menu = ["Latte", "Espresso", "Tea", "Water"]
stock = {"Latte": 30, "Espresso": 20, "Tea": 15, "Water": 50}
price = {"Latte": 3.50, "Espresso": 2.00, "Tea": 3.00, "Water": 1.50}

# Calculating the total stock worth in the cafe using the for loop 
# and printing out the result, formatted to two decimal places:
total_stock_worth = 0

for item in menu:
    item_value = (stock[item] * price[item])
    total_stock_worth += item_value
    
print(f"Total stock worth in the cafe is: £{total_stock_worth:.2f}")