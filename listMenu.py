#Chris Dimas
#Menu with a list and 5 commands

myList = ["Mahogany, Birch, Oak, Cherry, Cedar"]
def menu():
    print("~~~MENU~~~")
    print("~~~List~~~")
    print("~~Append~~")
    print("~~Delete~~")
    print("~~~Find~~~")
    print("~~Index~~~")
    print("~~Reverse~")
    print("Enter either List, Append, Delete, Find, Index, Reverse or EX", end= " ")
    # x = str(input())
    # return x
print(menu())
x = str(input())
while x != "EX":
    if x == "EX":
        print(menu())
    if x == "List":
        print(myList[0:5])
        break
    if x == "Append":
        print("What would you like to append?)")
        pine=input()
        myList.append(pine)
        print(myList)
        break
    if x == "Delete":
        print("What would you like to delete?")
        delete=input()
        myList.remove(delete)
        print(myList)
        break
    if x == "Find":
        print("Select element index 0:4")
        y = int(input())
        print(myList[y])
        break
    if x == "Index":
        print("What item's index would you like to find?")
        wood=input()
        index = myList.index(wood)
        print(wood, index)
        break
    if x == "Reverse":
        myList.reverse()
        print(myList)
        break

        