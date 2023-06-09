# Jordan Allen
# zyLabs 14.11: Descending selection sort with output during execution

def selection_sort_descend_trace(integers):
    for i in range(len(integers) - 1):  # find integer of the greatest value
        greatest_value = i  # hold current integer of the greatest value
        for num in range(i + 1, len(integers)):  # next integer(loop)
            if integers[greatest_value] < integers[num]:  # calculate greater integer
                greatest_value = num  # update greatest value
        integers[i], integers[greatest_value] = integers[greatest_value], integers[i]  # update list
        print(''.join([str(n) + ' ' for n in integers]))  # output iteration
    return integers


if __name__ == '__main__':
    integers_list = [int(number) for number in input().split()]  # get input, require input to be an integer,
    # split numbers and place into list
    selection_sort_descend_trace(integers_list)  # call function to sort the list
