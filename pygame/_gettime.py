import datetime

class GetTime:

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

if __name__ == '__main__':
    # NOTE: For Debug
    # _time = GetTime()
    # print('The time for today is currently:', _time.current_time)
    pass