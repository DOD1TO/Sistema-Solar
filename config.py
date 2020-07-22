import pygame
from pygame.locals import *
import math
import random

# Color
WHITE = ((255, 255, 255))
BLACK = ((0, 0, 0))

# Font
pygame.font.init()
font_standard = pygame.font.SysFont("Arial", 25)

# Image shaft
img_shaft = pygame.image.load("shaft.png")

# Rect
rect_shaft = pygame.Rect(1450, 650, 50, 80)


def sun():
    # Config
    WIDTH = 1520
    HEIGHT = 720
    WIN = pygame.display.set_mode((WIDTH, HEIGHT))

    # Images
    img_bg = pygame.image.load("bg.jpg")

    img_bigsun = pygame.image.load("bigsun.png")

    game_over = False
    while game_over != True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True

            if event.type == pygame.MOUSEBUTTONDOWN:
                if rect_shaft.collidepoint(pygame.mouse.get_pos()):
                    return

        text_information = font_standard.render("- Center of the solar system.", True, WHITE)
        text_diameter = font_standard.render("- Diameter: 1,392 million kilometers.", True, WHITE)
        text_temperature = font_standard.render("- Temperature: 5.778 K (5.504 ºC) (9.940 ºF).", True, WHITE)
        text_age = font_standard.render("- Age: 4,603 * 10^9 years.", True, WHITE)
        text_mass = font_standard.render("- Mass: 1,989 * 10^30 Kg.", True, WHITE)
        text_radius = font_standard.render("- Radius: 696.340 Km.", True, WHITE)
        text_luminosity = font_standard.render("- Luminosity: 3,9 *10^33 ergs/s.", True, WHITE)

        WIN.blit(img_bg, (0, 0))
        WIN.blit(img_bigsun, (0, 80))
        WIN.blit(img_shaft, (1450, 650))
        WIN.blit(text_information, (650, 50))
        WIN.blit(text_diameter, (650, 150))
        WIN.blit(text_temperature, (650, 250))
        WIN.blit(text_age, (650, 350))
        WIN.blit(text_mass, (650, 450))
        WIN.blit(text_radius, (650, 550))
        WIN.blit(text_luminosity, (650, 650))

        pygame.draw.rect(WIN, WHITE, rect_shaft, -1)

        pygame.display.update()

    pygame.quit()


def mercury():
    # Config
    WIDTH = 1520
    HEIGHT = 720
    WIN = pygame.display.set_mode((WIDTH, HEIGHT))

    # Images
    img_bg = pygame.image.load("bg.jpg")

    img_bigmercury = pygame.image.load("bigmercury.png")

    game_over = False
    while game_over != True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True

            if event.type == pygame.MOUSEBUTTONDOWN:
                if rect_shaft.collidepoint(pygame.mouse.get_pos()):
                    return

        text_information = font_standard.render("- First planet of the solar system.", True, WHITE)
        text_lengt_day = font_standard.render("- Length of day: 58d 15h 30m.", True, WHITE)
        text_orbital = font_standard.render("- Orbital period: 88 days.", True, WHITE)
        text_radius = font_standard.render("- Radius: 2.439,7 Km.", True, WHITE)
        text_mass = font_standard.render("- Mass: 3,285 * 10^23 Kg.", True, WHITE)
        text_gravity = font_standard.render("- Gravity: 3,7 m/s².", True, WHITE)
        text_surface = font_standard.render("- Surface area: 74.800.000 km²", True, WHITE)
        text_age = font_standard.render("- Age: 4,503 * 10^9 years.", True, WHITE)

        WIN.blit(img_bg, (0, 0))
        WIN.blit(img_bigmercury, (0, 80))
        WIN.blit(img_shaft, (1450, 650))
        WIN.blit(text_information, (650, 50))
        WIN.blit(text_lengt_day, (650, 150))
        WIN.blit(text_orbital, (650, 250))
        WIN.blit(text_radius, (650, 350))
        WIN.blit(text_mass, (650, 450))
        WIN.blit(text_gravity, (650, 550))
        WIN.blit(text_surface, (650, 650))
        WIN.blit(text_age, (1000, 50))

        pygame.draw.rect(WIN, WHITE, rect_shaft, -1)

        pygame.display.update()

    pygame.quit()


