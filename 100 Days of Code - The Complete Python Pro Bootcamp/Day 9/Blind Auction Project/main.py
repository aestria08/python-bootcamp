# TODO-1: Ask the user for input
import art
print(art.logo)

# name=input("What is your name?\n ")
# bid=int(input("What is your bid? \n"))
# dict={}
# dict[name]=bid
# print(dict)
# more=input("Are there any more bidders? Type 'yes' or 'no' \n ")
more="yes"
dict={}
while more=="yes":
    name = input("What is your name?\n ")
    bid =int (input("What is your bid? $ \n"))
    # dict = {}
    dict[name] = bid
    print(dict)
    more = input("Are there any more bidders? Type 'yes' or 'no' \n ")
    print("\n"*20)
if more=="no":
    highest=max(dict,key=dict.get)
    print(f"{highest} won the bid")


# TODO-2: Save data into dictionary {name: price}
# TODO-3: Whether if new bids need to be added
# TODO-4: Compare bids in dictionary


