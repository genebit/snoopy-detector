
import pygame
import sys

window = pygame.display.set_mode((1366, 768), pygame.FULLSCREEN | pygame.SCALED)
clock = pygame.time.Clock()

fake_window = pygame.image.load('./pygame/img/windows.PNG')

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    window.blit(fake_window, (0, 0))

    pygame.display.update()