import art
import random
print(art.logo)

easy_level_turns=10
hard_level_turns=5

# Compare user's guess with generated number

def compare(user_number,actual_number,turns):
    if user_number>actual_number:
        print("Too High")
        return turns-1
    elif user_number<actual_number:
        print("Too Low")
        return turns-1
    else:
        print(f"You have got it.The answer was {actual_number} ")



def choose_difficulty():
    difficulty = input("Choose your difficulty level. Type 'easy' or 'hard' ")
    if difficulty=="easy":
        return easy_level_turns
    else:
        return hard_level_turns

def number_guessing_game():

    print("WElCOME TO THE NUMBER GUESSING GAME\nI AM THINKING OF A NUMBER BETWEEN 1 TO 100")
    # generate a random number
    number=random.randint(1,100)


    turns=choose_difficulty()
    # Let the user make a guess
    guess=0
    while guess!=number:
        print(f"You have {turns} guesses left")
        guess=int(input("Make a guess: "))

        turns=compare(guess,number,turns)
        if turns==0:
            print("You have run out of guesses,you lose")
            print(f"Correct answer was {number}")
            return

number_guessing_game()















