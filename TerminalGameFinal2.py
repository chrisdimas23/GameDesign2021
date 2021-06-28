#Chris Dimas
#6-25-21
#Trivia game with levels that increase in difficulty
#In order to access next level, level has to be unlocked by correctly guessing a certain number of questions correctly

import os, sys, datetime, time, random

file="scoreSheet.txt"

dt=datetime.datetime.now()
linef=str(dt.month)+"/"+str(dt.day)+"/"+str(dt.year)+"\t"+dt.strftime("%A")+"\t"

def updateScore(score):
    Filewrite=open(file,'a')
    line=name+"\t"+linef+"\t\t"+str(score)
    Filewrite.write("\n"+line)
    Filewrite.close()

def instructions():
    print("All answers must begin with a capital letter. Special instructions will be given with certain questions. Yes or no questions can be answered with Y or N. If you fail to qualify for one level, you will need to complete all other levels again to prevent score boosting. Good luck!")

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

print("******Menu*******")
print("*****Level1******")
print("*****Level2******")
print("*****Level3******")
print("*****Level4******")
print("***Instructions**")
print("***ScoreSheet****")
print("Warning: all inputs must be capitalized")
name = input("What is your name?")
print(name, end = "")
answer = input(", Input Y to begin, input Instructions for instructions, or input ScoreSheet to see scores.")
if answer == "Instructions":
    instructions()
    answer28 = input("Go back?").upper()
if answer == "ScoreSheet":
    os.system('cls')
    file="scoreSheet.txt"
    # FILE=open(file, 'r')
    # print(FILE.read())
    # FILE.close()
    FILE=open(file, 'r')
    contest_List=FILE.readlines()
    FILE.close()
    sorted_List=sorted(contest_List, reverse=False)[::-1]
    for line in range(6):
        print(sorted_List[line])
    answer29 = input("Go back?").upper
while "Y" in answer:
    score=0
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
    print(score)
    if score >= 3:
        answer21=input("Would you like to continue?")
        if answer21 == "N":
            Filewrite=open(file,'a')
            line=name+"\t"+linef+"\t\t"+str(score)
            Filewrite.write("\n"+line)
            Filewrite.close()
            sys.exit()
        while "Y" in answer:
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
            print(score)
            if score >= 6:
                answer23=input("Would you like to continue?")
                if answer23 == "N":
                    Filewrite=open(file,'a')
                    line=name+"\t"+linef+"\t\t"+str(score)
                    Filewrite.write("\n"+line)
                    Filewrite.close()
                    sys.exit()
                while "Y" in answer:
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
                    print(score)
                    if score >= 9:
                        answer25=input("Would you like to continue?")
                        if answer25 == "N":
                            Filewrite=open(file,'a')
                            line=name+"\t"+linef+"\t\t"+str(score)
                            Filewrite.write("\n"+line)
                            Filewrite.close()
                            sys.exit()
                        while "Y" in answer:
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
                            print(score)
                            print("Excellent job! If you made it this far, then you must be a trivia master!")
                            answer27 = input("Would you like to return to the menu?").upper()
                            if answer27 == "N":
                                print("Thanks for playing!")
                                sys.exit()
                        else:
                            answer26 = input("Sorry, you did not score high enough! Would you like to try again?").upper()
                            if answer26 == "N":
                                Filewrite=open(file,'a')
                                line=name+"\t"+linef+"\t\t"+str(score)
                                Filewrite.write("\n"+line)
                                Filewrite.close()
                                sys.exit()                               
                    else:
                        answer24 = input("Sorry, you did not score high enough! Would you like to try again?").upper()
                        if answer24 == "N":
                            Filewrite=open(file,'a')
                            line=name+"\t"+linef+"\t\t"+str(score)
                            Filewrite.write("\n"+line)
                            Filewrite.close()
                            sys.exit()
    else:
        answer22 = input("Sorry, you did not score high enough! Would you like to try again?").upper()
        if answer22 == "N":
            Filewrite=open(file,'a')
            line=name+"\t"+linef+"\t\t"+str(score)
            Filewrite.write("\n"+line)
            Filewrite.close()
            sys.exit()
            
