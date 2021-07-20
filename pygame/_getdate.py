import datetime

class GetDate:

    _month = None
    _day = None
    _day_of_the_week = None

    def __init__(self):

        self._month = self.determine_month()
        self._day = datetime.datetime.now().day
        self._day_of_the_week = self.determine_day_of_the_week()

    def determine_month(self):
        raw_month = datetime.datetime.now().month

        month = None

        if raw_month == 1:
            month = 'January'
        if raw_month == 2:
            month = 'February'
        if raw_month == 3:
            month = 'March'
        if raw_month == 4:
            month = 'April'
        if raw_month == 5:
            month = 'May'
        if raw_month == 6:
            month = 'June'
        if raw_month == 7:
            month = 'July'
        if raw_month == 8:
            month = 'August'
        if raw_month == 9:
            month = 'September'
        if raw_month == 10:
            month = 'October'
        if raw_month == 11:
            month = 'November'
        if raw_month == 12:
            month = 'December'
        
        return month

    def determine_day_of_the_week(self):
        raw_weekday = datetime.datetime.today().weekday()
        
        day = None

        if raw_weekday == 0:
            day = 'Monday'
        if raw_weekday == 1:
            day = 'Tuesday'
        if raw_weekday == 2:
            day = 'Wednesday'
        if raw_weekday == 3:
            day = 'Thursday'
        if raw_weekday == 4:
            day = 'Friday'
        if raw_weekday == 5:
            day = 'Saturday'
        if raw_weekday == 6:
            day = 'Sunday'

        return day