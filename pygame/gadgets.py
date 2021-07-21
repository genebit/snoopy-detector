import pygame

pygame.init()

class Gadget:

    DATE = None
    TIME = None
    WHITE = (225, 225, 225)
    FONT = 'Times New Roman'

    clock = None
    clock_rect = None

    month = None
    day_of_the_week = None
    day = None

    def __init__(self, window, date, time):
        self.DATE = date
        self.TIME = time
    
    # Fonts
        CLOCK_FONT = pygame.font.SysFont(self.FONT, 100)
        DATE_FONT = pygame.font.SysFont(self.FONT, 50)
        DAY_FONT = pygame.font.SysFont(self.FONT, 90)

    # Time
        self.clock =  CLOCK_FONT.render(self.TIME.current_time, True, self.WHITE)
        self.clock_rect = self.clock.get_rect()
        self.clock_rect.center = (window.get_width()/2, window.get_height()/2-20)
    
    # Calendar
        self.month = DATE_FONT.render(str(date._month), True, self.WHITE)
        self.day = DAY_FONT.render(str(date._day), True, self.WHITE)
        self.day_of_the_week = DATE_FONT.render(str(date._day_of_the_week), True, self.WHITE)

    def show_gadget(self, window, enable):
        if enable:
            window.blit(self.clock, self.clock_rect)

            window.blit(self.month, (window.get_width()/2, window.get_height()/2 +20))
            window.blit(self.day, (window.get_width()/2  +100, window.get_height()/2 +20))
            window.blit(self.day_of_the_week, (window.get_width()/2 -10, window.get_height()/2 +60))