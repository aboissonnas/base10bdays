import re
from . import utils


# run the whole script
def run_base10_bdays():
    
    print('Hello! Welcome to the Base 10 Birthdays calculator!')
    print('A normal year is 365 days, but a Base 10 year is 1000 days. This calculator finds what date you turned a given age in Base 10!')

    keep_playing = True
    while keep_playing:

        date_pattern = '[0-9]{2}/[0-9]{2}/[0-9]{4}' # checks for 2 numeric characters, a /, 2 numeric characters, a /, and then 4 numeric characters
        date_regex = re.compile(date_pattern)
        bday_in = ''
        good_input = False
        while not good_input:
            user_in = input('Please enter a birthdate in the format mm/dd/yyyy: ')

            # time to sanitize our inputs! make sure we're getting a date in the right format
            if not date_regex.fullmatch(user_in.strip()):
                print('That\'s not a mm/dd/yyyy date! Try again.')
                continue

            # any 4-digit year is going to be valid
            in_year = utils.get_year(user_in)

            in_month = utils.get_month(user_in)
            # make sure the month is valid (1-12)
            if not (in_month > 0 and in_month <= 12):
                print('The month {} is invalid. Please try again.'.format(in_month))
                continue

            in_day = utils.get_day(user_in)
            days_in_in_month = utils.list_of_days_in_each_month(in_year)[in_month-1]
            # make sure the day is valid for the month
            if not (in_day > 0 and in_day <= days_in_in_month):
                print('The day {} is invalid for the month {}. Please try again.'.format(in_day, in_month))
                continue

            # if the input passed all the checks, then the user gave us a valid mm/dd/yyyy date
            bday_in = user_in
            good_input = True

        age_pattern = '[0-9]+' # checks for any number of numeric characters
        age_regex = re.compile(age_pattern)
        age_in = 0
        good_input = False
        while not good_input:
            user_in = input('Please enter a Base 10 age to calculate: ')

            # another input to sanitize...
            if not age_regex.fullmatch(user_in.strip()):
                print('That\'s not a valid age! Try again.')
                continue

            # this one's not complicated - we just need a number. if we have that, we're good.
            age_in = int(user_in)
            good_input = True

        print('Great! I\'ll calculate the date at which someone born on {} turns {} in Base 10 years!'.format(bday_in, age_in))
        print('Calculating...')

        base_ten_bday = utils.find_base_ten_bday_math_solution(bday_in, age_in)

        print('A person born on {} turns Base 10 {} on {}!'.format(bday_in, age_in, base_ten_bday))

        user_in = input('Would you like to calculate another Base 10 birthday? y/n: ')

        # kick the user out unless they give a comprehensible yes
        if user_in.strip() not in ('y', 'Y', 'yes', 'YES', 'Yes'):
            keep_playing = False


# this is where i'm actually running the script
run_base10_bdays()
