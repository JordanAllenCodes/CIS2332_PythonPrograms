# Jordan Allen
# ZyLabs 11.22

words = input()  # get words from input

newList = words.split(' ')  # create a list of the words

for i in newList:  # for each word in the list print the word with its count
    print(i, newList.count(i))
