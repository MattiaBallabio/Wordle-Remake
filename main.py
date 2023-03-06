import random

#Game title, design-related purpose
def title():
  print('''
Generated ascii art
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
gameWord = random.choice(wordsList)
gameWordList.extend(gameWord)

#Design related purpose
for letter in gameWordList:
  shownGameWord += "[ " + letter + " ] "

#NEEDS TO BE REPLACED WITH BLANK LETTERS
#WHEN GAME IS COMPLETED
print(shownGameWord)

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
  
#enumerate() was used to keep track of the position of the letter in the for loop
  for i, letter in enumerate(guessList):
    if letter == g1:
      guessList[i] = l1
    elif letter == g2:
      guessList[i] = l2
    elif letter == g3:
      guessList[i] = l3
    elif letter == g4:
      guessList[i] = l4
    elif letter == g5:
      guessList[i] = l5
    if letter == gameWordList[i]:
  	  guessList[i] = green + letter + white

  '''
  for i, letter in enumerate(guessList):
    if letter in (l1, l2, l3, l4, l5):
      letter = guessList[i]
      guessList[i] = yellow + letter + white
  '''
  for letter in guessList:
  	shownGuess += "[ " + letter + " ] "
  	
  print(shownGuess)
  guessList.clear()

  match win:
    case True:
      break
    case False:
      pass