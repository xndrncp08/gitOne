# November 30 2024
# Group #8, Members: Xander Rancap & Yvana Gaddao

# We both worked on Part 2 at the same time in teams

# Welcome message
print("Welcome to Circle Phones’ Profit calculator.")
print("You can calculate your profits for a specific day, by week, or you can divide the week into weekdays and the weekend.")

# Profit margins
profit_margins = [120.45, 99.50, 75.69, 65.73, 51.49]

total_profit = 0

#user selects period
print("\nEnter:")
print("\n1 - For specific Day")
print("\n2 - For the Week")
print("\n3 - For Week Business Days")
print("\n4 - For Weekend days")
print("\n0 - Exit")

while True:
    choice = int(input())

    if choice == 0:  #stop if user entered 0
        print("Program End!")
        break  #ends program

    if choice == 1:  #calculate total for day
        print("Enter a specific day [Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday]")
        day = input().capitalize()
        
        if day not in ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]:
            print("Invalid input, please enter a valid day.") #user input not valid, select value 1-5
            
        else:
            print(f"For {day}")
            while True:
                print("Enter product number 1-5, or enter 0 to stop:")
                product = int(input())
                
                if product == 0:  #stop if user entered 0
                    break
                
                if product < 1 or product > 5:
                    print("Invalid input, please enter a valid number.") #user input not valid, select value 1-5
                    continue
                print("Enter quantity sold:")
                quantity = int(input())
                total_profit += profit_margins[product - 1] * quantity
                
            print(f"Total Profit for {day} is: ${total_profit:.2f}")
            if total_profit >= 10000:
                print("You did well this period! Keep up the great work")
            else:
                print(f"More hard work needed... The last {day} wasn't the best")

    elif choice == 2:  #calculate total for week
        days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
        for day in days_of_week:
            print(f"For {day}")
            while True:
                print("Enter product number 1-5, or enter 0 to stop:")
                product = int(input())
                if product == 0: #stop if user entered 0
                    break
                if product < 1 or product > 5:
                    print("Invalid input, please enter a valid number.") #user input not valid, select value 1-5
                    continue
                print("Enter quantity sold:")
                quantity = int(input())
                total_profit += profit_margins[product - 1] * quantity
        if total_profit >= 10000:
            print(f"Total Profit for the week is: ${total_profit:.2f}")
            print("You did good this week")
        else:
            print(f"Total Profit for the week is: ${total_profit:.2f}")
            print("We didn’t reach our goal for this period. More work is needed")

    elif choice == 3:  #calculate total for business days (weekdays)
        weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
        for day in weekdays:
            print(f"For {day}")
            while True:
                print("Enter product number 1-5, or enter 0 to stop:")
                product = int(input())
                if product == 0: #stop if user entered 0
                    break
                if product < 1 or product > 5:
                    print("Invalid input, please enter a valid number.") #user input not valid, select value 1-5
                    continue
                print("Enter quantity sold:")
                quantity = int(input())
                total_profit += profit_margins[product - 1] * quantity
        if total_profit >= 10000:
            print(f"Total Profit for the week (business days) is: ${total_profit:.2f}")
            print("You did good this week (business days)")
        else:
            print(f"Total Profit for the week (business days) is: ${total_profit:.2f}")
            print("We didn’t reach our goal for this period. More work is needed")

    elif choice == 4:  #calculate total for weekend
        weekend_days = ["Saturday", "Sunday"]
        for day in weekend_days:
            print(f"For {day}")
            while True:
                print("Enter product number 1-5, or enter 0 to stop:")
                product = int(input())
                if product == 0: #stop if user entered 0
                    break
                if product < 1 or product > 5:
                    print("Invalid input, please enter a valid number.") #user input not valid, select value 1-5
                    continue
                print("Enter quantity sold:")
                quantity = int(input())
                total_profit += profit_margins[product - 1] * quantity
            print(f"Total Profit for {day} is: ${total_profit:.2f}")
            if total_profit >= 10000:
                print("You did good this weekend")
            else:
                print("We didn’t reach our goal for this period. More work is needed")
    else:
        print("Invalid input, please enter a valid input")
