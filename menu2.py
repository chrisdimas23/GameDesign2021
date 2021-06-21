# Chris Dimas
# Starting from lucas code
# While loop is a loop until condition is met
varChoice=""
def menu():
    print("*"*28)
    print("*"," "*6,"Capitalization"," "*6,"*")
    print("*"," "*9,"Menu"," "*9,"*")
    print("*"," "*24,"*")
    print("*"," "*2,"L1- capitalize"," "*3,"*")
    print("*"," "*2,"L2- level 2"," "*5,"*")
    print("*"," "*2,"L3- level 3"," "*7,"*")
    print("*"," "*2,"EX- level 4"," "*7,"*")
    print("*"*28)
    print("Enter either L1,L2,L3,or EX", end= " ")
    varChoice = str(input())
    return varChoice

while varChoice != "EX":
    if varChoice == "L1":
        print("You are in level 1")
    if varChoice == "L2":
        print("You are in level 2")
    if varChoice == "L3":
        print=score
    def score():
        print("Your scores:")
        print("23434  Peter")
        print("15678  Maria")
        print("9043   Chris")
        print("4569   Lucas")
        print("934    Ben")

        
varChoice = str(input())
print("Goodbye, Have a nice day")

def gamePause():
    print("do you want to change levels?")
    level=input()
    if level !='no':
        varChoice=menu()
varChoice=menu() #call function

while varChoice!="EX":
    if varChoice == "L1":
        print("you are in level 1")
        answer=input()
        answer=answer.capitalize()
        print(answer)
        gamePause()

while varChoice!="EX":
    if varChoice == "L1":
        convert=True #boolean variable true or false
        while convert:
            print("you are in level 1")
            print("please enter a phrase")
            answer=input()
            answer=answer.capitalize()
            print(answer)
            convert=gamePause()

