# Jordan Allen
# ZyLabs 11.18

userNumbers = input()  # get values
originalList = userNumbers.split()  # split user input

new_list = []  # new list to hold applicable values

for i in originalList:  # if true
    if int(i) >= 0:
        new_list.append(int(i))  # add to new list

new_list.sort()  # sort new list

for i in new_list:
    print(i, end=' ')
