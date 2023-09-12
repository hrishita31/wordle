BG_GREEN = "\u001b[32m"
BG_YELLOW = "\u001b[43m"
RESET = "\u001b[0m"
print("LET'S PLAY A WORDLE GAME!")

import csv
import random
import pandas as pd

words = []
#reading the csv file
with open("5_letters.csv", 'r') as f:
  csvreader = csv.reader(f)
  for row in csvreader:
    if row:
        words.append(row[0])

#randomly chosing a word from the csv file
correct = random.choice(words)
#print(f"Randomly chosen word is: {correct}")
print("A word has been randomly generated so let's begin the guessing game!")

data = pd.read_csv("5_letters.csv")
#data

print("Start guessing!")

for j in range(6):
    guess = input("Guess the word: ").lower()
    #check each letter
    for i in range(0, 5):
        if guess[i] == correct[i]:
            print(f"{BG_GREEN}{guess[i]}{RESET}", end="")
        elif guess[i] in correct:
            print(f"{BG_YELLOW}{guess[i]}{RESET}", end="")
        else:
            print(guess[i], end="")

    print()

    #check if guess is correct
    if guess == correct:
        print("You win!Congratulations!")
        exit()

print("You lose! Better luck next time!")
print(f"The correct word was {correct}")