def venus():
    # Config
    WIDTH = 1520
    HEIGHT = 720
    WIN = pygame.display.set_mode((WIDTH, HEIGHT))

    # Images
    img_bg = pygame.image.load("bg.jpg")

    img_bigvenus = pygame.image.load("bigvenus.png")

    game_over = False
    while game_over != True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True

            if event.type == pygame.MOUSEBUTTONDOWN:
                if rect_shaft.collidepoint(pygame.mouse.get_pos()):
                    return

        text_information = font_standard.render("- Second planet of the solar system.", True, WHITE)
        text_lengt_day = font_standard.render("- Length of day: 116d 18h 0m.", True, WHITE)
        text_orbital = font_standard.render("- Orbital period: 225 days.", True, WHITE)
        text_radius = font_standard.render("- Radius: 6.051,8 Km.", True, WHITE)
        text_mass = font_standard.render("- Mass: 4,867 * 10^24 Kg.", True, WHITE)
        text_gravity = font_standard.render("- Gravity: 8,87 m/s².", True, WHITE)
        text_surface = font_standard.render("- Surface area: 460.200.000 km²", True, WHITE)
        text_age = font_standard.render("- Age: 4,503 * 10^9 years.", True, WHITE)
        text_name = font_standard.render("- It was named after the Roman goddess of love", True, WHITE)
        text_name2 = font_standard.render("and beauty Venus, equivalent to Aphrodite.", True, WHITE)

        WIN.blit(img_bg, (0, 0))
        WIN.blit(img_bigvenus, (0, 80))
        WIN.blit(img_shaft, (1450, 650))
        WIN.blit(text_information, (650, 50))
        WIN.blit(text_lengt_day, (650, 150))
        WIN.blit(text_orbital, (650, 250))
        WIN.blit(text_radius, (650, 350))
        WIN.blit(text_mass, (650, 450))
        WIN.blit(text_gravity, (650, 550))
        WIN.blit(text_surface, (650, 650))
        WIN.blit(text_age, (1000, 150))
        WIN.blit(text_name, (1000, 50))
        WIN.blit(text_name2, (1012, 80))

        pygame.draw.rect(WIN, WHITE, rect_shaft, -1)

        pygame.display.update()

    pygame.quit()


def earth():
    # Config
    WIDTH = 1520
    HEIGHT = 720
    WIN = pygame.display.set_mode((WIDTH, HEIGHT))

    # Images
    img_bg = pygame.image.load("bg.jpg")

    img_bigearth = pygame.image.load("bigearth.png")

    game_over = False
    while game_over != True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True

            if event.type == pygame.MOUSEBUTTONDOWN:
                if rect_shaft.collidepoint(pygame.mouse.get_pos()):
                    return

        text_information = font_standard.render("- Second planet of the solar system.", True, WHITE)
        text_lengt_day = font_standard.render("- Length of day: 116d 18h 0m.", True, WHITE)
        text_orbital = font_standard.render("- Orbital period: 225 days.", True, WHITE)
        text_radius = font_standard.render("- Radius: 6.051,8 Km.", True, WHITE)
        text_mass = font_standard.render("- Mass: 4,867 * 10^24 Kg.", True, WHITE)
        text_gravity = font_standard.render("- Gravity: 8,87 m/s².", True, WHITE)
        text_surface = font_standard.render("- Surface area: 460.200.000 km²", True, WHITE)
        text_age = font_standard.render("- Age: 4,503 * 10^9 years.", True, WHITE)

        WIN.blit(img_bg, (0, 0))
        WIN.blit(img_bigearth, (0, 80))
        WIN.blit(img_shaft, (1450, 650))
        WIN.blit(text_information, (650, 50))
        WIN.blit(text_lengt_day, (650, 150))
        WIN.blit(text_orbital, (650, 250))
        WIN.blit(text_radius, (650, 350))
        WIN.blit(text_mass, (650, 450))
        WIN.blit(text_gravity, (650, 550))
        WIN.blit(text_surface, (650, 650))
        WIN.blit(text_age, (1000, 50))

        pygame.draw.rect(WIN, WHITE, rect_shaft, -1)

        pygame.display.update()

    pygame.quit()


