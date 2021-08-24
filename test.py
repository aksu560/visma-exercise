import unittest
from unittest.case import TestCase
import HolidayPlanner

class TestHolidayPlanner(unittest.TestCase):

    def test_holiday_length(self):
        res = HolidayPlanner.HolidayPlanner("2021-02-01", "2021-02-15").toDict()
        self.assertEqual(res["duration_days"], 14)

    def test_incorrect_order(self):
        self.assertRaises(ValueError, HolidayPlanner.HolidayPlanner, "2021-02-15", "2021-02-01")

    def test_holiday_too_long(self):
        self.assertRaises(ValueError, HolidayPlanner.HolidayPlanner, "2021-01-01", "2021-02-21")

class TestFinnishHolidayPlanner(unittest.TestCase):

    def test_national_holiday(self):
        res = HolidayPlanner.FinnishHolidayPlanner("2021-01-01", "2021-01-02").toDict()
        self.assertEqual(res["national_holidays"], 1)

    def test_sunday(self):
        res = HolidayPlanner.FinnishHolidayPlanner("2021-01-03", "2021-01-04").toDict()
        self.assertEqual(res["sundays"], 1)

    def test_saturday(self):
        res = HolidayPlanner.FinnishHolidayPlanner("2021-01-02", "2021-01-03").toDict()
        self.assertEqual(res["used_days"], 1)

    def test_over_holiday_period(self):
        self.assertRaises(ValueError, HolidayPlanner.FinnishHolidayPlanner, "2021-03-31", "2021-04-01")

if __name__ == "__main__":
    unittest.main()