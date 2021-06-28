#Chris Dimas
#6-25-21
#Trivia game with levels that increase in difficulty
#In order to access next level, level has to be unlocked by correctly guessing a certain number of questions correctly

import os, sys, datetime, time, random

file="scoreSheet.txt"

dt=datetime.datetime.now()
linef=str(dt.month)+"/"+str(dt.day)+"/"+str(dt.year)+"\t"+dt.strftime("%A")+"\t"

answer1 = "Hornet"
answer2 = "Yes"
answer3 = "Addison"
answer4 = "Texas"
answer5 = "Yellow"
answer6 = "Gold"
answer7 = "Performing"
answer8 = "1950"
answer9 = "Yes"
answer10 = "1"
answer11 = "8"
answer12 = "Fulton"
answer13 = "PES"
answer14 = "Random"
answer15 = "Yes"
answer16 = "14"
answer17 = "Per Aspera Ad Astra"
answer18 = "Peahen"
answer19 = "7"
answer20 = "10110010111"

score = 0

check = False

def menu():
    print("******Menu*******")
    print("*****Level1******")
    print("*****Level2******")
    print("*****Level3******")
    print("*****Level4******")
    print("***ScoreSheet****")
    print("Warning: all inputs must be capitalized")



def level1():
    score = 0
    print("Hello, welcome to Level 1 : Easy mode")
    newGuess1=input("What is Greenhill's mascot?")
    if newGuess1 in answer1:
        print("Great job!")
        score += 1
    else:
        print("Sorry, that's wrong!")

    newGuess2=input("Does Mrs. Suarez teach game design?")
    if newGuess2 in answer2:
        print("Great job!")
        score += 1
    else:
        print("Sorry, that's wrong!")
    
    newGuess3=input("Where is Greenhill located?")
    if newGuess3 in answer3:
        print("Great job!")
        score += 1
    else:
        print("Sorry, that's wrong!")

    newGuess4=input("What state is Austin located in?")
    if newGuess4 in answer4:
        print("Great job!")
        score += 1
    else:
        print("Sorry, that's wrong!")

    newGuess5=input("What color is the sun?")
    if newGuess5 in answer5:
        print("Great job!")
        score += 1
    else:
        print("Sorry, that's wrong!")
    print("If you answered 3/5 correctly, the next level will be unlocked!")
    print(score)
    if score >= 3:
        check = True
    mainMenu()

def level2():
    print("Hello, welcome to Level 2 : Medium mode")
    newGuess6=input("What is Greenhill's secondary color (primary being green)?")
    if newGuess6 in answer6:
        print("Great job!")
        score += 1
    else:
        print("Sorry, that's wrong!")
    
    newGuess7=input("Fill in the blank: Marshall __________ Arts Center")
    if newGuess7 in answer7:
        print("Great job!")
        score += 1
    else:
        print("Sorry, that's wrong!")
    
    newGuess8=input("What year was Greenhill founded in?")
    if newGuess8 in answer8:
        print("Great job!")
        score += 1
    else:
        print("Sorry, that's wrong!")

    newGuess9=input("Is a keyboard an input device?")
    if newGuess9 in answer9:
        print("Great job!")
        score += 1
    else:
        print("Sorry, that's wrong!")

    newGuess10=input("How many computer science credits are required to graduate from greenhill?")
    if newGuess10 in answer10:
        print("Great job!")
        score += 1
    else:
        print("Sorry, that's wrong!")

def level3():
    print("Hello, welcome to Level 3 : Hard mode")
    newGuess11=input("How many bits are in a byte?")
    if newGuess11 in answer11:
        print("Great job!")
        score += 1
    else:
        print("Sorry, that's wrong!")
    
    newGuess12=input("What is the last name of greenhill's founder?")
    if newGuess12 in answer12:
        print("Great job!")
        score += 1
    else:
        print("Sorry, that's wrong!")
    
    newGuess13=input("What is the acronym for the name of the highschool south of Greenhill? (all caps)")
    if newGuess13 in answer13:
        print("Great job!")
        score += 1
    else:
        print("Sorry, that's wrong!")

    newGuess14=input("Fill in the blank: ______ access memory")
    if newGuess14 in answer14:
        print("Great job!")
        score += 1
    else:
        print("Sorry, that's wrong!")

    newGuess15=input("Is Visual Studio software?")
    if newGuess15 in answer15:
        print("Great job!")
        score += 1
    else:
        print("Sorry, that's wrong!")

def level4():
    print("Hello, welcome to Level 4 : Impossible mode")
    newGuess16=input("What number does E represent in hexadecimal?")
    if newGuess16 in answer16:
        print("Great job!")
        score += 1
    else:
        print("Sorry, that's wrong!")
    
    newGuess17=input("What is Greenhill's motto?")
    if newGuess17 in answer17:
        print("Great job!")
        score += 1
    else:
        print("Sorry, that's wrong!")
    
    newGuess18=input("What is the name for the female counterpart of the birds that are found on Greenhill's campus?")
    if newGuess18 in answer18:
        print("Great job!")
        score += 1
    else:
        print("Sorry, that's wrong!")

    newGuess19=input("How many bits is ASCII?")
    if newGuess19 in answer19:
        print("Great job!")
        score += 1
    else:
        print("Sorry, that's wrong!")

    newGuess20=input("What is 1431 in binary?")
    if newGuess20 in answer20:
        print("Great job!")
        score += 1
    else:
        print("Sorry, that's wrong!")


def mainMenu():
    name = input("What is your name?")
    print(name, end = "")
    answer = input(", select a level.")

    if answer == "Level1":
        level1()

    if answer == "Level2":
        if score > 2:
            level2()
        else:
            print("Sorry, this level is still locked!")
            mainMenu()

    if answer("Level3"):
        if score > 5:
            level3()
        else:
            print("Sorry, this level is still locked!")

    if answer("Level4"):
        if score > 8:
            level4()
        else:
            print("Sorry, this level is still locked!")
menu()
mainMenu()