import pygame
import random

width = 640
height = 480
icon = pygame.image.load("snake.ico")
pygame.display.set_icon(icon)

# Taille des carrés dans la grille
square_size = 32

# Largeur et hauteur de la grille
grid_width = width / square_size
grid_height = height / square_size

FPS = 10

# Couleurs
grid_color = (216, 216, 216)
snake_color = (22, 240, 26)
bg_color = (0, 0, 0)
apple_color = (255, 0, 0)

# Jeu
class Game():
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode((width, height))
        pygame.display.set_caption("Snake - Christopher CORNET")
        self.fps = pygame.time.Clock()
        # Direction
        self.direction = 1
        self.score = 0

    # Afficher le serpent, et les pommes
    def elements(self):
        self.snake_apple = pygame.sprite.Group()
        self.head = Snake(self, 8, 7)
        self.body = []
        self.body.append(Snake(self, 4, 5))
        self.body.append(Snake(self, 3, 5))

        # Pomme emplacement aléatoire
        self.apple = Apple(self, random.randint(0, 18), random.randint(0, 14))

    def check_coords(self):
        x = random.randrange(0, grid_width - 1)
        y = random.randrange(0, grid_height - 1)
        
        for parts in self.body:
            if x == parts.x and y == parts.y:
                x, y = self.check_coords()
        return x, y

    # Lancer le jeu
    def run(self):
        # Boucle de jeu
        self.running = True
        while self.running:
            self.fps.tick(FPS)
            self.events()
            self.update_game()
            self.display_grid()

    # Mettre à jour l'affichage du serpent et des pommes
    def update_game(self):
        # Augmenter la taille du serpent à chaque pomme mangée
        if self.apple.apple_hit():
            x, y = self.check_coords()
            self.apple.x = x
            self.apple.y = y
            self.body.append(Snake(self, self.body[-1].x, self.body[-1].y))
            self.score += 1

        # Afficher le serpent et la pomme (update)
        self.snake_apple.update()

        # Bouger les parties du corps du serpent
        x, y = self.head.x, self.head.y
        for parts in self.body:
            temp_x, temp_y = parts.x, parts.y
            parts.x, parts.y = x, y
            x, y = temp_x, temp_y

        # Avance automatiquement dans la dernière direction choisie
        if self.direction == 1:
            self.head.y -= 1 # Haut
        elif self.direction == 2:
            self.head.y += 1 # Bas
        elif self.direction == 3:
            self.head.x -= 1 # Gauche
        elif self.direction == 4:
            self.head.x += 1 # Droite

        # Condition de défaite
        for i in self.body:
            if i.snake_hit():
                self.running = False

    # Grille
    def grid(self):
        # Lignes de la grille
        for row in range(0, width, square_size):
            pygame.draw.line(self.window, grid_color, (row, 0), (row, height)) # x,y 1er point, x,y 2e point
        for col in range(0, height, square_size):
            pygame.draw.line(self.window, grid_color, (0, col), (width, col)) # x,y 1er point, x,y 2e point

    # Afficher la grille
    def display_grid(self):
        self.window.fill(bg_color)
        self.snake_apple.draw(self.window)
        self.grid()
        pygame.display.flip()

    # Evenements
    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.end()
            # Mouvements du serpent
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    if not self.direction == 2:
                        self.direction = 1
                elif event.key == pygame.K_DOWN:
                    if not self.direction == 1:
                        self.direction = 2
                elif event.key == pygame.K_LEFT:
                    if not self.direction == 4:
                        self.direction = 3
                elif event.key == pygame.K_RIGHT:
                    if not self.direction == 3:
                        self.direction = 4

    # Quitter le jeu
    def end(self):
        pygame.quit()
        quit(0)

# Serpent
class Snake(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        self.groups = game.snake_apple
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.x, self.y = x, y # Coordonées du serpent
        self.image = pygame.Surface((square_size, square_size)) # Serpent de la taille d'un carré
        self.image.fill(snake_color)
        self.rect = self.image.get_rect()

    def snake_hit(self):
        if self.x == self.game.head.x and self.y == self.game.head.y:
            return True
        return False

    def update(self):
        self.rect.x = self.x * square_size
        self.rect.y = self.y * square_size

# Pomme
class Apple(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        self.groups = game.snake_apple
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.x, self.y = x, y # Coordonées de la pomme
        self.image = pygame.Surface((square_size, square_size)) # Pomme de la taille d'un carré
        self.image.fill(apple_color)
        self.rect = self.image.get_rect()

    # Pomme touchée
    def apple_hit(self):
        if self.game.head.x == self.x and self.game.head.y == self.y:
            return True
        return False

    def update(self):
        self.rect.x = self.x * square_size
        self.rect.y = self.y * square_size

snake_game = Game()
while True:
    # Afficher le serpent et la pomme sur le jeu, Lancer le jeu
    snake_game.elements()
    snake_game.run()