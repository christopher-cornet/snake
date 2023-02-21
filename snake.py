import pygame
import random

width = 640
height = 480

# Taille des carrés dans la grille
square_size = 32

# Largeur et hauteur de la grille
grid_width = width / square_size
grid_height = height / square_size

FPS = 10

# Couleurs
grid_color = (0, 0, 0)
snake_color = (255, 231, 82)
bg_color = (0, 0, 0)
apple_color = (148, 40, 255)
btn_color = (35, 35, 35)

# Jeu
class Game():
    def __init__(self):
        pygame.init()
        icon = pygame.image.load("snake.ico")
        pygame.display.set_icon(icon)
        self.window = pygame.display.set_mode((width, height))
        pygame.display.set_caption("Snake - Christopher CORNET")
        self.fps = pygame.time.Clock()
        # Direction
        self.direction = 1
        self.score = 0
        self.pause = False
        self.high_score = self.get_high_score()

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
        x = random.randint(0, grid_width - 1)
        y = random.randint(0, grid_height - 1)
        
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
                print(self.score) # Print le score
                self.running = False

    # Grille
    def grid(self):
        # Lignes de la grille
        for row in range(0, width, square_size):
            pygame.draw.line(self.window, grid_color, (row, 0), (row, height)) # x,y 1er point, x,y 2e point
        for col in range(0, height, square_size):
            pygame.draw.line(self.window, grid_color, (0, col), (width, col)) # x,y 1er point, x,y 2e point

    # Le serpent apparait à l'opposé quand il sort de l'écran
        if self.head.x > grid_width:
            self.head.x = 0
        elif self.head.x < 0:
            self.head.x = grid_width
        elif self.head.y > grid_height:
            self.head.y = 0
        elif self.head.y < 0:
            self.head.y = grid_height

    # Afficher la grille
    def display_grid(self):
        self.window.fill(bg_color)
        self.snake_apple.draw(self.window)
        self.grid()
        if self.pause:
            Menu(10, 10, "PAUSE").draw(self.window, 100)
        pygame.display.flip()

    # Meilleur score
    def get_high_score(self):
        with open("score.txt", "r") as file:
            score = file.read()
        return int(score)

    # Enregistrer le plus grand score
    def save_score(self):
        with open("score.txt", "w") as file:
            # Score plus grand que le meilleur score = écrire un nouveau score, sinon écrire le meilleur score
            if self.score > self.high_score:
                file.write(str(self.score))
            else:
                file.write(str(self.high_score))

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
                if event.type == pygame.K_ESCAPE:
                    self.pause = not self.pause

    # Menu
    def menu(self):
        self.save_score()
        self.window.fill(btn_color)
        if not self.run:
            Menu(8, 7, "PERDU !").draw(self.window, 80)
            Menu(14, 13, f"Score: {self.score}").draw(self.window, 30)
        else:
            Menu(6.6, 2.5, "SNAKE").draw(self.window, 80)

        Menu(6.5, 6, f"Meilleur score: {self.high_score if self.high_score > self.score else self.score}").draw(self.window, 30)

        # Boutons
        self.start_button = Button(self, ((148, 40, 255)), ((148, 40, 255)), width / 2 - (150/2), 270, 150, 50, "JOUER")
        self.quit_button = Button(self, ((148, 40, 255)), ((148, 40, 255)), width / 2 - (150/2), 345, 150, 50, "QUITTER")
        self.expect()

    # Tant que jouer ou quitter n'est pas cliqué afficher le menu
    def expect(self):
        expecting = True
        while expecting:
            self.start_button.draw(self.window)
            self.quit_button.draw(self.window)
            pygame.display.flip()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.end()
                mouse_x, mouse_y = pygame.mouse.get_pos()
                if event.type == pygame.MOUSEMOTION:
                    if self.start_button.onclick(mouse_x, mouse_y):
                        self.start_button.color = ((118, 27, 207))
                    else:
                        self.start_button.color = (148, 40, 255)
                    if self.quit_button.onclick(mouse_x, mouse_y):
                        self.quit_button.color = ((118, 27, 207))
                    else:
                        self.quit_button.color = (148, 40, 255)
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.start_button.onclick(mouse_x, mouse_y):
                        expecting = False
                    if self.quit_button.onclick(mouse_x, mouse_y):
                        self.end()

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

# Menu
class Menu:
    def __init__(self, x, y, text):
        self.x, self.y = x * square_size, y * square_size
        self.text = text

    def draw(self, window, font_size):
        # Titre et score
        font = pygame.font.SysFont("Impact", font_size)
        text = font.render(self.text, True, ((255, 231, 82)))
        window.blit(text, (self.x, self.y))

# Boutons
class Button():
    def __init__(self, game, color, outline, x, y,  width, height, text):
        self.game = game
        self.color, self.outline = color, outline
        self.x, self.y = x, y
        self.width, self.height = width, height
        self.text = text

    def draw(self, window):
        pygame.draw.rect(window, self.outline, (self.x - 2, self.y - 2, self.width + 4, self.height + 4))
        pygame.draw.rect(window, self.color, (self.x, self.y, self.width, self.height))
        font = pygame.font.SysFont("Times new Romans", 30)
        text = font.render(self.text, True, (255, 245, 119))
        draw_x = self.x + (self.width/2 - text.get_width()/2)
        draw_y = self.y + (self.height/2 - text.get_height()/2)
        window.blit(text, (draw_x, draw_y))

    def onclick(self, mouse_x, mouse_y):
        return self.x <= mouse_x <= self.x + self.width and self.y <= mouse_y <= self.y + self.height

snake_game = Game()
while True:
    # Afficher le serpent et la pomme sur le jeu, Lancer le jeu
    snake_game.menu()
    snake_game.elements()
    snake_game.run()