import pygame
import random

width = 610
height = 480
icon = pygame.image.load("snake.ico")
pygame.display.set_icon(icon)

# Carrés dans la grille
square = 32
# Largeur et hauteur de la grille
grid_width = width / square
grid_height = height / square

FPS = 10

class Game():
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode((width, height))
        pygame.display.set_caption("Snake - Christopher CORNET")

    # Lancer le jeu
    def run(self):
        pass

snake_game = Game()
while True:
    # Lancer le jeu
    snake_game.run()