print('welcome to the game')

playing = input('do u wanna play? \n')

if playing.lower() != 'yes':
    quit()
print('u said yuss hurahhh!!, lets playy' )

score =0
wrong = 0
answer1 = input('Q:- what is the CPU sttands for?? \nAns:-')
if 'central processing unit' in answer1.lower():
    print('right ahhh!!, wet krta')
    score+=1
else:
    print('o jaa yr cse kinne rkha ti')
    wrong+=1


answer2 = input('Q:-how many gurus is there in sikhism \nAns:-')
if '10' in answer2.lower():
    print('wahhhhhhhhguru seeengh')
    score+=1

else:
    print('sala bhappa')
    wrong+=1


answer3 = input('Q:- what is combination of seven colours called??\nAns:- ')

if 'vibgyor' in answer3.lower():
    print('o balle tere satrange ')
    score+=1
else:
    print('naa pra')
    wrong+=1



answer4 = input('Q:- asees da nalda kon\nAns:- ')
answer4=answer4.lower()
if 'shehbaz' in answer4:
    print('hn hn pta yarr')
    score+=1
else:
    print('salya shitr kahne e')
    wrong+=1



answer5 = input('Q:- asees kinnu pyaar krdi?\nAns:-')
answer5=answer5.lower()
if 'shehbaz ' in answer5:
    print('yussss syi kya')
    score+=1
else:
    print('o chl muh vekhya one')
    wrong+=1



answer6 = input('Q:- 3 phase ch kinniya windings hundiya?\nAns:-')
answer6=answer6.lower()
if '3' in answer6:
    print('gud electrician saab')
    score+=1
else:
    print('hai sal gendu')
    wrong+=1



answer7 = input('Q:- asees ne kithe jana padhn??\nAns:-')
answer7=answer7.lower()
if 'delhi' in answer7:
    print('hnn yrr tnu vi jana pena')
    score+=1
else:
    print('nhi pra')
    wrong+=1


print(f'your score =  {score}\nwrong answers = {wrong}')
print(f'u got {(score/7)*100} % out of 100')