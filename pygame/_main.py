
import pygame
import sys

import _gettime

time = _gettime.GetTime()

pygame.init()

window = pygame.display.set_mode((1366, 768), pygame.FULLSCREEN | pygame.SCALED)
clock = pygame.time.Clock()

fake_window = pygame.image.load('./pygame/img/windows.PNG')

# FIXME: Font not initialized
font = pygame.font.SysFont('Roboto', 130)
clock =  font.render(time.current_time, True, (255, 255, 255))
clock_rect = clock.get_rect()
clock_rect.center = (window.get_width()/2, window.get_height()/2 -20)

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    window.blit(fake_window, (0, 0))
    window.blit(clock, clock_rect)

    pygame.display.update()