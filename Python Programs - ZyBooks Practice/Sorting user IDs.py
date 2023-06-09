# Jordan Allen
# zyLabs 14.13: Sorting user IDs

num_calls = 0


def partition(userid, y, x):
    calculation = userid[(y + x) // 2]
    low = y - 1
    high = x + 1
    while True:
        low += 1
        while userid[low] < calculation:
            low += 1
        high -= 1
        while userid[high] > calculation:
            high -= 1
        if low >= high:
            return high
        userid[low], userid[high] = userid[high], userid[low]


def quicksort(userid, y, x):
    global num_calls
    num_calls += 1
    if y < x:
        split_index = partition(userid, y, x)
        quicksort(userid, y, split_index)
        quicksort(userid, split_index + 1, x)


if __name__ == "__main__":
    userid_list = []
    userID = input()
    while userID != '-1':
        userid_list.append(userID)
        userID = input()
    quicksort(userid_list, 0, len(userid_list) - 1)
    print(num_calls)
    for userID in userid_list:
        print(userID)
