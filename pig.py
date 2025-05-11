import random
import time

def roll():
   
   roll = random.randint(1,6)
   return roll

while True:
 players = input('enter the number of players (2-4):\n')
 time.sleep(1)
 if players.isdigit():
   players = int(players)
   if 2<= players <=4:
     print(f'alright!! total {players} players are playing. ')
     time.sleep(1)
     break
 else :
   print('enter valid numbers of palyers!!\ntry again !\n')
   time.sleep(1)

max_score = 50
player_score = [0 for i in range(players)]

while max(player_score) <  max_score:
  
 for i in range(players): 
  print(f'\nplayer number {i+1} turn has just started!')
  print(f'your total score is: {player_score[i]}\n')
  time.sleep(1)
  current_score = 0
  while True:
        
         dice_roll = input('would you like to roll the dice?? (y/n):\n').lower()
         if dice_roll != 'y':
          break
         value = roll() 
         if value == 1:
          current_score = 0
          print('you rolled 1! turn done!\n you lost all your scores!')
          break
         else:
          current_score  += value
          print(f'you rolled {value}')

         print(f'you score is {current_score}')
  player_score[i] += current_score
  print(f'your total scores is : {player_score[i]}')

max_score = max(player_score)
winning= player_score.index(max_score)
print(f'player {winning + 1} is the winner with the score of {max_score} ')