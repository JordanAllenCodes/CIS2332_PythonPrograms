# Jordan Allen

# import csv module and OrderedDict subclass
import csv
from collections import OrderedDict


def word_frequency():  # use function to calculate word frequency
    # create list of words from csv file then create an identifier for the ordered dictionary
    wordfreq = []
    dic = OrderedDict()
    # open and read the cvs file
    with open(file_name, 'rt') as f:
        file = csv.reader(f)
        for line in file:
            wordfreq = line
    # iterate every word in wordfreq. add 1 everytime word is in the dictionary. else add word with value 1.
    for word in wordfreq:
        if word in dic:
            dic[word] = dic[word] + 1
        else:
            dic[word] = 1
# display results with key value
    for count in list(dic.keys()):
        print(count, dic[count])


if __name__ == '__main__':
    file_name = 'input1.csv'
    word_frequency()
