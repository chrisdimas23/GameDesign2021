#Chris Dimas
#Word Game
#Create a list of words, randomly select a word from the list for user to guess
#Give the user some turns
#Show the word to the user with the characters guessed
#Play as long as the user has turns or has guessed the word
import os
import sys
import time
import datetime

file="scoreSheet.txt"

dt=datetime.datetime.now()
linef=str(dt.month)+"/"+str(dt.day)+"/"+str(dt.year)+"\t"+dt.strftime("%A")+"\t"

def printScore(score):
    FileRead=open(file,'r')
    print(FileRead.read())
    FileRead.close()

def updateScore(score):
    Filewrite=open(file,'a')
    line=name+"\t"+linef+"\t\t"+str(score)
    Filewrite.write("\n"+line)
    Filewrite.close()
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
print("\n", gameWords) #delete when code works properly
while "Y" in answer:
    print(name, " Good Luck")
    word=random.choice(gameWords)
    # print(word)
    turns=10  #find better way to create turns
    guesses=''
    counter=len(word)
    updateWord(word)
    while turns >0 and counter>0:
        # for char in word:
        #     if char in guesses:
        #         print(char, end=' ')
        #     else:
        #         print('_', end=' ')
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
printScore(score)
updateScore(score)



import os
import sys
import time
import datetime



file="scoreSheet.txt"

# dt=datetime.datetime.now()
# linef=str(dt.month)+"/"+str(dt.day)+"/"+str(dt.year)+"\t\t"+dt.strftime("%A")+"\t"




# def printScore():
#     FileRead=open(file,'r')
#     print(FileRead.read())
#     FileRead.close()

# def updateScore(score):
#     Filewrite=open(file,'a')
#     line=name+"\t"+linef+"\t"+int(score)
#     Filewrite.write("\n"+line)
#     Filewrite.close()




        # if newGuess in word:
        #     counter-=1
        #     guesses += newGuess
        #     print("You are right!")
        # else:
        #     turns-=1
        #     print("Sorry, that is wrong. You still have", turns," turns")
        #     answer="n"
        #     print("goodbye")