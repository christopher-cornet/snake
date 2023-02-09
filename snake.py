import pygame
import random

pygame.init()
window = pygame.display.set_mode((600, 500))
pygame.display.set_caption("Snake - Christopher CORNET")
icon = pygame.image.load("snake.ico")
pygame.display.set_icon(icon)
FPS = 30
CLOCK = pygame.time.Clock()

# Snake
snake_size = 1
snake_color = (70, 255, 0) # couleur serpent = vert
snake_x = 250
snake_y = 200
snake_speed = 5

# Serpent avance toujours vers l'avant de 1 bloc

# Le serpent doit manger des pommes qui apparaissent aléatoirement

# Si le serpent se touche lui même ou la bordure de la fenêtre, fin de la partie

# Condition si serpent mange la pomme: augmente le score de 1, augmente le score et génère une nouvelle pomme à un x,y
# random, augmenter de 1 bloc sa taille

# Pomme
apple_color = (255, 0, 0) # couleur pomme = rouge
snake = pygame.draw.rect(window, apple_color, (random.randint(0, 600),random.randint(0, 500), 25, 25)) # x,y - width,height

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                snake_x += 30
            if event.key == pygame.K_LEFT:
                snake_x -= 30
            if event.key == pygame.K_UP:
                snake_y -= 30
            if event.key == pygame.K_DOWN:
                snake_y += 30
    pygame.draw.rect(window, snake_color, (snake_x, snake_y, 25, 25)) # x,y - width,height
    pygame.display.flip()
    CLOCK.tick(FPS)
pygame.quit()