import pygame

window = pygame.display.set_mode((500, 400))
BLACK = (20, 20, 20)
WHITE = (255, 255, 255)

class Object:

    object = pygame.Rect(0, 0, 50, 50)

    def __init__(self, window):
        self.object.center = (window.get_width()/2, window.get_height()/2)

    def show(self, window, enable):
        if enable:
            pygame.draw.rect(window, WHITE, self.object, 2)

box = Object(window)
is_enabled = True

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                # Disable Obj
                if is_enabled:
                    is_enabled = False
                    print('Disabled')
                else:
                    is_enabled = True
                    print('Enabled')


    window.fill(BLACK)

    # Draw Object Here
    box.show(window, is_enabled)

    pygame.display.update()