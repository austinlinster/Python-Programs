# Taco Sales Tool

#Jonathan Zhou:
#Homework 1 Taco Sales:
#September 1st, 2022:
#Enter product and sales information to create a financial summary:

# User Input Data
name = input("What is the name of the item being sold? ")
number_of_items = float(input("How many of the items were sold? "))
cost_of_item = float(input("What is the cost of the item being sold? "))
price_of_item = float(input("What is the price of the item being sold? "))

# Process & Calculations
total_cost = number_of_items * cost_of_item
total_revenue = number_of_items * price_of_item
total_profit = total_revenue - total_cost
percent_profit = (total_profit / total_revenue) * 100

# Formatting Output
format_quantity = int(number_of_items)
format_cost = "{:.2f}".format(total_cost)
format_revenue = "{:.2f}".format(total_revenue)
format_profit = "{:.2f}".format(total_revenue)
format_percent = int(percent_profit)

# Print Out Relvant Info
print(f'Item Name: {name}')
print(f'Quantity Sold: {format_quantity}')
print(f'Total Cost: ${format_cost}')
print(f'Total Revenue: ${format_revenue}')
print(f'Total Profit: ${format_profit}')
print(f'Percent Profit: {format_percent}%')