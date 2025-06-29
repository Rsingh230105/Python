'''import random as r
n=int(input("Enter the number :"))
print( 1.Rock
2.Paper
    3.Scissor)
c=r.randint(1,3)
print(c)
if c==1:
    if n==2:
        print('Paper win')
elif c==2:
    if n==3:
        print('scissor win')
elif c==3:
    if n==1:
        print('Rock Win')
elif c==n:
    print('Toe')
else:
    print('Wrong input please enter 1 to 3 only')
'''
#---------------------------------------------------------------------
import random
l=["rock","paper","scissor"]

while True:
    ccount=0
    ucount=0
    uc=int(input('''Game start..
                     1.Yes
                     2.No
                              '''))
    if uc==1:
      for a in range(1,6):# 5 round
          userInput=int(input('''
          1.Rock
          2.Paper
          3.Scissor
                    '''))
          if userInput==1:
              uchoice="rock"
          elif userInput==2:
              uchoice="paper"
          elif userInput==3:
              uchoice="scissor"
          Cchoice=random.choice(l)
          #print(uchoice)
          #print(Cchoice)
          if Cchoice==uchoice:
                  print("Computer Value:",Cchoice)
                  print("User Value:",uchoice)
                  print("Game Draw")
                  ucount=ucount+1
                  ccount=ccount+1

          elif (Cchoice=="rock" and uchoice=="paper") or (Cchoice =="paper" and uchoice=="scissor") or (Cchoice=="scissor" and uchoice=="rock" ):
                  print("Computer Value:",Cchoice)
                  print("User Value:",uchoice)
                  print("You win")
                  ucount=ucount+1
          else:
                  print("Computer Value:",Cchoice)
                  print("User Value:",uchoice)
                  print("Computer Win")
                  ccount=ccount+1

      if ucount==ccount:
          print("Final Game draw")
          print("User Score:",ucount)
          print("Computer Score:",ccount)
      elif ucount>ccount:
          print("FInal You Win The game")
          print("User Score:",ucount)
          print("Computer Score:",ccount)
      else:
          print("Final Computer Win the game")
          print("User Score:", ucount)
          print("Computer Score:", ccount)





    else:
        break

