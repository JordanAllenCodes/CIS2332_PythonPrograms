# Jordan Allen
# zyLabs 12.7: Fat-burning heart rate

def get_age():
    user_age = int(input())  # get age from input
    if 18 <= user_age <= 75:  # check if input is in valid range
        return user_age  # accepted
    raise ValueError('Invalid age.')  # rejected, raise ValueError


def fat_burning_heart_rate(user_age):
    calculation = (220 - user_age) * 0.7  # calculate heart rate for accepted ages
    return calculation


if __name__ == "__main__":
    try:  # test code and find errors
        age = get_age()
        print('Fat burning heart rate for a', age, 'year-old:', fat_burning_heart_rate(age), 'bpm')  # successful
    except ValueError as error:  # manage error
        print(error)
        print('Could not calculate heart rate info.\n')
