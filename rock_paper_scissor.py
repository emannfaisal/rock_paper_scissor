game_choice= ['''
    _______
---'   ____)  
      (_____)  
      (_____)  
      (____)
---'__(___)  
'''
,

'''  
    _______
---'   ____)____  
          ______)  
          _______)  
         _______)
---'__________)  
'''
,
'''  
    _______
---'   ____)____  
          ______)  
       __________)  
      (____)
---.__(___)  
'''  ]

import random

game_question = True
while game_question :
    choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."))
    if choice >= 3 or choice < 0:
        print("You typed invalid number")
    else:
        game_question = False


print(game_choice[choice])
computer_choice = random.randint(0,2)
print("computer_choose:")
print(game_choice[computer_choice])

if choice == 0 and computer_choice == 2:
    print("You win!")

elif choice == 2 and computer_choice == 0:
    print("You lose!")

elif computer_choice > choice:
    print("you loose!")

elif choice > computer_choice:
    print("You win!")

elif choice == computer_choice:
    print("Its a draw!")