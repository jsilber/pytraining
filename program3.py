# This program computes the number of days between today and
# the next Penn State Football day provided by the user

import datetime

def print_header():
    print('-------------------')
    print('   GAME DAY APP'    )
    print('-------------------')
    print()

def get_gameday_from_user():
    print("When is the next Penn State football game?")
    #Everything that is pass into input is a string by default. Must convert it to an integer
    year = int(input("Year [YYYY]: "))
    month = int(input("Month [MM]: "))
    day = int(input("Day [DD]: "))

    gameday = datetime.date(year, month, day)
    return gameday


def compute_days_between_dates(original_date,target_date):
    this_year = datetime.date(original_date.year, original_date.month, original_date.day)
    dt = this_year - target_date
    return dt.days


def print_gameday_information(days):
    #If the game was in the past
    if days < 0:
        print("The last game was {:,} days ago".format(days))
    elif days > 0:
        print("The game is in {:,} days".format(days))
    else:
        print ("Today is game day!")

def main():
    print_header()
    gday = get_gameday_from_user()
    print(gday)
    today = datetime.date.today()
    number_of_days = compute_days_between_dates(gday, today)
    print_gameday_information(number_of_days)

#Call main function
main()
