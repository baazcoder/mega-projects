import random

user_wins = 0
computer_wins = 0

options = ['rock','paper','scissors']


while True:
    
    user = input('select rock/paper/scissors or Q to quit the game.\n').lower()
    if user == 'q':
        break
    elif user not in options:
        
        continue

    r = random.randint(0,2)
    # 0 = rock
    # 1 = papper
    # 2 scissors
    c = options[r] # c = computer's choice
    print('computer picked', c)
    if c == 'rock' and user == 'paper':
        print(f'you chose {user} computer chose {c}\n you wins')
        user_wins += 1
    elif c == 'paper' and user == 'scisoors':
        print(f'you chose {user} computer chose {c}\n you wins')
        user_wins += 1
    elif c == 'scissors' and user == 'rock':
        print(f'you chose {user} computer chose {c}\n you wins')
        user_wins += 1
    elif c == user :
        print('its is TIE!!')
    else:
        print('you lost!!')
        computer_wins += 1

print(f'you won {user_wins} times . computer won {computer_wins} times')
print('naa khed lodeya')

    

