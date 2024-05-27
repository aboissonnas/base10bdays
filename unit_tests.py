import unittest
from . import utils


class TestGetYear(unittest.TestCase):
    
    def test_correct(self):
        test_year = utils.get_year('01/02/2023')

        self.assertEqual(test_year, 2023)

    def test_unexpected_format(self):
        test_year = utils.get_year('011/2/34582')

        self.assertEqual(test_year, 34582)

    
class TestGetMonth(unittest.TestCase):

    def test_correct(self):
        test_month = utils.get_month('01/02/2023')

        self.assertEqual(test_month, 1)

    def test_unexpected_format(self):
        test_month = utils.get_month('453/777777/12')

        self.assertEqual(test_month, 453)


class TestGetDay(unittest.TestCase):

    def test_correct(self):
        test_day = utils.get_day('01/02/2023')

        self.assertEqual(test_day, 2)

    def test_unexpected_format(self):
        test_day = utils.get_day('0/5699998/41')

        self.assertEqual(test_day, 5699998)


class TestGetDateString(unittest.TestCase):

    def test_one_digit_month_and_day(self):
        test_string = utils.get_date_string(2, 1, 2023)

        self.assertEqual(test_string, '01/02/2023')

    def test_one_digit_month_two_digit_day(self):
        test_string = utils.get_date_string(25, 1, 2023)

        self.assertEqual(test_string, '01/25/2023')

    def test_two_digit_month_one_digit_day(self):
        test_string = utils.get_date_string(2, 12, 2023)
        
        self.assertEqual(test_string, '12/02/2023')

    def test_two_digit_month_and_day(self):
        test_string = utils.get_date_string(22, 10, 2023)
        
        self.assertEqual(test_string, '10/22/2023')

    def test_nonsense_date(self):
        test_string = utils.get_date_string(584, -45, 17776)

        # this nonsense is the expected behavior
        self.assertEqual(test_string, '0-45/584/17776')


class TestIsEvenlyDivisible(unittest.TestCase):

    def test_when_true(self):
        test_bool = utils.is_evenly_divisible(10, 5)

        self.assertTrue(test_bool)

    def test_when_false(self):
        test_bool = utils.is_evenly_divisible(9, 5)

        self.assertFalse(test_bool)


class TestIsLeapYear(unittest.TestCase):

    def test_fourth_year(self):
        test_bool = utils.is_leap_year(2024)

        self.assertTrue(test_bool)

    def test_century(self):
        test_bool = utils.is_leap_year(1900)

        self.assertFalse(test_bool)

    def test_fourth_century(self):
        test_bool = utils.is_leap_year(2000)

        self.assertTrue(test_bool)

    def test_random_year(self):
        test_bool = utils.is_leap_year(2017)

        self.assertFalse(test_bool)


class TestFindNumLeapYears(unittest.TestCase):

    def test_fourth_year(self):
        test_years = utils.find_num_leap_years(2003, 2005)

        self.assertEqual(test_years, 1)

    def test_century(self):
        test_years = utils.find_num_leap_years(1899, 1901)

        # every century is not a leap year
        self.assertEqual(test_years, 0)

    def test_fourth_century(self):
        test_years = utils.find_num_leap_years(1999, 2001)

        # every 4th century is a leap year
        self.assertEqual(test_years, 1)

    def test_start_on_leap_year(self):
        test_years = utils.find_num_leap_years(2004, 2005)

        self.assertEqual(test_years, 1)

    def test_stop_on_leap_year(self):
        test_years = utils.find_num_leap_years(2003, 2004)

        self.assertEqual(test_years, 1)

    def test_stop_is_smaller(self):
        test_years = utils.find_num_leap_years(2009, 2002)

        self.assertEqual(test_years, -2)

    def test_stop_is_negative(self):
        test_years = utils.find_num_leap_years(2002, -5)

        self.assertEqual(test_years, -487)


class TestListOfDaysInEachMonth(unittest.TestCase):

    def test_leap_year(self):
        test_list = utils.list_of_days_in_each_month(2024)

        self.assertEqual(len(test_list), 12)
        self.assertEqual(test_list, [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31])

    def test_normal_year(self):
        test_list = utils.list_of_days_in_each_month(2021)

        self.assertEqual(len(test_list), 12)
        self.assertEqual(test_list, [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31])


