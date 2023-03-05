import random

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

#Picking a random word for the game.
gameWord = random.choice(wordsList)

gameWordList.extend(gameWord)

for letter in gameWordList:
  shownGameWord += "[ " + letter + " ] "

print(shownGameWord)

l1, l2, l3, l4, l5 = gameWordList

#Making sure the input is a 5 letters word
def guessWord():
  global guess
  guess = input("Guess the word: ").upper()

guessWord()

while True:
  if len(guess) != 5:
    print("The word is supposed to be 5 letters long.")
    guess = guessWord()
  else:
    break

guessList.extend(guess)

g1, g2, g3, g4, g5 = guessList

#enumerate() was used to keep track of the position of the letter in the for loop
for i, letter in enumerate(guessList):
  if letter == l1:
    guessList[i] = g1
  elif letter == l2:
    guessList[i] = g2
  elif letter == l3:
    guessList[i] = g3
  elif letter == l4:
    guessList[i] = g4
  elif letter == l5:
    guessList[i] = g5
if letter == gameWordList[i]:
	guessList[i] = green + letter + white
	      
for letter in guessList:
	shownGuess += "[ " + letter + " ] "
	
print(shownGuess)