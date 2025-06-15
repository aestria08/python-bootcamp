# print logo
import art,random
from game_data import data
print(art.logo)
score=0
# out of list give one option with name,country and description leaving out followers
def get_data(account):
    acc_name=account['name']
    acc_desc=account["description"]
    acc_country=account["country"]
    return f"{acc_name},a {acc_desc},from {acc_country}"
# compare 2 options based on followers
def compare(user_guess,a_follower,b_follower):
    if a_follower>b_follower:
        return user_guess=='a'
    else:
        return user_guess=='b'


account_b=random.choice(data)
continue_game=True
while continue_game:

    account_a=account_b
    account_b=random.choice(data)
    if account_a==account_b:
        account_b=random.choice(data)

    print(f"Compare A: {get_data(account_a)}")

    # print vs part of logo
    print(art.vs)
    # give 2nd option in similar option
    print(f"Against B: {get_data(account_b)}")
    # Ask user to choose between A nd B based on the number of followers
    guess=input("Who has more followers? Type 'A' or 'B':\n ").lower()
    # Clear the screen
    print("\n"*30)
    print(art.logo)

    a_follower_count=account_a["follower_count"]
    b_follower_count=account_b["follower_count"]
    correct=compare(guess,a_follower_count,b_follower_count)

    if correct:
        score+=1
        print(f"You are right! Current Score:{score}")
    else:
        print(f"Sorry,you got it wrong.Final Score:{score} \nGame Over!")
        continue_game=False



    # if user guesses correctly move ahead by keeping the option of fewer followers as it is and giving next option
    # continue until user gets the guess wrong