class TestCountDaysToYearEnd(unittest.TestCase):

    def test_regular_year(self):
        test_count = utils.count_days_to_year_end(7, 2, 2021)

        self.assertEqual(test_count, 327)

    def test_leap_year(self):
        test_count = utils.count_days_to_year_end(7, 2, 2020)

        self.assertEqual(test_count, 328)

    def test_jan_1(self):
        test_count = utils.count_days_to_year_end(1, 1, 2021)

        self.assertEqual(test_count, 364)

    def test_dec_31(self):
        test_count = utils.count_days_to_year_end(31, 12, 2021)

        self.assertEqual(test_count, 0)

    def test_wrong_day(self):
        test_count = utils.count_days_to_year_end(54, 9, 2021)
        control_count = utils.count_days_to_year_end(30, 9, 2021)

        # if the day is after the end of the month, assume it's meant to be the last day of the month
        self.assertEqual(test_count, control_count)

    def test_negative_day(self):
        test_count = utils.count_days_to_year_end(-4, 9, 2021)
        control_count = utils.count_days_to_year_end(1, 9, 2021)

        # if the day is negative, assume it's meant to be the 1st day of the month
        self.assertEqual(test_count, control_count)

    def test_wrong_month(self):
        test_count = utils.count_days_to_year_end(7, 14, 2021)
        control_count = utils.count_days_to_year_end(7, 12, 2021)

        # if the month is after the end of the year, assume it's meant to be december
        self.assertEqual(test_count, control_count)

    def test_negative_month(self):
        test_count = utils.count_days_to_year_end(7, -4, 2021)
        control_count = utils.count_days_to_year_end(7, 1, 2021)

        # if the month is negative, assume it's meant to be january
        self.assertEqual(test_count, control_count)


class TestFindDateFromYearEnd(unittest.TestCase):

    def test_regular_year(self):
        test_day, test_month = utils.find_date_from_year_end(327, 2021)

        self.assertEqual(test_day, 7)
        self.assertEqual(test_month, 2)

    def test_leap_year(self):
        test_day, test_month = utils.find_date_from_year_end(327, 2020)

        self.assertEqual(test_day, 8)
        self.assertEqual(test_month, 2)

    def test_negative_num_days(self):
        test_day, test_month = utils.find_date_from_year_end(-7, 2020)

        # negative numbers are readjusted to 0
        self.assertEqual(test_day, 31)
        self.assertEqual(test_month, 12)

    def test_negative_year(self):
        test_day, test_month = utils.find_date_from_year_end(327, -5)

        # negative years are treated just like positive years
        self.assertEqual(test_day, 7)
        self.assertEqual(test_month, 2)


class TestFindDateFromYearStart(unittest.TestCase):

    def test_regular_year(self):
        test_day, test_month = utils.find_date_from_year_start(63, 2021)

        self.assertEqual(test_day, 4)
        self.assertEqual(test_month, 3)

    def test_leap_year(self):
        test_day, test_month = utils.find_date_from_year_start(63, 2020)

        self.assertEqual(test_day, 3)
        self.assertEqual(test_month, 3)

    def test_negative_num_days(self):
        test_day, test_month = utils.find_date_from_year_start(-22, 2021)

        # negative numbers are readjusted to 1
        self.assertEqual(test_day, 1)
        self.assertEqual(test_month, 1)

    def test_negative_year(self):
        test_day, test_month = utils.find_date_from_year_start(63, -629)

        # negative years are treated just like positive years
        self.assertEqual(test_day, 4)
        self.assertEqual(test_month, 3)


class TestFindBaseTenBdayCountingAheadSolution(unittest.TestCase):

    def test_correct(self):
        test_date = utils.find_base_ten_bday_counting_ahead_solution('01/01/1990', 1)
        test_leap = utils.find_base_ten_bday_counting_ahead_solution('01/01/1991', 1)

        self.assertEqual(test_date, '09/27/1992')
        self.assertEqual(test_leap, '09/27/1993')

    def test_negative_age(self):
        test_date = utils.find_base_ten_bday_counting_ahead_solution('01/01/1990', -1)

        # just returns the birthdate
        self.assertEqual(test_date, '01/01/1990')


class TestFindBaseTenBdayMathSolution(unittest.TestCase):

    def test_correct(self):
        test_date = utils.find_base_ten_bday_math_solution('01/01/1990', 1)
        test_leap = utils.find_base_ten_bday_math_solution('01/01/1991', 1)

        self.assertEqual(test_date, '09/27/1992')
        self.assertEqual(test_leap, '09/27/1993')

    def test_negative_age(self):
        test_date = utils.find_base_ten_bday_math_solution('01/01/1990', -1)

        # just returns the birthdate
        self.assertEqual(test_date, '01/01/1990')
