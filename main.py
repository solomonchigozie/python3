import random
def get_choices():
    player_choice = input('Enter a choice (rock, paper, scissors) : ')
    # computer_choice = "paper"

    options = ['rock','paper','scissors']
    computer_choice = random.choice(options)

    choices = {"player":player_choice,"computer":computer_choice}

    return choices

def check_win(player, computer):
    print(f"You chose {player}, Computer chose {computer}")

    if player==computer:
        return "Its a tie"
    elif player == "rock":
        if computer == "scissors":
            return "Rock smashes scissors! You Win"
        else:
            return "Paper covers rock! you loose."
    elif player == "paper":
        if computer == "rock":
            return "Paper covers rock! you win"
        else:
            return "Scissors cuts paper! You loose."
    elif player == "scissors":
        if computer == "paper":
            return "Scissors cuts paper! you win"
        else:
            return "Rock smashes scissors! You loose"


choices = get_choices()
result = check_win(choices['player'], choices['computer'])
print(result)

# check_win("rock",'shoe'):



# dictionary
# dic = {"name":"jonh", "color":choices}

# list 
# food = ['pizza','egg','yam']
# dinner = random.choice(food)
