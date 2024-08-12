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
def check_resources(drink):
    """Checks if the given ingredient is available as needed"""
    sufficient = True
    for ingredient in MENU[drink]["ingredients"]:
        if resources[ingredient] < MENU[drink]["ingredients"][ingredient]:
            print(f"Sorry there is not enough {ingredient}")
            sufficient = False

machine_on = True

while machine_on:
    choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if choice in MENU:
        check_resources(choice)

    if choice == "off":
        machine_on = False
    elif choice == "report":
        print(f'water: {resources["water"]}ml')
        print(f'milk: {resources["milk"]}ml')
        print(f'coffee: {resources["coffee"]}g')

#TODO: Check resources sufficient?


                      