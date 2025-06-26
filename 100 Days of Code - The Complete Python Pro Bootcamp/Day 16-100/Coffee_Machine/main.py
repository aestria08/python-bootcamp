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
resources={
    "water":300,
    "milk":200,
    "coffee":100
}
money=0

def sufficient_resource(ingredients):
    enough=True
    for i in ingredients:
        if ingredients[i]>=resources[i]:
            print(f"Sorry there is not enough {i}.")
            enough=False
    return enough


def coins():
    print("Please insert coins")
    total=int(input("How many quarters? : "))*0.25
    total+=int(input("How many dimes? : "))*0.1
    total+=int(input("How many nickles? :"))*0.05
    total+=int(input("How many pennies? :"))*0.01
    return total

def transaction(received,drink_cost):
    if received>=drink_cost:
        change=round(received-drink_cost,2)
        print(f"Here is ${change} dollars in change")
        global money
        money+=drink_cost
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False

def make_coffee(drink_name,ingredients):
    for i in ingredients:
        resources[i]-=ingredients[i]
    print(f"Here's your {drink_name}")


machine_on=True
while machine_on:
    choose=input("What would you like? (espresso/latte/cappuccino):")
    if choose=="off":
        machine_on=False
    elif choose=="report":
       print(f" Water: {resources["water"]}ml")
       print(f" Milk: {resources["milk"]}ml")
       print(f" Coffee: {resources["coffee"]}g")
       print(f" Money: ${money}")
    else:
        drink=MENU[choose]
        if sufficient_resource(drink["ingredients"]):
            payment=coins()
            if transaction(payment,drink["cost"]):
                make_coffee(choose,drink["ingredients"])


