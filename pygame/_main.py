
import pygame
import sys

window = pygame.display.set_mode((1366, 768), pygame.FULLSCREEN | pygame.SCALED)
clock = pygame.time.Clock()

fake_window = pygame.image.load('./pygame/img/windows.PNG')

# FIXME: Font not initialized
font = pygame.font.SysFont('Roboto', 32)
clock =  font.render('10', True, (255, 255, 255))
clock_rect = clock.get_rect()
clock_rect.center = (window.get_width()/2, window.get_height()/2 -20)

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    window.blit(fake_window, (0, 0))

    pygame.display.update()