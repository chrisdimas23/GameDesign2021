#Chris Dimas
#Word Game
#Create a list of words, randomly select a word from the list for user to guess
#Give the user some turns
#Show the word to the user with the characters guessed
#Play as long as the user has turns or has guessed the word

import random

gameWords = ['burger','fries','milkshake','ketchup','chicken','canes','fiveguys','whataburger','pattymelt','plate','napkin','soda']
name = input("What is your name?")
print(name, end = "")
answer = input(", Do you want to play?").upper()
print("\n", gameWords) #delete when code works properly
while "Y" in answer:
    print(name, " Good Luck")
    word=random.choice(gameWords)
    # print(word)
    turns=10  #find better way to create turns
    guesses=''
    counter=len(word)
    while turns >0 and counter>0:
        for char in word:
            if char in guesses:
                print(char, end=' ')
            else:
                print('_', end=' ')
        newGuess=input("\n Give me a letter")
        if newGuess not in word:
            turns -=1
            print("Wrong! you have ", turns, "guesses left")
        else:
            counter -=word.count(newGuess)
            print("Nice guess!")
        guesses+=newGuess
    answer=input("no")
print(name," Thank you for playing!")
        
        # if newGuess in word:
        #     counter-=1
        #     guesses += newGuess
        #     print("You are right!")
        # else:
        #     turns-=1
        #     print("Sorry, that is wrong. You still have", turns," turns")
        #     answer="n"
        #     print("goodbye")