import random

r = random.randint(0,100)

print('hey! welcome to guess the number game')
print('RULE :- \n You have to guess the number in less than 10 attempts')
a= input('do u want to play this game??\n')

if a != 'yes':
    quit()
else:
    print("let's start the game")

attempts = 0


while True:
   attempts +=1
   guess= int(input('guess any number between 0-100!\n'))
   if guess > 100:
       print('make sure to type b/w 0-100 next time')
       quit()
   
   elif guess > r:
        print('ur guess is too high!')
        
   elif guess<r:
        print('ur guess is too low')
        
   else :
        print('congo!! u have guessed the number')
       
        break

print(f'u guessed the no. {r} in {attempts} attempts')
if attempts <= 10:
    print('you won!!')
else :
    print('you lose, better luck next time')

 