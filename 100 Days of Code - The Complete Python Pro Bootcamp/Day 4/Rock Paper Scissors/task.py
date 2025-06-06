import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
game=[rock,paper,scissors]
user_input=input("What would you choose?? TYPE 0 for Rock,1 for Paper,2 for scissors")
computer_choice= random.randint(0,2)

if user_input>=3 and user_input<0:





