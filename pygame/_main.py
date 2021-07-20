import pygame
import sys

import _gettime
import _getdate

time = _gettime.GetTime()
today = _getdate.GetDate()

WHITE = (225, 225, 225)

pygame.init()

window = pygame.display.set_mode((1366, 768), pygame.FULLSCREEN | pygame.SCALED)

DATE_FONT = pygame.font.SysFont('Times New Roman', 50)
DAY_FONT = pygame.font.SysFont('Times New Roman', 90)

month =  DATE_FONT.render(str(today._month), True, WHITE)
day_of_the_week =  DATE_FONT.render(str(today._day_of_the_week), True, WHITE)
day =  DAY_FONT.render(str(today._day), True, WHITE)

class ClockObject:

    clock = None
    clock_rect = None

    def __init__(self, window):
        CLOCK_FONT = pygame.font.SysFont('Times New Roman', 100)

        self.clock =  CLOCK_FONT.render(time.current_time, True, WHITE)
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
fps_clock = pygame.time.Clock()

click_count = 0
key_pressed = 0

rec_mouse_pos = open('./record/m_position.rec', 'w')
rec_input = open('./record/input.rec', 'w')

while True:
    
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            click_count += 1

            rec_input.write('Click Count: {0}\n'.format(str(click_count)))
            
            if click_count >= 3:
                pygame.quit()
                sys.exit()   

        if event.type == pygame.KEYDOWN:
            key_pressed = event.key
            rec_input.write('Key Stroke: {0}\n'.format(str(key_pressed)))
    
    show_fake_window()
    fake_clock.show_clock(window)

    show_calendar(month, day_of_the_week, day)
    
    mouse_x, mouse_y = pygame.mouse.get_pos()
    rec_mouse_pos.write('Mouse Position [X:{0}, Y:{1}]\n'.format(str(mouse_x), str(mouse_y)))

    fps_clock.tick(5)
    pygame.display.update()