def moon():
    # Config
    WIDTH = 1520
    HEIGHT = 720
    WIN = pygame.display.set_mode((WIDTH, HEIGHT))

    # Images
    img_bg = pygame.image.load("bg.jpg")

    img_bigmoon = pygame.image.load("bigmoon.png")

    game_over = False
    while game_over != True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True

            if event.type == pygame.MOUSEBUTTONDOWN:
                if rect_shaft.collidepoint(pygame.mouse.get_pos()):
                    return

        text_information = font_standard.render("- Earth's natural satellite and the fifth largest in the Solar System.", True, WHITE)
        text_lengt_day = font_standard.render("- Length of day: 29,5 days.", True, WHITE)
        text_orbital = font_standard.render("- Orbital period: 27 days.", True, WHITE)
        text_radius = font_standard.render("- Radius: 1.737,1 Km.", True, WHITE)
        text_mass = font_standard.render("- Mass: 7,349 * 10^22 Kg.", True, WHITE)
        text_gravity = font_standard.render("- Gravity: 1,62 m/s².", True, WHITE)
        text_surface = font_standard.render("- Surface area: 3,793 x 107 km²", True, WHITE)
        text_age = font_standard.render("- Age: 4,53 * 10^9 years.", True, WHITE)

        WIN.blit(img_bg, (0, 0))
        WIN.blit(img_bigmoon, (20, 80))
        WIN.blit(img_shaft, (1450, 650))
        WIN.blit(text_information, (650, 50))
        WIN.blit(text_lengt_day, (650, 150))
        WIN.blit(text_orbital, (650, 250))
        WIN.blit(text_radius, (650, 350))
        WIN.blit(text_mass, (650, 450))
        WIN.blit(text_gravity, (650, 550))
        WIN.blit(text_surface, (650, 650))
        WIN.blit(text_age, (1250, 50))

        pygame.draw.rect(WIN, WHITE, rect_shaft, -1)

        pygame.display.update()

    pygame.quit()


def mars():
    # Config
    WIDTH = 1520
    HEIGHT = 720
    WIN = pygame.display.set_mode((WIDTH, HEIGHT))

    # Images
    img_bg = pygame.image.load("bg.jpg")

    img_bigmars = pygame.image.load("bigmars.png")

    game_over = False
    while game_over != True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True

            if event.type == pygame.MOUSEBUTTONDOWN:
                if rect_shaft.collidepoint(pygame.mouse.get_pos()):
                    return

        text_information = font_standard.render("- Fourth planet of the solar system.", True, WHITE)
        text_lengt_day = font_standard.render("- Length of day: 1d 0h 37m.", True, WHITE)
        text_orbital = font_standard.render("- Orbital period: 687 days.", True, WHITE)
        text_radius = font_standard.render("- Radius: 3.389,5 Km.", True, WHITE)
        text_mass = font_standard.render("- Mass: 6,39 * 10^23 Kg.", True, WHITE)
        text_gravity = font_standard.render("- Gravity: 3,711 m/s².", True, WHITE)
        text_surface = font_standard.render("- Surface area: 114.800.000 km²", True, WHITE)
        text_age = font_standard.render("- Age: 4,603 * 10^9 years.", True, WHITE)
        text_name = font_standard.render("- Named after the Roman god of war, it is often described", True, WHITE)
        text_name2 = font_standard.render("as Red Planet, because the iron oxide prevalent on its", True, WHITE)
        text_name3 = font_standard.render("surface is similar to an average appearance.", True, WHITE)

        WIN.blit(img_bg, (0, 0))
        WIN.blit(img_bigmars, (0, 80))
        WIN.blit(img_shaft, (1450, 650))
        WIN.blit(text_information, (650, 50))
        WIN.blit(text_lengt_day, (650, 150))
        WIN.blit(text_orbital, (650, 250))
        WIN.blit(text_radius, (650, 350))
        WIN.blit(text_mass, (650, 450))
        WIN.blit(text_gravity, (650, 550))
        WIN.blit(text_surface, (650, 650))
        WIN.blit(text_age, (1000, 150))
        WIN.blit(text_name, (1000, 50))
        WIN.blit(text_name2, (1012, 80))
        WIN.blit(text_name3, (1012, 110))

        pygame.draw.rect(WIN, WHITE, rect_shaft, -1)

        pygame.display.update()

    pygame.quit()


