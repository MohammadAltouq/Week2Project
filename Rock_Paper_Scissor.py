import random
def computer_choice():
    l = ["rock", "paper", "scissor"]
    i = random.randint(0, 2)
    return l[i]
win_num = 0
loss_num = 0
p_t_tracking = 0
play_time = int(input("how many rounds would you like to play enter '-1' if you would like to keep playing until quit entered: "))
while True:
    print("Number of wins: ", win_num)
    print("Number of losses: ", loss_num)
    if p_t_tracking == play_time:
        if win_num > loss_num:
            print("You are superior")
        elif win_num == loss_num:
            print("We are equal")
        else:
            print("I am superior")
        print("See ya next time :)")
        break
    user_input = input("Rock, Paper, Scissor, choose one: ")
    if user_input.lower().strip() == 'quit':
        if win_num > loss_num:
            print("You are superior")
        elif win_num == loss_num:
            print("We are equal")
        else:
            print("I am superior")
        print("See ya next time :)")
        break
    com = computer_choice()
    print("Computer chose: ", com)
    if user_input.lower().strip() == 'rock' and com == 'paper':
        print("You lose!")
        loss_num += 1
        p_t_tracking += 1
    elif user_input.lower().strip() == 'rock' and com == 'scissor':
        print("You win!")
        win_num += 1
        p_t_tracking += 1
    elif user_input.lower().strip() == com:
        print("Game Tied")
        p_t_tracking += 1
    elif user_input.lower().strip() == 'paper' and com == 'rock':
        print("You win!")
        win_num += 1
        p_t_tracking += 1
    elif user_input.lower().strip() == 'paper' and com == 'scissor':
        print("You lose!")
        loss_num += 1
    elif user_input.lower().strip() == 'scissor' and com == 'rock':
        print("You lose!")
        loss_num += 1
        p_t_tracking += 1
    elif user_input.lower().strip() == 'scissor' and com == 'paper':
        print("You win!")
        win_num += 1
        p_t_tracking += 1
    else:
        print("Invalid Input")