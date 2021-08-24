import datetime
import sys

class HolidayPlanner:
    """A class for determining required number of holiday days to hold a holiday
    during a certain time period"""

    def __init__(self, start, end):
        # Initialize the start and end dates
        start_date = datetime.date.fromisoformat(start)
        end_date = datetime.date.fromisoformat(end)


        if start_date > end_date:
            raise ValueError("Start date must be before end date")

        # Check if the duration of the holiday is over 50 days.
        holiday_duration = end_date - start_date
        if (holiday_duration.days > 50):
            raise ValueError("The holiday duration cannot be more than 50 days")
        
        self.start_date = start_date
        self.end_date = end_date
        self.duration = holiday_duration
    
    # A function to export holiday data to a dictionary. Makes testing easier.
    def toDict(self):
        return {
            "start_date": self.start_date,
            "end_date": self.end_date,
            "duration_days": self.duration.days,
        }

    def __str__(self) -> str:
        return f"The holiday begins on {self.start_date}, ends on {self.end_date} " \
        f"and requires {self.duration.days} holiday days."

class FinnishHolidayPlanner(HolidayPlanner):
    """Subclass for holidays adhering to Finnish regulations"""

    # List of national holidays. Could eventually be more robust with year agnosticism.
    # NOTE: List provided by the exercise instructions is not complete. It's used here,
    # but not all holidays are included.
    national_holidays_list = [
        datetime.date(2020, 1, 1), # New year's day
        datetime.date(2020, 1, 6), # Epiphany
        datetime.date(2020, 4, 10), # Good Friday
        datetime.date(2020, 4, 13), # Second day of Easter
        datetime.date(2020, 5, 1), # Labour Day
        datetime.date(2020, 5, 21), # Ascension Day
        datetime.date(2020, 6, 19), # Mid-Summer Eve
        datetime.date(2020, 12, 24), # Christmas Eve
        datetime.date(2020, 12, 25), # Christmas Day
        datetime.date(2021, 1, 1), # New year's day
        datetime.date(2021, 1, 6), # Epiphany
        datetime.date(2021, 4, 2), # Good Friday
        datetime.date(2021, 4, 5), # Second day of Easter
        datetime.date(2021, 5, 13), # Ascension Day
        datetime.date(2021, 6, 20), # Mid-Summer Eve
        datetime.date(2021, 12, 24), # Christmas Eve
    ]

    def __init__(self, start, end):
        super().__init__(start, end)

        self.sundays = 0
        self.national_holidays = 0
        
        # Check if the holiday falls on the end of a holiday period.
        # Holiday periods in Finland start on the first of April.
        if (self.start_date.month < 4 and self.end_date.month >= 4):
            raise ValueError("The holiday overlaps the start of a new holiday period.")

        # Check if national holidays fall within the holiday. We exclude sundays, as we count those separately.
        for holiday in self.national_holidays_list:
            if (self.start_date <= holiday <= self.end_date and holiday.weekday() != 6):
                self.national_holidays += 1

        # Remove sundays from the required days.
        sunday_fraction = divmod(self.duration.days, 7)
        self.sundays = sunday_fraction[0]

        # Check if the holiday starts on a sunday.
        if (self.start_date.weekday() == 6):
            self.sundays += 1

        # Adding the remainder to the holiday start date, and checking if it goes over sunday, will handle
        # the off by one error at the end of the holiday.
        if self.duration.days > 6 and sunday_fraction[1] + self.end_date.weekday() > 6:
            self.sundays += 1

        self.holiday_days_required = self.duration.days - self.sundays - self.national_holidays

    def toDict(self):
        return {
            "start_date": self.start_date,
            "end_date": self.end_date,
            "duration_days": self.duration.days,
            "used_days": self.holiday_days_required,
            "sundays": self.sundays,
            "national_holidays": self.national_holidays
        }
        
    def __str__(self) -> str:
        return f"The holiday begins on {self.start_date}, ends on {self.end_date} " \
        f"and requires {self.holiday_days_required} holiday days. \n" \
        f"The holiday includes {self.sundays} sundays and {self.national_holidays} national holidays."

if __name__ == "__main__":
    print(FinnishHolidayPlanner(sys.argv[1], sys.argv[2]))