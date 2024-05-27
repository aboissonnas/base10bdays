# get the year given a string date in the format 'mm/dd/yyyy'
def get_year(date_string):

    return int(date_string.split('/')[2])


# get the month given a string date in the format 'mm/dd/yyyy'
def get_month(date_string):

    return int(date_string.split('/')[0])


# get the day given a string date in the format 'mm/dd/yyyy'
def get_day(date_string):

    return int(date_string.split('/')[1])


# translate a date to a string in the format 'mm/dd/yyyy'
def get_date_string(day, month, year):
    
    date_string = ''
    # add filler digit if month is one digit
    if month < 10:
        date_string += '0'

    date_string += '{}/'.format(month)
    # add filler digit if day is one digit
    if day < 10:
        date_string += '0'
    
    # year is always 4 digits
    date_string += '{}/{}'.format(day, year)

    return date_string


# determine whether a given integer divides evenly by another given integer
def is_evenly_divisible(num, divisor):

    return num % divisor == 0


# determine whether a given integer is a leap year
def is_leap_year(year):

    is_fourth_year = is_evenly_divisible(year, 4)
    is_century = is_evenly_divisible(year, 100)
    is_fourth_century = is_evenly_divisible(year, 400)

    # every 4th year is a leap year, except for the year that is a century. the 4th century, however, is also a leap year.
    return (is_fourth_year and not is_century) or is_fourth_century


# finds the number of leap years between two years
def find_num_leap_years(start_year, stop_year):

    # uses integer division to find the number of times a 4th/100th/400th year was passed between two years
    num_4th_years = (stop_year // 4) - (start_year // 4)
    num_100th_years = (stop_year // 100) - (start_year // 100)
    num_400th_years = (stop_year // 400) - (start_year // 400)

    # the above operations are inclusive of the stop year, but not the start year
    if is_leap_year(start_year):
        num_4th_years += 1

    # every 4th year is a leap year, except for the year that is also a century, except except for the year that is ALSO a 4th century
    return num_4th_years - num_100th_years + num_400th_years


# the days in each month are magic numbers that we need more than once so let's generate them in one spot
def list_of_days_in_each_month(year):

    days_in_months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    # february has 29 days in leap years
    if is_leap_year(year):
        days_in_months[1] = 29

    return days_in_months


# determines the amount of days left in a given year based on the current date
def count_days_to_year_end(day, month, year):

    days_in_months = list_of_days_in_each_month(year)
    days_counter = 0

    # if the month is larger than 12, assume december is what's meant
    if month > 12:
        month = 12
    # if the month is negative, assume january is what's meant
    elif month < 1:
        month = 1

    # if the day is negative, assume the 1st day of the month is what's meant
    if day <= 0:
        day = 1
    # if the day is larger than the # in the month, assume the last day of the month is what's meant
    elif day > days_in_months[month - 1]:
        day = days_in_months[month - 1]

    # add days remaining in month
    days_counter += days_in_months[month - 1] - day

    # add days in months until end of year
    for i in range(month, 12): # range() is inclusive of the start number and exclusive of the stop number, but lists are 0-indexed
        days_counter += days_in_months[i]

    return days_counter


# determines the date that is the given number of days before the end of the year
def find_date_from_year_end(num_days, year):

    days_in_months = list_of_days_in_each_month(year)
    days_counter = 0
    months_counter = 12

    # if the number of days is negative, assume dec 31 was meant
    if num_days < 1:
        num_days = 0

    # move backwards one month at a time
    while days_counter <= num_days:
        months_counter -= 1
        days_counter += days_in_months[months_counter]

    # lists are 0-indexed so this month is off by 1
    current_month = months_counter + 1

    # we've overshot again, but only to the end of the month
    current_day = days_counter - num_days

    return current_day, current_month


def find_date_from_year_start(num_days, year):

    days_in_months = list_of_days_in_each_month(year)
    days_counter = 0
    months_counter = 0

    # if the number of days is negative, assume jan 1 was meant
    if num_days < 1:
        num_days = 1

    # move forwards one month at a time
    while days_counter < num_days:
        days_counter += days_in_months[months_counter]
        months_counter += 1

    # lists are 0-indexed so this month, which has already incremented, is off by 1
    current_day = num_days - (days_counter - days_in_months[months_counter - 1])

    return current_day, months_counter


# find the day someone turns a certain age in base 10 - counts days in a loop
def find_base_ten_bday_counting_ahead_solution(bday, age_to_find):

    if age_to_find < 0:
        return bday

    # get some numbers to work with
    base_ten_year = 1000
    bday_year = get_year(bday)
    bday_month = get_month(bday)
    bday_day = get_day(bday)
    days_needed_for_age = age_to_find * base_ten_year

    # start counting days
    days_counter = 0
    days_counter += count_days_to_year_end(bday_day, bday_month, bday_year)

    # add days one year at a time
    current_year = bday_year
    while days_counter < days_needed_for_age:
        current_year += 1

        if is_leap_year(current_year):
            days_counter += 366
        else:
            days_counter += 365

    # we've found the year this person turns this base 10 age, but we've overshot to the end of the year
    overshot_days = days_counter % base_ten_year
    current_day, current_month = find_date_from_year_end(overshot_days, current_year)

    # format the date into a string
    base_ten_bday = get_date_string(current_day, current_month, current_year)

    return base_ten_bday


# find the day someone turns a certain age in base 10 - does math
def find_base_ten_bday_math_solution(bday, age_to_find):

    if age_to_find < 0:
        return bday

    # get some numbers to work with
    base_ten_year = 1000
    bday_year = get_year(bday)
    bday_month = get_month(bday)
    bday_day = get_day(bday)
    days_needed_for_age = age_to_find * base_ten_year

    # figure out how many leap years happen between the bday and the base 10 age
    years_needed_estimate = days_needed_for_age // 365
    final_year_estimate = bday_year + years_needed_estimate
    num_leap_years = find_num_leap_years(bday_year, final_year_estimate)

    # recalculate the number of years that will pass taking leap years into account
    actual_years_needed = ((days_needed_for_age - (num_leap_years * 366)) // 365) + num_leap_years
    actual_final_year = bday_year + actual_years_needed
    miscalculated_years = actual_final_year - final_year_estimate

    # correct for missed leap years
    while miscalculated_years > 0:
        num_leap_years += find_num_leap_years(final_year_estimate, actual_final_year)
        final_year_estimate = actual_final_year
        actual_years_needed = ((days_needed_for_age - (num_leap_years * 366)) // 365) + num_leap_years
        actual_final_year = bday_year + actual_years_needed
        
        miscalculated_years = actual_final_year - final_year_estimate

    # find number of days in whole years between the bday and the base 10 age
    if is_leap_year(actual_final_year):
        days_passed_in_intervening_years = ((actual_years_needed - num_leap_years) * 365) + ((num_leap_years - 1) * 366)
    else:
        days_passed_in_intervening_years = ((actual_years_needed - num_leap_years - 1) * 365) + (num_leap_years * 366)

    # figure out how many days into the final year the base 10 bday will happen
    days_into_year = days_needed_for_age - count_days_to_year_end(bday_day, bday_month, bday_year) - days_passed_in_intervening_years

    # get the date
    final_day, final_month = find_date_from_year_start(days_into_year, actual_final_year)

    # format the date into a string
    base_ten_bday = get_date_string(final_day, final_month, actual_final_year)

    return base_ten_bday
