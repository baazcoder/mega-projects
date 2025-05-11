import random
import time

OPERATORS = ['+','-','/','*']
total_prblms = 10

def make_prblm():
   left = random.randint(3,12)
   right = random.randint(3,12)
   operator  = random.choice(OPERATORS)

   expr = str(left) +" "+ operator+" "+ str(right)
   ans = round(eval(expr),2)

   return expr,ans

wrong = 0
input('press enter to start! ')
print('----------------')

start_time = time.time()

for i in range (total_prblms):
   expr , ans = make_prblm()
   while True:
    
    guess = input(f'problem # {str(i+1)}: {expr} = ')
    if guess == str(ans):
      break
    wrong += 1 

end_time = time.time()
total_time = round(end_time-start_time,2)

print('----------')
print('nice work!')
print(f'you finished in {total_time} seconds!')