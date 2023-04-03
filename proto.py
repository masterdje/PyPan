import pygame

# Initialisation de Pygame
pygame.init()

# Récupération des dimensions de l'écran
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

# Chargement de l'image et redimensionnement à la taille de l'écran
image = pygame.image.load("GB01.png")
image = pygame.transform.scale(image, (screen.get_width(), screen.get_height()))

# Affichage de l'image en plein écran
screen.blit(image, (0, 0))

# Rafraîchissement de l'affichage de la fenêtre
pygame.display.flip()

# Boucle d'événements pour maintenir la fenêtre ouverte
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

# Fermeture de Pygame
pygame.quit()