def jupiter():
    # Config
    WIDTH = 1520
    HEIGHT = 720
    WIN = pygame.display.set_mode((WIDTH, HEIGHT))

    # Images
    img_bg = pygame.image.load("bg.jpg")

    img_bigjupiter = pygame.image.load("bigjupiter.png")

    game_over = False
    while game_over != True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True

            if event.type == pygame.MOUSEBUTTONDOWN:
                if rect_shaft.collidepoint(pygame.mouse.get_pos()):
                    return

        text_information = font_standard.render("- Fifth planet of the solar system.", True, WHITE)
        text_lengt_day = font_standard.render("- Length of day: 0d 9h 56m.", True, WHITE)
        text_orbital = font_standard.render("- Orbital period: 12 years.", True, WHITE)
        text_radius = font_standard.render("- Radius: 69.911 Km.", True, WHITE)
        text_mass = font_standard.render("- Mass: 1,898 * 10^27 Kg.", True, WHITE)
        text_gravity = font_standard.render("- Gravity: 24,79 m/s².", True, WHITE)
        text_surface = font_standard.render("- Surface area: 6,142 *^10 km²", True, WHITE)
        text_age = font_standard.render("- Age: 4,503 * 10^9 years.", True, WHITE)
        text_name = font_standard.render("- Jupiter is the largest planet in the Solar System, both in", True, WHITE)
        text_name2 = font_standard.render("diameter and mass.", True, WHITE)

        WIN.blit(img_bg, (0, 0))
        WIN.blit(img_bigjupiter, (0, 80))
        WIN.blit(img_shaft, (1450, 650))
        WIN.blit(text_information, (650, 50))
        WIN.blit(text_lengt_day, (650, 150))
        WIN.blit(text_orbital, (650, 250))
        WIN.blit(text_radius, (650, 350))
        WIN.blit(text_mass, (650, 450))
        WIN.blit(text_gravity, (650, 550))
        WIN.blit(text_surface, (650, 650))
        WIN.blit(text_age, (1000, 150))
        WIN.blit(text_name, (1000, 50))
        WIN.blit(text_name2, (1012, 80))

        pygame.draw.rect(WIN, WHITE, rect_shaft, -1)

        pygame.display.update()

    pygame.quit()


