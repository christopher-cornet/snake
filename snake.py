import pygame
import random

width = 610
height = 480
icon = pygame.image.load("snake.ico")
pygame.display.set_icon(icon)

# Couleur des lignes de la grille
grid_color = (216, 216, 216)

# Taille des carrés dans la grille
square_size = 32

# Largeur et hauteur de la grille
grid_width = width / square_size
grid_height = height / square_size

FPS = 10

# Couleur du serpent
snake_color = (22, 240, 26)

# Background color
bg_color = (0, 0, 0)

# Jeu
class Game():
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode((width, height))
        pygame.display.set_caption("Snake - Christopher CORNET")
        self.fps = pygame.time.Clock()
        # Direction
        self.direction = 1

    # Lancer le jeu
    def run(self):
        # Boucle de jeu
        self.running = True
        while self.running:
            self.fps.tick(FPS)
            self.events()
            self.update()
            self.display_grid()

    # Mettre à jour le serpent
    def update(self):
        self.all_sprites.update()
        # Avance automatiquement dans la dernière direction choisie
        if self.direction == 1: # Haut
            self.head.y -= 1 
        elif self.direction == 2: # Bas
            self.head.y += 1 
        elif self.direction == 3: # Gauche
            self.head.x -= 1
        elif self.direction == 4: # Droite
            self.head.x += 1

    # Afficher le serpent
    def snake_body(self):
        self.all_sprites = pygame.sprite.Group()
        self.head = Snake(self, 8, 7)

    # Grille
    def grid(self):
        # Lignes de la grille
        for row in range(0, width, square_size):
            pygame.draw.line(self.window, grid_color, (row, 0), (row, height)) # fenêtre, couleur, x,y 1er point, x,y 2e point
        for col in range(0, height, square_size):
            pygame.draw.line(self.window, grid_color, (0, col), (width, col)) # fenêtre, couleur, x,y 1er point, x,y 2e point

    # Afficher la grille
    def display_grid(self):
        self.window.fill(bg_color)
        self.grid()
        self.all_sprites.draw(self.window)
        pygame.display.flip()

    # Evenements
    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.quit()
            # Mouvements du serpent
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    if not self.direction == 2:
                        self.direction = 1
                if event.key == pygame.K_DOWN:
                    if not self.direction == 1:
                        self.direction = 2
                if event.key == pygame.K_LEFT:
                    if not self.direction == 4:
                        self.direction = 3
                if event.key == pygame.K_RIGHT:
                    if not self.direction == 3:
                        self.direction = 4

# Serpent
class Snake(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        self.groups = game.all_sprites
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.x, self.y = x, y # Coordonées du serpent
        self.image = pygame.Surface((square_size, square_size))
        self.image.fill(snake_color) # Couleur du serpent
        self.rect = self.image.get_rect()

    def update(self):
        self.rect.x = self.x * square_size
        self.rect.y = self.y * square_size

snake_game = Game()
while True:
    # Afficher le serpent sur le jeu, Lancer le jeu
    snake_game.snake_body()
    snake_game.run()