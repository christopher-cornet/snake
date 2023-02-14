import pygame
import random

width = 610
height = 480
icon = pygame.image.load("snake.ico")
pygame.display.set_icon(icon)

grid_color = (216, 216, 216) # Couleur des lignes de la grille

# Taille des carrés dans la grille
square_size = 32
# Largeur et hauteur de la grille
grid_width = width / square_size
grid_height = height / square_size

FPS = 10

# Jeu
class Game():
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode((width, height))
        pygame.display.set_caption("Snake - Christopher CORNET")
        self.clock = pygame.time.Clock()

    # Lancer le jeu
    def run(self):
        # Boucle de jeu
        self.running = True
        while self.running:
            self.clock.tick(FPS)
            self.events()
            self.display_grid()

    def grid(self):
        # Lignes de la grille
        for row in range(0, width, square_size):
            pygame.draw.line(self.window, grid_color, (row, 0), (row, height)) # fenêtre, couleur, x,y 1er point, x,y 2e point
        for col in range(0, height, square_size):
            pygame.draw.line(self.window, grid_color, (0, col), (width, col)) # fenêtre, couleur, x,y 1er point, x,y 2e point

    def display_grid(self):
        # Afficher la grille
        self.grid()
        pygame.display.flip()

    def events(self):
        # Evenements
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.quit()

snake_game = Game()
while True:
    # Lancer le jeu
    snake_game.run()