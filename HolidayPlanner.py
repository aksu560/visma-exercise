import datetime
import sys
import json

# Helper function to iterate between two dates.
def yield_dates(start_date, end_date):
    for x in range(int((end_date - start_date).days)):
        yield start_date + datetime.timedelta(x)

class HolidayPlanner:
    """Base class for all holidays, regardless of jurisdiction"""

    def __init__(self, start, end, holidays):

        start_date = datetime.date.fromisoformat(start)
        end_date = datetime.date.fromisoformat(end)

        if (start_date > end_date):
            raise ValueError("Start date must be before end date")

        holiday_duration = end_date - start_date
        if (holiday_duration.days > 50):
            raise ValueError("The holiday duration cannot be more than 50 days")

        # Initialize the list of national holidays
        self.national_holidays_list = []
        for holiday in holidays:
            self.national_holidays_list.append(datetime.date.fromisoformat(holiday))
        self.start_date = start_date
        self.end_date = end_date
        self.duration = holiday_duration

    def get_national_holiday_count(self):
        holidays = 0
        for holiday in self.national_holidays_list:
            if (self.start_date <= holiday <= self.end_date):
                holidays += 1
        return holidays

    def get_required_days(self):
        return self.duration.days - self.get_national_holiday_count()

    def get_free_day_count(self):
        required_days = self.get_required_days()
        return self.duration.days - required_days

class FinnishHolidayPlanner(HolidayPlanner):
    """Subclass for holidays adhering to Finnish regulations"""

    def __init__(self, start, end, national_holidays_list):
        super().__init__(start, end, national_holidays_list)
        
        # Check if the holiday falls on the end of a holiday period.
        # Holiday periods in Finland start on the first of April.
        if (self.start_date.month < 4 and self.end_date.month >= 4):
            raise ValueError("The holiday overlaps the start of a new holiday period.")

    def get_required_days(self):
        return self.duration.days - self.get_national_holiday_count() - self.get_sunday_count()

    def get_sunday_count(self):
        sundays = 0
        for day in yield_dates(self.start_date, self.end_date):
            if (day.weekday() == 6):
                sundays += 1                
        return sundays

class HumanReadableHolidayReader():
    """Subclass for human readable holiday output"""

    def get_holiday_as_string(holiday):
        """Returns the holiday as a human readable string"""
        total_days = holiday.duration.days
        days_not_counted = holiday.get_free_day_count()
        days_required = holiday.get_required_days()
        start = holiday.start_date.isoformat()
        end = holiday.end_date.isoformat()

        return f"Holiday from {start} to {end}\nTotal days: {total_days}\nDays not counted: {days_not_counted}\nHoliday days required: {days_required}"

class HolidayDictionarySerializer:
    """Class for serializing holiday data to a dictionary"""

    def serialize(holiday: HolidayPlanner):
        return {
            "start": holiday.start_date.isoformat(),
            "end": holiday.end_date.isoformat(),
            "duration": holiday.duration.days,
            "days_not_counted": holiday.get_free_day_count(),
            "holiday_days_required": holiday.get_required_days()
        }

class HolidayJSONSerializer:
    """Class for serializing holiday data to JSON"""

    def serialize(holiday: HolidayPlanner):
        return json.dumps(HolidayDictionarySerializer.serialize(holiday))

if __name__ == "__main__":

    # List of national holidays. Could eventually be more robust with year agnosticism.
    # NOTE: List provided by the exercise instructions is not complete. It's used here,
    # but not all holidays are included.
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

    start = sys.argv[1]
    end = sys.argv[2]

    holiday = FinnishHolidayPlanner(start, end, national_holidays_list)
    print(HumanReadableHolidayReader.get_holiday_as_string(holiday))