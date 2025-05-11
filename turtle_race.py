import turtle
import time
import random


WIDTH , HEIGHT = 500 , 500
COLORS = ['red', 'green', 'blue', 'orange', 'yellow', 'black', 'purple', 'cyan','pink', 'brown']



def no_of_racers(): 
   racers = 0
   while True:
      racers= input('enter the no. of  racers u want to race (2-10): ')
      if racers.isdigit():
         racers = int(racers)
      else:
         print('plz enter a no.!! ')
         continue
      
      if 2 <= racers <=10:
         return racers
      else:
         print('enter a valid no.!!')

def create_turtles(colors):
   turtles = []
   spacingx = WIDTH / (len(colors) + 1) 
   for i , color in enumerate(colors):
      racer = turtle.Turtle() 
      racer.color(color)
      racer.shape('turtle')
      racer.left(90)
      racer.penup()
      racer.setpos(-WIDTH//2 + (i + 1) * spacingx , -HEIGHT//2 + 20)
      racer.pendown()
      turtles.append(racer)
   return turtles

def race(colors):
   turtles = create_turtles(colors)

   while True:
      for racer in turtles:
         distance = random.randrange(1,20)
         racer.forward(distance)
         
         x , y = racer.pos()
         if y >= HEIGHT / 2 -10:
            return colors[turtles.index(racer)]


def init_turtle():
  
  screen =turtle.Screen()
  screen.setup(WIDTH,HEIGHT)
  screen.title('sex race')

racers = no_of_racers()
init_turtle()


random.shuffle(COLORS)
colors = COLORS[:racers]

winner = race(colors)
print(f'the winner is {winner}')
