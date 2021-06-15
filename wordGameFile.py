import random
def updateWord(word):
    for char in word:
        if char in guesses:
            print(char,end=' ')
        else:
            print('_', end=' ')

gameWords = ['burger','fries','milkshake','ketchup','chicken','canes','fiveguys','whataburger','pattymelt','plate','napkin','soda']
name = input("What is your name?")
print(name, end = "")
answer = input(", Do you want to play?").upper()
score=0
print("\n", gameWords)
while "Y" in answer:
    print(name, " Good Luck")
    word=random.choice(gameWords)
    turns=10
    guesses=''
    counter=len(word)
    updateWord(word)
    while turns >0 and counter>0:
        newGuess=input("\n Give me a letter")
        if newGuess not in guesses:
            if newGuess not in word:
                turns -=1
                print("Wrong! you have ", turns, "guesses left")
            else:
                counter -=word.count(newGuess)
                print("Nice guess!")
            guesses+=newGuess
        else:
            print("You used this one already!")
        updateWord(word)
    if counter == 0:
        print("Fantastic you are a champion")
        score +=1
        print("Score : ", score)
    else:
        print("You lost :(")
    answer=input("Do you want to play again?").upper()
print(name," Thank you for playing!")
print("Score : ", score)

ezLines=print(name, "\n" "~~~~~~\n", str(score), "\n")

import os
import sys
import time
import datetime

BOOK=open("scoreSheet.txt", 'w')
BOOK.writelines(str(ezLines))
BOOK.write(datetime)
time.sleep(1)
BOOK.close
