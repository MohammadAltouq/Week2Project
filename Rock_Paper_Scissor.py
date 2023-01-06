import random
def computer_choice():
    l = ["rock", "paper", "scissor"]
    i = random.randint(0, 2)
    return l[i]
win_num = 0
loss_num = 0
while True:
    print("Number of wins: ", win_num)
    print("Number of losses: ", loss_num)
    user_input = input("Rock, Paper, Scissor, choose one. ")
    if user_input.lower().strip() == 'quit':
        print("See ya next time :)")
        break
    com = computer_choice()
    print("Computer chose: ", com)
    if user_input.lower().strip() == 'rock' and computer_choice() == 'paper':
        print("You lose!")
        loss_num += 1
    elif user_input.lower().strip() == 'rock' and computer_choice() == 'scissor':
        print("You win!")
        win_num += 1
    elif user_input.lower().strip() == computer_choice():
        print("Game Tied")
    elif user_input.lower().strip() == 'paper' and computer_choice() == 'rock':
        print("You win!")
        win_num += 1
    elif user_input.lower().strip() == 'paper' and computer_choice() == 'scissor':
        print("You lose!")
        loss_num += 1
    elif user_input.lower().strip() == 'scissor' and computer_choice() == 'rock':
        print("You lose!")
        loss_num += 1
    elif user_input.lower().strip() == 'scissor' and computer_choice() == 'paper':
        print("You win!")
        win_num += 1
    else:
        print("Invalid Input")