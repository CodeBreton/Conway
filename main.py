import pygame
import random
import time

def generer_grille(longueur, largeur):
    return [[False for _ in range(longueur)] for _ in range(largeur)]

def cases_aleatoires(grille, nb_cases_true):
    longueur, largeur = len(grille), len(grille[0])
    cases_disponibles = [(i, j) for i in range(longueur) for j in range(largeur)]
    random.shuffle(cases_disponibles)

    for i, j in cases_disponibles[:nb_cases_true]:
        grille[i][j] = True

    return grille

def afficher_grille(grille, taille_case, screen):
    screen.fill((255, 255, 255))
    for i in range(len(grille)):
        for j in range(len(grille[i])):
            x = j * taille_case
            y = i * taille_case
            couleur = (0, 0, 0) if grille[i][j] else (255, 255, 255)
            pygame.draw.rect(screen, couleur, (x, y, taille_case, taille_case))
            pygame.draw.rect(screen, (200, 200, 200), (x, y, taille_case, taille_case), 1) # Grille

def compter_voisins(grille, x, y):
    voisins = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    count = 0
    for dx, dy in voisins:
        nx, ny = x + dx, y + dy
        if 0 <= nx < len(grille) and 0 <= ny < len(grille[0]):
            count += grille[nx][ny]
    return count

def prochaine_generation(grille):
    nouvelle_grille = generer_grille(len(grille), len(grille[0]))
    for i in range(len(grille)):
        for j in range(len(grille[i])):
            voisins = compter_voisins(grille, i, j)
            if grille[i][j]:
                if voisins == 2 or voisins == 3:
                    nouvelle_grille[i][j] = True
            else:
                if voisins == 3:
                    nouvelle_grille[i][j] = True
    return nouvelle_grille

def game_de_la_vie(longueur, largeur, taille_case):
    pygame.init()
    screen = pygame.display.set_mode((longueur * taille_case, largeur * taille_case))
    pygame.display.set_caption("Jeu de la Vie")

    grille = generer_grille(longueur, largeur)

    # Glider
    inserer_cellule(grille, 10, 10)
    inserer_cellule(grille, 9, 10)
    inserer_cellule(grille, 11, 10)
    inserer_cellule(grille, 11, 9)
    inserer_cellule(grille, 10, 8)

    clock = pygame.time.Clock()
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        grille = prochaine_generation(grille)
        afficher_grille(grille, taille_case, screen)
        pygame.display.flip()
        clock.tick(10)

    pygame.quit()

def inserer_cellule(grille, x, y):
    if 0 <= x < len(grille) and 0 <= y < len(grille[0]):
        grille[x][y] = True

# Lancer le jeu
game_de_la_vie(50, 50, 20)