import datetime

class Date:

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
            day = 'Mon'
        if raw_weekday == 1:
            day = 'Tue'
        if raw_weekday == 2:
            day = 'Wed'
        if raw_weekday == 3:
            day = 'Thu'
        if raw_weekday == 4:
            day = 'Fri'
        if raw_weekday == 5:
            day = 'Sat'
        if raw_weekday == 6:
            day = 'Sun'

        return day

class Time:

    _hour = None
    _minute = None

    current_hour = None
    current_daytime = None
    current_time = None

    def __init__(self):
        self._hour = datetime.datetime.now().hour
        self._minute = datetime.datetime.now().minute

        self.current_hour = self.convert_hour(self._hour)
        self.current_daytime = self.determine_daytime(self._hour)
        
        self.current_time = '{0}:{1} {2}'.format(self.current_hour, self._minute, self.current_daytime)
    
    def convert_hour(self, hour):
        format = hour % 12
        format = 12 if format == 0 else format
        
        return format

    def determine_daytime(self, hour):
        daytime = None
        daytime = 'AM' if hour < 12 else 'PM'

        return daytime