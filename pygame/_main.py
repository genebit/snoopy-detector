
import pygame
import sys

import _gettime
import _getdate

time = _gettime.GetTime()
today = _getdate.GetDate()

WHITE = (225, 225, 225)
pygame.init()

window = pygame.display.set_mode((1366, 768), pygame.FULLSCREEN | pygame.SCALED)

font = pygame.font.SysFont('Times New Roman', 100)
font_date = pygame.font.SysFont('Times New Roman', 50)
font_day = pygame.font.SysFont('Times New Roman', 90)

month =  font_date.render(str(today._month), True, WHITE)
day_of_the_week =  font_date.render(str(today._day_of_the_week), True, WHITE)

day =  font_day.render(str(today._day), True, WHITE)

class ClockObject:

    clock = None
    clock_rect = None

    def __init__(self, window):
        self.clock =  font.render(time.current_time, True, WHITE)
        self.clock_rect = self.clock.get_rect()
        self.clock_rect.center = (window.get_width()/2, window.get_height()/2 -20)
    
    def show_clock(self, window):
        window.blit(self.clock, self.clock_rect)

def show_fake_window():
    fake_window = pygame.image.load('./pygame/img/windows.PNG')

    window.blit(fake_window, (0, 0))

def show_calendar(month, day_of_the_week, day):
    window.blit(month, (window.get_width()/2, window.get_height()/2 +20))
    window.blit(day, (window.get_width()/2  +100, window.get_height()/2 +20))
    window.blit(day_of_the_week, (window.get_width()/2 -85, window.get_height()/2 +60))

fake_clock = ClockObject(window)

while True:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()      

    show_fake_window()
    fake_clock.show_clock(window)

    show_calendar(month, day_of_the_week, day)
    
    pygame.display.update()