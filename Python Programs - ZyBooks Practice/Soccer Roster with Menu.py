# Jordan Allen
# ZyLabs 11.27

def print_roster():
    dict_keys = list(soccer_team.keys())  # get jersey numbers
    dict_keys.sort()  # sort in ascending order
    print('ROSTER')
    for dkey in dict_keys:
        print('Jersey number: %d, Rating: %d' % (dkey, soccer_team[dkey]))


soccer_team = {}  # create dictionary to store players info

for i in range(5):  # limit the amount of iterations to 5
    jersey_number = int(input("Enter player %d's jersey number:\n" % (i + 1)))  # get jersey number
    soccer_team[jersey_number] = int(input("Enter player %d's rating:\n" % (i + 1)))  # assign rating to jersey number
    print("")

print_roster()  # call function

while True:  # set up while loop. the program will run continuously starting at the menu after each loop finishes.
    print(
        "\nMENU\na - Add player\nd - Remove player\nu - Update player rating\nr - Output players above a rat"
        "ing\no - Output roster\nq - Quit\n")  # create menu

    user_choice = input("Choose an option:\n")  # user navigation

    if user_choice == 'o':  # o - output roster
        print_roster()

    elif user_choice == 'a':  # - add player, get jersey number and player rating. add to dictionary
        jersey_number = int(input("Enter a new player's jersey number:\n"))
        player_rating = int(input("Enter the player's rating:\n"))
        soccer_team[jersey_number] = player_rating

    elif user_choice == 'd':  # d - remove player, get jersey number and search the dictionary, removed if found
        jersey_number = int(input("Enter a player's jersey number:\n"))
        if jersey_number in list(soccer_team.keys()):
            del soccer_team[jersey_number]

    elif user_choice == 'u':  # u - update player rating, get jersey number and new rating.
        jersey_number = int(input("Enter a jersey number:\n"))
        player_rating = int(input("Enter a new rating for player:\n"))
        soccer_team[jersey_number] = player_rating  # update dictionary with new variable value

    elif user_choice == 'r':  # r - Output players above a given rating
        player_rating = int(input("Enter a rating:\n"))
        new_keys = list(soccer_team.keys())
        new_keys.sort()
        print("\nABOVE %d" % player_rating)  # get rating, list and sort all values in ascending order
        results = 0
        for key in new_keys:
            if soccer_team[key] > player_rating:
                print("Jersey number: %d, Rating: %d" % (key, soccer_team[key]))
                # if the existing rating is greater than input print, then move to next value
                results += 1
        if results == 0:
            print('No players found')  # if no existing rating is greater than input. print no players found

    if user_choice == 'q':
        break  # force loop to stop [end program]
