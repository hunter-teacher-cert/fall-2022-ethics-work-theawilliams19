# FILENAME: nim.py
# First Last: Théa Williams
# CSCI 77800 Fall 2022
# collaborators: 
# consulted: thinkcspy text, Datacamp Intro to Python course

import random

stones = 12 #total stones at start of game

#loop util game ends
while stones > 0 : # the colon (:) lets you know your in a block or function, and you stay in it until your tab ends
  #prompt for use input (user turn - a  move = taking 1-3 stones
  userStonesTaken = input("Your turn, pick between 1 and 3 stones to remove.") #the input function includes print functionality, so an extra print function isn't necessary.
  userStonesTaken = int(userStonesTaken)
  
  #calculate number of stones remaining, print
  stones = stones - userStonesTaken #python doesn't use the same shortcut operators as Java, e.g. -=

  print("You have selected " + str(userStonesTaken)) 
  print("There are " + str(stones) + " remaining. ")

  #check for win
  if stones <= 0:
    print("You win!")
    break

  #machine turn
  machineStonesTaken = random.randrange(1,4)
  print("The computer has chosen " + str(machineStonesTaken))

  #calculate number of stones remaining, print  
  stones = stones - machineStonesTaken
  print("There are " + str(stones) + " remaining. ")

  #check win
  if stones <= 0:
    print("Computer Wins! Sorry, better luck next time. :(")