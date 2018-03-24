import random

def is_valid_play(play):
    return play in ['rock', 'paper', 'scissors']

def random_play():
    return random.choice(['rock', 'paper', 'scissors'])

def determine_game_result(human, computer):
    if human == computer:
        return 'tie'
    elif human == "rock" and computer == "paper":
        return "computer"
    elif human == "rock" and computer == "scissors":
        return "human"
    elif human == "paper" and computer == "rock":
        return "human"
    elif human == "paper" and computer == "scissors":
        return "computer"
    elif human == "scissors" and computer == "rock":
        return "computer"
    elif human == "scissors" and computer == "paper":
        return "human"


def main(input=input):
    human = ''
    while not is_valid_play(human):
        human = input('rock, paper or scissors? ')

    computer = random_play()

    print(computer)

    result = determine_game_result(human, computer)
    if result == 'tie':
        print('it is a tie!')
    else:
        print(result, 'wins!')

#aby funkce main prosla testama - takovej tricek maincode
if __name__ == '__main__':
    main()
