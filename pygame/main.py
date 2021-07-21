import pygame
import os
import time

import gadgets
import getdate

WINDOW_WIDTH = 1366
WINDOW_HEIGHT = 768
CLOCK_FPS = pygame.time.Clock()

window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT), pygame.FULLSCREEN | pygame.SCALED)

# ------------------
# Initialize modules
_date = getdate.Date()
_time = getdate.Time()

gadget = gadgets.Gadget(window, _date, _time)
# ------------------
enable_gadget = True
enable_fake_windows = True

# ------------------
# Trigger
click_count = 0

# ------------------
# Mouse Position and Input File logs
rec_mouse_pos = open('./record/m_position.rec', 'w')
rec_input = open('./record/input.rec', 'w')

def show_fake_window(enable):
    if enable:
        fake_window = pygame.image.load('./pygame/img/windows.PNG')
        window.blit(fake_window, (0, 0))
    else:
        death_img = pygame.image.load('./pygame/img/death.jpg')
        window.blit(death_img, (0, 0))

def sleep():
    time.sleep(0.5)
    os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")
    
    pygame.quit()
    quit()

def input_trigger():
    global click_count, enable_gadget, enable_fake_windows

    click_count += 1
    if click_count == 3:
        # Disable gadget and window
        enable_gadget = False
        enable_fake_windows = False
    
    if click_count > 3:
        sleep()

while True:
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:

            rec_input.write('Click Count: {0}\n'.format(str(click_count)))
            
            input_trigger()

        if event.type == pygame.KEYDOWN:
            input_trigger()

            key_pressed = event.key
            rec_input.write('Key Stroke: {0}\n'.format(str(key_pressed)))
                
    show_fake_window(enable_fake_windows)
    gadget.show_gadget(window, enable_gadget)

    mouse_x, mouse_y = pygame.mouse.get_pos()
    rec_mouse_pos.write('Mouse Position [X:{0}, Y:{1}]\n'.format(str(mouse_x), str(mouse_y)))

    CLOCK_FPS.tick(5)
    pygame.display.update()