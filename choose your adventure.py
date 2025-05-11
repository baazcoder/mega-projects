import time

name = input(' enter your name: ')

time.sleep(1)
print(f'welcome {name} to the adventure!!')
time.sleep(1)

while True:
  ans = input('you are on the way to batala, decide if you want to have a therapy session or wanna meet asees, enter therapy or asees : \n ').lower()
  time.sleep(1)
  if ans == 'therapy':
      ans=input('you reached the hospital, enter continue to continue the therapy or leave to meet asees: \n ')
      if ans == 'continue':
          print(' you get bored, and died due to asees craving')
      elif ans == 'leave':
          print('you have wasted so much time ,asees is busy now , you lost ')
      else :
          print('enter a valid choice')
  elif ans =='asees':
   while True:
        ans = input('okay so call her and tell her to meet \n by which contact u wanna call her?? panda or pipoo :\n ')
        time.sleep(1)
        if ans == 'panda':
            print('her mom picked the call and asking you , who are u!!\n busted')
        elif ans == 'pipoo':
            print('asees picked the call , she is waiting for you near her tution')
            time.sleep(1)
            ans = input('where u guys wanna hang out?? (shubash park/ roam around) : \n')
            time.sleep(1)
            while True :
             if ans == 'roam around':
                 print('you were roaming around a particular area, she got bored and left, YOU LOSE ')
             elif ans == 'shubash park':
                 print("you guys are now in the park and walking around .")
                 time.sleep(1)
                 print('she seems nervous and is not talking much')
                 time.sleep(1)

                 while True:
                  ans = input('act serious to look mature or nonchalant to make her feel comfortable (serious/nonchalant).\n')
                  time.sleep(1)
                  if ans == 'serious':
                      print('you acted like a mature boy which was very boring , she did not like your company and left!! you lost')
                  elif ans == 'nonchalant':
                      print('you acted like a kid which seemed to be funny to her and she enjoyed your company')
                      time.sleep(1)
                      break
                  else :
                      print('enter a valid choice')
                 while True:
                    ans = input("you guys have no photo together. do you wanna ask if we can click some??.(yes/no)\n")
                    time.sleep(1)
                    if ans == 'no':
                       print('she also wanted to click pics but u r dick u didnt asked . you lost!!')
                    elif ans == 'yes':
                       print('you : asees can we click some pics together to capture this beautiful day??')
                       time.sleep(1)
                       print('asees : ohh i was thinking the same, why not less go!')
                       break
                       
                    else:
                       print('invalid option')
                 while True:
                    print('asses is clicking your funny pics, in which you are looking joker.')
                    time.sleep(1)
                    ans = input('say her to stop this crap or let her enjoy because she is looking very happy(stop/let her enjoy) \n')
                    time.sleep(1)
                    if ans == 'stop':
                       print('you : asees stop humilating me, i dont like when someone takes my weird pics!! huhh \n')
                       time.sleep(1)
                       print('asees : muh vekhya e apna bandra jya! jaa daffa labb la koi jehdi nhi khichdi huhhh. you lost \n')
                    elif ans == 'let her enjoy':
                       print('you : hawwww krn dyi a! lemme act like a gay.\n')
                       time.sleep(1)
                       print('asees: yarrr tu pagal aa?? \n')
                       break 
                    else:
                       print('invalid option')
                #  while True
        #      else:
        #          print('invalid choice')
        # else:
        #         # print('invalid choice')
         
  else :
    print('enter valid choice!! ')

          