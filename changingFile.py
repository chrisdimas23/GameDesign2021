import time, sys, os

os.system('cls')
file="scoreSheet.txt"
FILE=open(file, 'r')
print(FILE.read())
FILE.close()
FILE=open(file, 'r')
contest_List=FILE.readlines()
# print(contest_List)
FILE.close()
# for element in contest_List:
#     print(element)
sorted_List=sorted(contest_List, reverse=False)[::-1]
# sorted_List=sorted(contest_List, key=lambda x: int(x.split()[4]), reverse=True)
for line in range(6):
    print(sorted_List[line])


# for element in sorted_List:
#     print(element)
