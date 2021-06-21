#Chris Dimas
#Menu with a list and 5 commands

myList = ["Mahogany", "Birch", "Oak", "Cherry", "Cedar"]
def menu():
    print("~~~MENU~~~")
    print("~~~List~~~")
    print("~~Append~~")
    print("~~Delete~~")
    print("~~~Find~~~")
    print("~~Index~~~")
    print("~~Reverse~")
    print("Enter either List, Append, Delete, Find, Index, Reverse or EX", end= " ")
    x = (input())
    return x
x=menu().upper()

while x != "EX":
    if "LI" in x:
        print(myList[0:5])
    if "APP" in x:
        print("What would you like to append?)")
        pine=input()
        myList.append(pine)
        print(myList)
    if "DEL" in x:
        print("What would you like to delete?")
        delete=input().capitalize()
        myList.remove(delete)
        print(myList)
    if "FI" in x:
        print("Select element index 0:4")
        y = int(input())
        print(myList[y])
        x=menu().upper()
    if "IN" in x:
        print("What item's index would you like to find?")
        wood=input()
        index = myList.index(wood)
        print(wood, index)
    if "REV" in x:
        myList.reverse()
        print(myList)
    x=menu().upper()
# print("Would you like to return to the menu or switch to a different level?")
# x = str(input())
        