import pygame

pygame.init()
window = pygame.display.set_mode((600, 500))
pygame.display.set_caption("Snake - Christopher CORNET")
icon = pygame.image.load("snake.ico")
pygame.display.set_icon(icon)
FPS = 30
CLOCK = pygame.time.Clock()

# Serpent commence à la taille de 1 bloc
snake_size = 1
snake_color = (70, 255, 0) # couleur serpent = vert

apple_color = (255, 0, 0) # couleur pomme = rouge

# Serpent avance toujours vers l'avant de 1 bloc

# Le serpent doit manger des pommes qui apparaissent aléatoirement

# Si le serpent mange une pomme: augmenter de 1 bloc sa taille, augmenter le score de 1
# Si le serpent se touche lui même ou la bordure de la fenêtre, fin de la partie

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    pygame.draw.rect(window, snake_color, (250, 200, 25, 25)) # x,y - width,height
    pygame.draw.rect(window, apple_color, (500, 500, 25, 25)) # x,y - width,height
    pygame.display.flip()
    CLOCK.tick(FPS)
pygame.quit()