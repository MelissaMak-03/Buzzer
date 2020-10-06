import pygame
pygame.init()


x= 500
y= 500
win = pygame.display.set_mode((x, y))
# set the pygame window name

pygame.display.set_caption("Buzzer Game")

width = 40
height = 60
vel = 5

# define the RGB value for white,
#  green, blue color .
white = (255, 255, 255)
green = (0, 255, 0)
blue = (0, 0, 128)
purple = (100, 0, 250)
# create a font object.
# 1st parameter is the font file
# which is present in pygame.
# 2nd parameter is size of the font
font = pygame.font.Font('freesansbold.ttf', 32)

# create a text suface object,
# on which text is drawn on it.
text = font.render('Welcome to the Buzzer Game', True, white, purple)

# create a rectangular object for the
# text surface object
textRect = text.get_rect()

# set the center of the rectangular object.
textRect.center = (x // 2, y // 2)

run = True
while run:
    pygame.time.delay(100)

    # copying the text surface object
    # to the display surface object
    # at the center coordinate.
    win.blit(text, textRect)
    pygame.display.update()


for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

pygame.quit()

