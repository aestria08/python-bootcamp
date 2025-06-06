print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M or L: ")
pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
extra_cheese = input("Do you want extra cheese? Y or N: ")
bill=0
if size=="S":
    # print("Small sized pizza costs $15")
    bill=15
    if pepperoni == "Y":
        # print("Pepperoni costs additional $2")
        bill += 2
elif size=="M":
    # print("Medium sized pizza costs $20")
    bill=20
    if pepperoni == "Y":
        # print("Pepperoni costs additional $2")
        bill += 3
elif size=="L":
    bill=25
    # print("Large sized pizza costs $25")
    if pepperoni == "Y":
        # print("Pepperoni costs additional $2")
        bill += 3


if extra_cheese=="Y":
    # print("Extra cheese costs $1")
    bill+=1
    print(f"Your final bill is: ${bill}.")
else:
    print(f"Your final bill is: ${bill}.")






