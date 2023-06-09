# Jordan Allen
# zyLabs 12.9: Exception handling to detect input string vs integer

def main():  # use function (or the list will not be accessible)
    input_list = []  # create list
    row = ""  # hold each row of input
    while row != '-1':  # accept row
        row = input()  # get row
        if row != '-1':  # accept row
            input_list.append(row)  # add to list
    for row in input_list:
        words = row.split()  # split row
        name = words[0]  # hold name
        while row:
            try:  # test code and find errors
                age = int(words[1]) + 1  # get age and add 1, hold age
                print(name, age)  # successful
                break
            except ValueError:  # manage error
                age = 0  # only taking first input from split, age automatically sets to 0
            print(name, age)
            break


main()
