# Coffee Machine Program

import os

flavours = {"espresso": {"water": 150, "coffee": 18, "milk": 0, 'amount': 1.5},
            "latte": {"water": 200, "coffee": 24, "milk": 150, 'amount': 2.5},
            "cappuccino": {"water": 250, "coffee": 24, "milk": 100, 'amount': 3.0}
            }

resource = {"water": 500, "coffee": 50, "milk": 500, 'amount': 5.0}


def progress():
    coins = {'quarters': 0.25, 'dimes': 0.10, 'nickles': 0.05, 'pennies': 0.01}
    consumer_amount = 0
    print("Please insert coins.")

    for coin in coins:
        count = int(input('how many {}?: '.format(coin)))
        consumer_amount += round(coins[coin] * count, 2)

    print(round(consumer_amount, 2))

    if flavours[consumer_input]['amount'] > consumer_amount:
        print("That's not enough money. Money refunded.")
    else:
        balance_amount = round((consumer_amount - flavours[consumer_input]['amount']), 2)
        resource['amount'] += flavours[consumer_input]['amount']
        resource['water'] -= flavours[consumer_input]['water']
        resource['coffee'] -= flavours[consumer_input]['coffee']
        resource['milk'] -= flavours[consumer_input]['milk']
        print(f"Here is ${balance_amount} in change.\nHere is your {consumer_input}.. ☕Enjoy..!")


def check_resource():
    if flavours[consumer_input]['water'] <= resource['water']:
        if flavours[consumer_input]['coffee'] <= resource['coffee']:
            if flavours[consumer_input]['milk'] <= resource['milk']:
                progress()
            else:
                print("Sorry there is not enough milk.")
        else:
            print("Sorry there is not enough coffee.")
    else:
        print("Sorry there is not enough water.")


while True:
    consumer_input = input('What would you like? (espresso/latte/cappuccino): ')

    if consumer_input == 'closed':
        print('Resource Report: ')
        print(f"Water: {resource['water']}ml")
        print(f"Milk: {resource['milk']}ml")
        print(f"Coffee: {resource['coffee']}g")
        print(f"Money: ${resource['amount']}")
        break
    check_resource()


    # Clear Screen used for windows
    def clear_screen():
        os.system('cls' if os.name == 'nt' else 'clear')

    print('\n' * 5)



# Another Method

# MENU = {
#     "espresso": {
#         "ingredients": {
#             "water": 50,
#             "coffee": 18,
#         },
#         "cost": 1.5,
#     },
#     "latte": {
#         "ingredients": {
#             "water": 200,
#             "milk": 150,
#             "coffee": 24,
#         },
#         "cost": 2.5,
#     },
#     "cappuccino": {
#         "ingredients": {
#             "water": 250,
#             "milk": 100,
#             "coffee": 24,
#         },
#         "cost": 3.0,
#     }
# }
#
# profit = 0
# resources = {
#     "water": 300,
#     "milk": 200,
#     "coffee": 100,
# }
#
#
# def is_resource_sufficient(order_ingredients):
#     """Returns True when order can be made, False if ingredients are insufficient."""
#     for item in order_ingredients:
#         if order_ingredients[item] > resources[item]:
#             print(f"​Sorry there is not enough {item}.")
#             return False
#     return True
#
#
# def process_coins():
#     """Returns the total calculated from coins inserted."""
#     print("Please insert coins.")
#     total = int(input("how many quarters?: ")) * 0.25
#     total += int(input("how many dimes?: ")) * 0.1
#     total += int(input("how many nickles?: ")) * 0.05
#     total += int(input("how many pennies?: ")) * 0.01
#     return total
#
#
# def is_transaction_successful(money_received, drink_cost):
#     """Return True when the payment is accepted, or False if money is insufficient."""
#     if money_received >= drink_cost:
#         change = round(money_received - drink_cost, 2)
#         print(f"Here is ${change} in change.")
#         global profit
#         profit += drink_cost
#         return True
#     else:
#         print("Sorry that's not enough money. Money refunded.")
#         return False
#
#
# def make_coffee(drink_name, order_ingredients):
#     """Deduct the required ingredients from the resources."""
#     for item in order_ingredients:
#         resources[item] -= order_ingredients[item]
#     print(f"Here is your {drink_name} ☕️. Enjoy!")
#
#
# is_on = True
#
# while is_on:
#     choice = input("​What would you like? (espresso/latte/cappuccino): ")
#     if choice == "off":
#         is_on = False
#     elif choice == "report":
#         print(f"Water: {resources['water']}ml")
#         print(f"Milk: {resources['milk']}ml")
#         print(f"Coffee: {resources['coffee']}g")
#         print(f"Money: ${profit}")
#     else:
#         drink = MENU[choice]
#         if is_resource_sufficient(drink["ingredients"]):
#             payment = process_coins()
#             if is_transaction_successful(payment, drink["cost"]):
#                 make_coffee(choice, drink["ingredients"])
