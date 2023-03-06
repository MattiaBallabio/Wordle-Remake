import random

#Game title, design-related purpose
def title():
  print('''
██╗    ██╗ ██████╗ ██████╗ ██████╗ ██╗     ███████╗
██║    ██║██╔═══██╗██╔══██╗██╔══██╗██║     ██╔════╝
██║ █╗ ██║██║   ██║██████╔╝██║  ██║██║     █████╗  
██║███╗██║██║   ██║██╔══██╗██║  ██║██║     ██╔══╝  
╚███╔███╔╝╚██████╔╝██║  ██║██████╔╝███████╗███████╗
 ╚══╝╚══╝  ╚═════╝ ╚═╝  ╚═╝╚═════╝ ╚══════╝╚══════╝

██████╗ ███████╗███╗   ███╗ █████╗ ██╗  ██╗███████╗
██╔══██╗██╔════╝████╗ ████║██╔══██╗██║ ██╔╝██╔════╝
██████╔╝█████╗  ██╔████╔██║███████║█████╔╝ █████╗ 
██╔══██╗██╔══╝  ██║╚██╔╝██║██╔══██║██╔═██╗ ██╔══╝ 
██║  ██║███████╗██║ ╚═╝ ██║██║  ██║██║  ██╗███████╗
╚═╝  ╚═╝╚══════╝╚═╝     ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝
  ''')

#Input used to ask the user for a guess
def guessWord():
  global guess
  guess = input("Guess the word: ").upper()
  
#Variables
wordsList = []
gameWord = ""
gameWordList = []
guessList = []
shownGameWord = ""
shownGuess = ""

#List of colors.
green = "\033[32m"
yellow = "\033[33m"
white = "\033[0m"

#Generating a list with 5 letters words
#coming from a separate text file.
with open('words.txt','r') as file:
    for line in file:
        for word in line.split():
            wordsList.append(word.upper())


#MAIN
#Picking a random word for the game.
title()
gameWord = random.choice(wordsList)
gameWordList.extend(gameWord)

#Design related purpose
for letter in gameWordList:
  shownGameWord += "[ " + letter + " ] "

#Word to guess starts as 5 blank squares
print("[*] [*] [*] [*] [*]")

#Dividing the word into other variables
l1, l2, l3, l4, l5 = gameWordList

#Continuous input until players guesses the word.
win = False
while True:
  guessWord()

#Making sure the input is a 5 letters word
  while True:
    if len(guess) != 5:
      print("The word is supposed to be 5 letters long.")
      guess = guessWord()
    else:
      break
  
  guessList.extend(guess)
#Dividing the guess into 5 variables
  g1, g2, g3, g4, g5 = guessList

#Check if letter is in word
  if g1 in gameWordList and g1 != l1:
      g1 = yellow + g1 + white
  if g2 in gameWordList and g2 != l2:
      g2 = yellow + g2 + white
  if g3 in gameWordList and g3 != l3:
      g3 = yellow + g3 + white
  if g4 in gameWordList and g4 != l4:
      g4 = yellow + g4 + white
  if g5 in gameWordList and g5 != l5:
      g5 = yellow + g5 + white

  guessList.clear()

#Check if letter is in right place
  if g1 == l1:
    g1 = green + g1 + white
  if g2 == l2:
    g2 = green + g2 + white
  if g3 == l3:
    g3 = green + g3 + white
  if g4 == l4:
    g4 = green + g4 + white
  if g5 == l5:
    g5 = green + g5 + white

  guessList = [g1, g2, g3, g4, g5]
  
  for letter in guessList:
  	shownGuess += "[ " + letter + " ] "
  	
  print(shownGuess)
  guessList.clear()
  shownGuess = ""

  match win:
    case True:
      break
    case False:
      pass