# November 30 2024
# Group #8, Members: Xander Rancap & Yvana Gaddao

# Xander did part 1
# Welcome message
print("Welcome to Circle Phones’ Profit calculator.")

#profit margins
profit_margins = [120.45, 99.50, 75.69, 65.73, 51.49]

total_profit = 0

while True: #Ask user for product category
    print("Enter product number 1-5, or enter 0 to stop:")
    product = int(input())  # Take user input as an integer

    if product == 0: 
        break #stop if user entered 0
    elif product < 1 or product > 5:
        print("Invalid input, please enter a valid number") #user input not valid, select value 1-5
        continue

    print("Enter quantity sold:") #ask user for quantity sold
    quantity = int(input()) # Take user input as an integer

    total_profit += profit_margins[product - 1] * quantity #calculating total profit based off of user input

print(f"Your total profit for today is: {total_profit:.2f}")