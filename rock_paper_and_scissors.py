import random

def play():
    user  = input("What's your choice? 'r' for rock, 'p' for paper, 's' for scissors")
    computer = random.choice(['r','s','p'])

    if user == computer:
        return 'its a Tie'
    
    if is_win(user,computer):
        return 'YOU WON'

    return 'YOU LOST'

def is_win(player,opponent):
    #return true if player wins
    #p>r, r>s, s>p
    if (player == 'r' and opponent == 's') or (player == 'p' and opponent == 'r') \
        or (player == 's' and opponent == 'p'):
        return True