def saturn():
    # Config
    WIDTH = 1520
    HEIGHT = 720
    WIN = pygame.display.set_mode((WIDTH, HEIGHT))

    # Images
    img_bg = pygame.image.load("bg.jpg")

    img_bigsaturn = pygame.image.load("bigsaturn.png")

    game_over = False
    while game_over != True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True

            if event.type == pygame.MOUSEBUTTONDOWN:
                if rect_shaft.collidepoint(pygame.mouse.get_pos()):
                    return

        text_information = font_standard.render("- Sixth planet of the solar system.", True, WHITE)
        text_group = font_standard.render("- Belonging to the group of gas giants", True, WHITE)
        text_number_masses = font_standard.render("- Has about 95 land masses", True, WHITE)
        text_lengt_day = font_standard.render("- Length of day: 0d 10h 42m.", True, WHITE)
        text_orbital = font_standard.render("- Orbital period: 29 years.", True, WHITE)
        text_radius = font_standard.render("- Radius: 58.232 Km.", True, WHITE)
        text_mass = font_standard.render("- Mass: 5,683 × 10^26 Kg.", True, WHITE)
        text_gravity = font_standard.render("- Gravity: 10,44 m/s².", True, WHITE)
        text_surface = font_standard.render("- Surface area: 4,27 × 10^10 km²", True, WHITE)
        text_age = font_standard.render("- Age: 4,503 * 10^9 years.", True, WHITE)
        text_orbits = font_standard.render("- And orbits an average distance of 9.5 astronomical units.", True, WHITE)

        WIN.blit(img_bg, (0, 0))
        WIN.blit(img_bigsaturn, (0, 180))
        WIN.blit(img_shaft, (1450, 650))
        WIN.blit(text_information, (650, 50))
        WIN.blit(text_lengt_day, (650, 150))
        WIN.blit(text_orbital, (650, 250))
        WIN.blit(text_radius, (650, 350))
        WIN.blit(text_mass, (650, 450))
        WIN.blit(text_gravity, (650, 550))
        WIN.blit(text_surface, (650, 650))
        WIN.blit(text_age, (1000, 150))
        WIN.blit(text_group, (1000, 50))
        WIN.blit(text_number_masses, (1000, 250))
        WIN.blit(text_orbits, (1000, 350))

        pygame.draw.rect(WIN, WHITE, rect_shaft, -1)

        pygame.display.update()

    pygame.quit()


def uranus():
    # Config
    WIDTH = 1520
    HEIGHT = 720
    WIN = pygame.display.set_mode((WIDTH, HEIGHT))

    # Images
    img_bg = pygame.image.load("bg.jpg")

    img_biguranus = pygame.image.load("biguranus.png")

    game_over = False
    while game_over != True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True

            if event.type == pygame.MOUSEBUTTONDOWN:
                if rect_shaft.collidepoint(pygame.mouse.get_pos()):
                    return

        text_information = font_standard.render("- Seventh planet of the solar system.", True, WHITE)
        text_lengt_day = font_standard.render("- Length of day: 0d 17h 14m.", True, WHITE)
        text_orbital = font_standard.render("- Orbital period: 84 years.", True, WHITE)
        text_radius = font_standard.render("- Radius: 25.362 km.", True, WHITE)
        text_mass = font_standard.render("- Mass: 8,681 × 10^25 kg.", True, WHITE)
        text_gravity = font_standard.render("- Gravity: 8,87 m/s²².", True, WHITE)
        text_surface = font_standard.render("- Surface area: 8,083 × 10^9 km²", True, WHITE)
        text_age = font_standard.render("- Age: 4,503 × 10^9 anos.", True, WHITE)

        WIN.blit(img_bg, (0, 0))
        WIN.blit(img_biguranus, (0, 80))
        WIN.blit(img_shaft, (1450, 650))
        WIN.blit(text_information, (650, 50))
        WIN.blit(text_lengt_day, (650, 150))
        WIN.blit(text_orbital, (650, 250))
        WIN.blit(text_radius, (650, 350))
        WIN.blit(text_mass, (650, 450))
        WIN.blit(text_gravity, (650, 550))
        WIN.blit(text_surface, (650, 650))
        WIN.blit(text_age, (1000, 50))

        pygame.draw.rect(WIN, WHITE, rect_shaft, -1)

        pygame.display.update()

    pygame.quit()


