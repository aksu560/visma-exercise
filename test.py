from logging import setLogRecordFactory
import unittest
from unittest.case import TestCase
import HolidayPlanner

national_holidays_list = [
        "2020-01-01", # New year's day
        "2020-01-06", # Epiphany
        "2020-04-10", # Good Friday
        "2020-04-13", # Second day of Easter
        "2020-05-01", # Labour Day
        "2020-05-21", # Ascension Day
        "2020-06-19", # Mid-Summer Eve
        "2020-12-24", # Christmas Eve
        "2020-12-25", # Christmas Day
        "2021-01-01", # New year's day
        "2021-01-06", # Epiphany
        "2021-04-02", # Good Friday
        "2021-04-05", # Second day of Easter
        "2021-05-13", # Ascension Day
        "2021-06-20", # Mid-Summer Eve
        "2021-12-24" # Christmas Eve
    ]

class TestHolidayPlanner(unittest.TestCase):


    def test_holiday_length(self):
        holiday = HolidayPlanner.HolidayPlanner("2021-02-01", "2021-02-15", national_holidays_list)
        res = HolidayPlanner.HolidayDictionarySerializer.serialize(holiday)
        self.assertEqual(res["duration"], 14)

    def test_incorrect_order(self):
        self.assertRaises(ValueError, HolidayPlanner.HolidayPlanner, "2021-02-15", "2021-02-01", national_holidays_list)

    def test_holiday_too_long(self):
        self.assertRaises(ValueError, HolidayPlanner.HolidayPlanner, "2021-01-01", "2021-02-21", national_holidays_list)
    
    def test_holiday_dict_must_serialize(self):
        holiday = HolidayPlanner.HolidayPlanner("2021-02-01", "2021-02-15", national_holidays_list)
        res = HolidayPlanner.HolidayJSONSerializer.serialize(holiday)
        expected = '{"start": "2021-02-01", "end": "2021-02-15", "duration": 14, "days_not_counted": 0, "holiday_days_required": 14}'
        self.assertEqual(res, expected)

class TestFinnishHolidayPlanner(unittest.TestCase):

    def test_national_holiday(self):
        holiday = HolidayPlanner.FinnishHolidayPlanner("2021-01-01", "2021-01-02", national_holidays_list)
        res = HolidayPlanner.HolidayDictionarySerializer.serialize(holiday)
        self.assertEqual(res["days_not_counted"], 1)

    def test_sunday(self):
        holiday = HolidayPlanner.FinnishHolidayPlanner("2021-01-03", "2021-01-04", national_holidays_list)
        res = HolidayPlanner.HolidayDictionarySerializer.serialize(holiday)
        self.assertEqual(res["days_not_counted"], 1)

    def test_saturday(self):
        holiday = HolidayPlanner.FinnishHolidayPlanner("2021-01-02", "2021-01-03", national_holidays_list)
        res = HolidayPlanner.HolidayDictionarySerializer.serialize(holiday)
        self.assertEqual(res["holiday_days_required"], 1)

    def test_over_holiday_period(self):
        self.assertRaises(ValueError, HolidayPlanner.FinnishHolidayPlanner, "2021-03-31", "2021-04-01", national_holidays_list)

if __name__ == "__main__":
    unittest.main()