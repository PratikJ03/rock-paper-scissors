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
Decision= int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."))
rand= random.randint(0,2)
des=[rock,paper,scissors]
if Decision==0:
    print(des[0],"\nComputer chose: \n",des[rand])
    if rand==0:
        print("Draw")
    elif rand==1:
        print("You Lose!")
    else:
        print("You Win!")
elif Decision==1:
    print(des[1], "\nComputer chose: \n", des[rand])
    if rand==0:
        print("You Win!")
    elif rand==1:
        print("Draw")
    else:
        print("You Lose!")
elif Decision==2:
    print(des[2], "\nComputer chose: \n", des[rand])
    if rand==0:
        print("You Lose!")
    elif rand==1:
        print("You Win!")
    else:
        print("Draw")
else:
    print("Wrong Input")