def neptune():
    # Config
    WIDTH = 1520
    HEIGHT = 720
    WIN = pygame.display.set_mode((WIDTH, HEIGHT))

    # Images
    img_bg = pygame.image.load("bg.jpg")

    img_bigneptune = pygame.image.load("bigneptune.png")

    game_over = False
    while game_over != True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True

            if event.type == pygame.MOUSEBUTTONDOWN:
                if rect_shaft.collidepoint(pygame.mouse.get_pos()):
                    return

        text_information = font_standard.render("- Last planet of the solar system.", True, WHITE)
        text_name = font_standard.render("- Belonging to the group of gas giants", True, WHITE)
        text_lengt_day = font_standard.render("- Length of day: 0d 16h 6m.", True, WHITE)
        text_orbital = font_standard.render("- Orbital period: 165 years.", True, WHITE)
        text_radius = font_standard.render("- Radius: 24.622 km.", True, WHITE)
        text_mass = font_standard.render("- Mass: 1,024 × 10^26 kg.", True, WHITE)
        text_gravity = font_standard.render("- Gravity: 11,15 m/s²", True, WHITE)
        text_surface = font_standard.render("- Surface area:7,618 × 10^9 km²", True, WHITE)
        text_age = font_standard.render("- Age: 4,503 * 10^9 years.", True, WHITE)

        WIN.blit(img_bg, (0, 0))
        WIN.blit(img_bigneptune, (0, 80))
        WIN.blit(img_shaft, (1450, 650))
        WIN.blit(text_information, (650, 50))
        WIN.blit(text_lengt_day, (650, 150))
        WIN.blit(text_orbital, (650, 250))
        WIN.blit(text_radius, (650, 350))
        WIN.blit(text_mass, (650, 450))
        WIN.blit(text_gravity, (650, 550))
        WIN.blit(text_surface, (650, 650))
        WIN.blit(text_name, (1000, 50))
        WIN.blit(text_age, (1000, 150))

        pygame.draw.rect(WIN, WHITE, rect_shaft, -1)

        pygame.display.update()

    pygame.quit()


def simulator():
    # Config
    WIDTH = 1520
    HEIGHT = 720
    WIN = pygame.display.set_mode((WIDTH, HEIGHT))
    WIN_RECT = WIN.get_rect()
    CLOCK = pygame.time.Clock()
    FPS = 40

    class Planet:
        def __init__(self, name, r, d, a, c):
            self.name = name
            self.radius = r
            self.distance = d
            self.angle = a
            self.color = c

        def paint(self, WIN):
            center_x = int(WIDTH / 2)
            center_y = int(HEIGHT / 2)
            x = round(self.distance * math.cos(self.angle) + center_x)
            y = round(self.distance * math.sin(self.angle) + center_y)
            pygame.draw.circle(WIN, self.color, (x, y), self.radius)
            font = pygame.font.Font(None, 20)
            text = font.render(self.name, 1, (255, 255, 255))
            text2 = font.render(str(self.distance), 1, (255, 255, 255))
            WIN.blit(text2, (x - 20, y - 17))
            WIN.blit(text, (x - 30, y - 30))

    # 2439
    mercury = Planet("Mercury", 2, 55, random.randint(0, 360), (200, 200, 200))
    # 6051
    venus = Planet("Venus", 2, 75, random.randint(0, 360), (127, 127, 127))
    # 6371
    earth = Planet("Earth", 2, 95, random.randint(0, 360), (0, 255, 255))
    # 3389
    mars = Planet("Mars", 2, 115, random.randint(0, 360), (255, 0, 0))
    # 69911
    jupiter = Planet("Jupiter", 2, 135, random.randint(0, 360), (100, 40, 0))
    # 58232
    saturn = Planet("Saturn", 2, 155, 0, (115, 0, 0))
    # 25362
    uranus = Planet("Uranus", 2, 200, 0, (200, 200, 200))
    # 24622
    neptune = Planet("Neptune", 2, 250, 0, (0, 0, 255))

    planets = [mercury, venus, earth, mars, jupiter, saturn, uranus, neptune]

    game_over = False
    while game_over != True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True

            if event.type == pygame.MOUSEBUTTONDOWN:
                if rect_shaft.collidepoint(pygame.mouse.get_pos()):
                    return

        WIN.fill(BLACK)

        WIN.blit(img_shaft, (1450, 650))

        pygame.draw.circle(WIN, (random.randint(240, 255), random.randint(240, 255), 0), (int(WIDTH / 2), int(HEIGHT / 2)), 50)

        for p in planets:
            p.angle = p.angle + 0.01
            p.paint(WIN)

        pygame.display.flip()

        CLOCK.tick(FPS)

    pygame.quit()
