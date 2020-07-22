import pygame
from pygame.locals import *
from config import sun, mercury, venus, earth, moon, mars, jupiter, saturn, uranus, neptune, rect_shaft, simulator

#Color
BLACK = ((0, 0, 0))
ORANGE = ((255,127, 39))
GRAY = ((128, 128, 128))
YELLOW = ((255, 255, 0))
DARK_BLUE = ((0, 0, 160))
WHITE = ((255, 255, 255))
RED = ((255, 0, 0))
LIGHT_GRAY = ((192, 192, 192))
BEIGE = ((255, 128, 128))
LIGHT_BLUE = ((128, 255, 255))
BLUE = ((0, 0, 255))

# Config
WIDTH = 1520
HEIGHT = 720
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Solar System")
WIN_RECT = WIN.get_rect()

# Font
pygame.font.init()
font_standard = pygame.font.SysFont("Arial", 80)

# Images
img_bg = pygame.image.load("bg.jpg")

img_sun = pygame.image.load("sun.png")
sun_rect = img_sun.get_rect()

img_mercury = pygame.image.load("mercury.png")
mercury_rect = img_mercury.get_rect()

img_venus = pygame.image.load("venus.png")
venus_rect = img_venus.get_rect()

img_earth = pygame.image.load("earth.png")
earth_rect = img_earth.get_rect()

img_moon = pygame.image.load("moon.png")
moon_rect = img_moon.get_rect()

img_mars = pygame.image.load("mars.png")
mars_rect = img_mars.get_rect()

img_jupiter = pygame.image.load("jupiter.png")
jupiter_rect = img_jupiter.get_rect()

img_saturn = pygame.image.load("saturn.png")
saturn_rect = img_saturn.get_rect()

img_uranus = pygame.image.load("uranus.png")
uranus_rect = img_uranus.get_rect()

img_neptune = pygame.image.load("neptune.png")
neptune_rect = img_neptune.get_rect()

img_clickhere = pygame.image.load("clickhere.png")

# Rect
rect_sun = pygame.Rect(10, 300, 150, 150)
rect_mercury = pygame.Rect(180, 300, 150, 150)
rect_venus = pygame.Rect(350, 300, 150, 150)
rect_earth = pygame.Rect(520, 300, 150, 150)
rect_moon = pygame.Rect(580, 220, 80, 70)
rect_mars = pygame.Rect(690, 300, 150, 150)
rect_jupiter = pygame.Rect(860, 300, 150, 150)
rect_saturn = pygame.Rect(1030, 300, 150, 150)
rect_uranus = pygame.Rect(1200, 300, 150, 150)
rect_neptune = pygame.Rect(1370, 300, 150, 150)
rect_clickhere = pygame.Rect(0, 650, 80, 80)


game_over = False
while game_over != True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True

        if event.type == pygame.MOUSEBUTTONDOWN:
            if rect_sun.collidepoint(pygame.mouse.get_pos()):
                sun()
            if rect_mercury.collidepoint(pygame.mouse.get_pos()):
                mercury()
            if rect_venus.collidepoint(pygame.mouse.get_pos()):
                venus()
            if rect_earth.collidepoint(pygame.mouse.get_pos()):
                earth()
            if rect_moon.collidepoint(pygame.mouse.get_pos()):
                moon()
            if rect_mars.collidepoint(pygame.mouse.get_pos()):
                mars()
            if rect_jupiter.collidepoint(pygame.mouse.get_pos()):
                jupiter()
            if rect_saturn.collidepoint(pygame.mouse.get_pos()):
                saturn()
            if rect_uranus.collidepoint(pygame.mouse.get_pos()):
                uranus()
            if rect_neptune.collidepoint(pygame.mouse.get_pos()):
                neptune()
            if rect_clickhere.collidepoint(pygame.mouse.get_pos()):
                simulator()

    text = font_standard.render("Solar System", True, WHITE)

    WIN.blit(img_bg, (0, 0))
    WIN.blit(text, (580, 0))
    WIN.blit(img_sun, (10, 300))
    WIN.blit(img_mercury, (180, 300))
    WIN.blit(img_venus, (350, 300))
    WIN.blit(img_earth, (520, 300))
    WIN.blit(img_moon, (580, 220))
    WIN.blit(img_mars, (690, 300))
    WIN.blit(img_jupiter, (860, 300))
    WIN.blit(img_saturn, (1030, 350))
    WIN.blit(img_uranus, (1200, 300))
    WIN.blit(img_neptune, (1370, 300))
    WIN.blit(img_clickhere, (0, 650))

    pygame.draw.rect(WIN, ORANGE, rect_sun, -1)
    pygame.draw.rect(WIN, GRAY, rect_mercury, -1)
    pygame.draw.rect(WIN, YELLOW, rect_venus, -1)
    pygame.draw.rect(WIN, DARK_BLUE, rect_earth, -1)
    pygame.draw.rect(WIN, WHITE, rect_moon, -1)
    pygame.draw.rect(WIN, RED, rect_mars, -1)
    pygame.draw.rect(WIN, LIGHT_GRAY, rect_jupiter, -1)
    pygame.draw.rect(WIN, BEIGE, rect_saturn, -1)
    pygame.draw.rect(WIN, LIGHT_BLUE, rect_uranus, -1)
    pygame.draw.rect(WIN, BLUE, rect_neptune, -1)
    pygame.draw.rect(WIN, RED, rect_clickhere, -1)

    pygame.display.update()

pygame.quit()
