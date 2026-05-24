#WIP IM NOT DONE WITH THIS YET SO DON'T DO NOTHING TO IT
#THIS IS NOT A SLOT MACHINE THIS IS A 
#Scrolling Contraption O' The Lifting Ability (of) Non-assured Donations
#or S.C.O.T.L.A.N.D for short

#HEY YOU SCROLL DOWN WHEN RUNNING IT FOR SOMEONE ELSE
# SO THEY DON'T SEE THE CODE 
#INCASE THEY SOMEHOW KNOW HOW TO READ PYTHON
#AND ASK YOU A BUNCH OF QUESTIONS LIKE
#Did you code that?
#Did you use ai to make that?
#"""Gambling""" is allowed? (prolly no but dont ask or ts gets shut down)
import random
import time
import sys

R = (random.randrange(1, 5))
#makes the scotland 20 times
for i in range(20):
  #ASSIGNS A RANDOM NUMBER FROM 1 TO 100 (101 just sets the cap to below 101)
  x = (random.randrange(1, 101))
  y = (random.randrange(1, 101))
  z = (random.randrange(1, 101))
  #ASSIGNS SYMBOL TO CERTAIN NUMBER GENERATED FOR THE FIRST VARIABLE
  #hahaha im evil and this is making it harder for them 2 win hahaha
  Y = 2
  #if x == z and x == y and R == 1 or 2 or 3 or 4 or 5 or 6:
   # if z < 50:
     # z = (random.randrange(50, 101))
     # Y = 1
    #else:
     # z = (random.randrange(1, 50))
      #Y = 1
  if x in range(1, 11):
    xR = ("[🍇]")
  if x in range(11, 21):
    xR = ("[🍒]")
  if x in range(21, 31):
   xR = ("[🥭]")
  if x in range(31, 41):
    xR = ("[🍎]")
  if x in range(41, 51):
   xR = ("[🍍]")
  if x in range(51, 61):
   xR = ("[🍌]")
  if x in range(61, 71):
    xR = ("[🫐]")
  if x in range(71, 81):
   xR = ("[🍉]")
  if x in range(81, 91):
   xR = ("[🍊]")
  if x in range(91, 97):
   xR = ("[💸]")
  if x in range(97,100):
    xR = ("[💎]")
  if x == 100:
   xR = ("[7️⃣]")
#same thing but for the second variable
  if y in range(1, 11):
   yR = ("[🍇]")
  if y in range(11, 21):
    yR = ("[🍒]")
  if y in range(21, 31):
     yR = ("[🥭]")
  if y in range(31, 41):
   yR = ("[🍎]")
  if y in range(41, 51):
     yR = ("[🍍]")
  if y in range(51, 61):
    yR = ("[🍌]")
  if y in range(61, 71):
    yR = ("[🫐]")
  if y in range(71, 81):
   yR = ("[🍉]")
  if y in range(81, 91):
    yR = ("[🍊]")
  if y in range(91, 97):
    yR = ("[💸]")
  if y in range(97, 100):
    yR = ("[💎]")
  if y == 100:
   yR = ("[7️⃣]")
#same thing but for the third variable
  if z in range(1, 11):
    zR = ("[🍇]")
  if z in range(11, 21):
   zR = ("[🍒]")
  if z in range(21, 31):
   zR = ("[🥭]")
  if z in range(31, 41):
    zR = ("[🍎]")
  if z in range(41, 51):
    zR = ("[🍍]")
  if z in range(51, 61):
      zR = ("[🍌]")
  if z in range(61, 71):
      zR = ("[🫐]")
  if z in range(71, 81):
   zR = ("[🍉]")
  if z in range(81, 91):
    zR = ("[🍊]")
  if z in range(91, 97):
   zR = ("[💸]")
  if z in range(97, 100):
    zR = ("[💎]")
  if z == 100:
      zR = ("[7️⃣]")
      
  #DONT LET ANYONE SEE THING BUT 777 IS LITERALLY A 1 IN A MILLION
  #LIKE STATISTICALLY IT IS STRAIGHT UP 1/1,000,000
  
  #lowk doesn't work 👇
  #del Line1
 # del Line2
 # del Line3
 # del Line4
#  del Line5
 # del Line6
  #del Line7
 # del Line2b
 
  #change the last number +1 in the "range(1, 12)"
  #to change the chances for the system to actually let wins
  if xR == yR and xR == zR and R in range(1, 4):
    if xR == ("[🍇]"):
      zR = ("[🍒]")
      Y = 1
    else:
      zR = ("[🍇]")
      Y = 1
  print("")
  print("")
  print("")
  print("")
  print("")
  print("")
  print("Scotland")
  print("")
  print("")
  print("")
  print(R)
  print("")
  print("")
  print("")
  print("")
  print("")
  print("")
  print("")
  Line1 = ("3 matching fruits is 4th reward")
  Line2 = ("3 matching dollars is 3rd reward")
  Line2b = ("3 matching diamonds is 2nd reward")
  Line3 = ("3 matching '7's is 1st reward")
  Line4 = ("")
  Line5 = ("|======================|")
  Line6 = (xR, yR, zR)
  Line7 = ("|======================|")
  print(Line1)
  print(Line2)
  print(Line2b)
  print(Line3)
  print(Line4)
  print(Line5)
  print(Line6)
  print(Line7)
  print("")
  L2 = ("")
  L1 = ("1")
  L3 = ("2")
  C = ("3 fruits is 0.1%, 3 Dollas is 0.08%, 3 diamonds is 0.01%, 3 '7's is 0.001%")
  if xR == yR:
    if yR == zR:
      print("winner winner chicken dinner 🤑")
    else:
      if Y == 2:
        print(L1)
  else:
    if xR == zR:
      print(L2)
    else: print(L2)
    
  if Y == 1:
    print(L3)
  print("")
  print("")
  time.sleep(0.1)

#doesnt work at all 👇  
  
#for i in range(9):
#def delete_last_line():
  #sys.stdout.write('\x1b[1A')
  #sys.stdout.write('\x1b[2K')
  #sys.stdout.flush()



#LOTTERYLOTTERYLOTTERYLOTTERYLOTTERYLOTERY

#LOTTERYLOTTERYLOTTERYLOTTERYLOTTERYLOTTERYLOTTERYLOTTERYLOTTERY

#LOTTERYLPTTERYLOTTERYLOTTERYLOTTERY


#THERES A CHANCE YOU get Money NONEY MONEY MONEY
#LOTTERYLPTTERYLOTTERYLOTTERYLOTTERY











































