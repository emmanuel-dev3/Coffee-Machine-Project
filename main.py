from idlelib.configdialog import changes
MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

on = True
money = 0

def calculate_amount(quarters_amount, dimes_amount, nickles_amount, pennies_amount):
    """This function calculate the sum of amount the user put in."""
    return quarters_amount * 0.25 + dimes_amount * 0.1 + nickles_amount * 0.05 + pennies_amount * 0.01

def user_ingredients(choice):
    """This function make the beverages and deduct the cost."""
    global money

    if resources["water"] < MENU[choice]["ingredients"]["water"]:
        print("Sorry there is not enough water.")
    elif "milk" in MENU[choice]["ingredients"] and resources["milk"] < MENU[choice]["ingredients"]["milk"]:
        print("Sorry there is not enough milk.")
    elif resources["coffee"] < MENU[choice]["ingredients"]["coffee"]:
        print("Sorry there is not enough coffee.")
    else:
        quarters = int(input("how many quarters?: "))
        dimes = int(input("how many dimes?: "))
        nickles = int(input("how many nickles?: "))
        pennies = int(input("how many pennies?: "))

        total_amount = calculate_amount(quarters, dimes, nickles, pennies)

        if total_amount >= MENU[choice]["cost"]:
            money += MENU[choice]["cost"]
            beverages = "latte" if choice == "latte" else "espresso" if choice == "espresso" else "cappuccino"
            change = total_amount - MENU[choice]["cost"]
            resources["water"] -= MENU[choice]["ingredients"]["water"]
            if choice != "espresso":
                resources["milk"] -= MENU[choice]["ingredients"]["milk"]
            resources["coffee"] -= MENU[choice]["ingredients"]["coffee"]

            print(f"Here is ${round(change, 2)} in change.")
            print(f"Here is your {beverages} ☕️. Enjoy!")
        else:
            print("Sorry that's not enough money. Money refunded.")

while on:
    user_choice = input("What would you like? (espresso/latte/cappuccino): ").lower()

    if user_choice == "espresso":
        user_ingredients(user_choice)
    elif user_choice == "latte":
        user_ingredients(user_choice)
    elif user_choice == "cappuccino":
        user_ingredients(user_choice)
    elif user_choice == "report":
        print(f"Water: {resources["water"]}ml \nMilk: {resources["milk"]}ml \nCoffee: {resources["coffee"]}g \nMoney: ${money}")
    elif user_choice == "off":
        on = False
