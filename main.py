import pygame
import random

def generer_grille(longueur, largeur): # Complexité en O(n * m)
    # Génère une grille de dimensions 'longueur' x 'largeur' initialisée avec des valeurs 'False'
    return [[False for _ in range(longueur)] for _ in range(largeur)]

def cases_aleatoires(grille, nb_cases_true):
    # Place aléatoirement 'nb_cases_true' cellules à 'True' dans la grille
    longueur, largeur = len(grille), len(grille[0])
    cases_disponibles = [(i, j) for i in range(longueur) for j in range(largeur)] # Complexité en O(n * m) pour générer la liste des positions disponibles
    random.shuffle(cases_disponibles)

    for i, j in cases_disponibles[:nb_cases_true]: # Complexité en O(k) pour mélanger et sélectionner les positions où k est nb_cases_true
        grille[i][j] = True

    return grille

def afficher_grille(grille, taille_case, screen):
    # Affiche la grille sur l'écran 'screen' avec des cases de taille 'taille_case'
    screen.fill((255, 255, 255))  # Remplit l'écran en blanc

    for i in range(len(grille)): # Complexité en O(n * m) car chaque cellule de la grille est vérifiée et dessinée
        for j in range(len(grille[i])):
            x = j * taille_case
            y = i * taille_case

            # Choisit la couleur en fonction de l'état de la cellule
            if grille[i][j]:
                couleur = (0, 0, 0)
            else:
                couleur = (255, 255, 255)

            pygame.draw.rect(screen, couleur, (x, y, taille_case, taille_case))
            pygame.draw.rect(screen, (200, 200, 200), (x, y, taille_case, taille_case), 1)

def compter_voisins(grille, x, y):
    # Compte le nombre de voisins 'True' autour de la cellule (x, y)
    voisins = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    count = 0
    for dx, dy in voisins: # Complexité en O(1) car le nombre de voisins est fixe (8 voisins maximum)
        nx, ny = x + dx, y + dy
        if 0 <= nx < len(grille) and 0 <= ny < len(grille[0]):
            count += grille[nx][ny]
    return count

def prochaine_generation(grille):
    # Génère la grille de la prochaine génération selon les règles du Jeu de la Vie
    # Complexité en O(n * m) car chaque cellule doit être vérifiée et mise à jour en fonction de ses voisins
    nouvelle_grille = generer_grille(len(grille), len(grille[0]))
    for i in range(len(grille)):
        for j in range(len(grille[i])):
            voisins = compter_voisins(grille, i, j)
            if grille[i][j]:
                # Une cellule vivante reste vivante si elle a 2 ou 3 voisins vivants
                if voisins == 2 or voisins == 3:
                    nouvelle_grille[i][j] = True
            else:
                # Une cellule morte devient vivante si elle a exactement 3 voisins vivants
                if voisins == 3:
                    nouvelle_grille[i][j] = True
    return nouvelle_grille

def inserer_cellule(grille, x, y):
    # Insère une cellule vivante à la position (x, y) si celle-ci est dans les limites de la grille
    if 0 <= x < len(grille) and 0 <= y < len(grille[0]):
        grille[x][y] = True

def Game(longueur, largeur, taille_case):
    # Complexité en O(T) ∗ O(n ∗ m) = O(T ∗ n ∗ m) où T est le nombre d'itérations de la boucle principale
    # Fonction principale pour initialiser et exécuter le jeu
    pygame.init()
    screen = pygame.display.set_mode((longueur * taille_case, largeur * taille_case))
    pygame.display.set_caption("Jeu de la Vie")

    grille = generer_grille(longueur, largeur)

    # Insère un motif "Glider" dans la grille pour démonstration
    inserer_cellule(grille, 10, 10)
    inserer_cellule(grille, 9, 10)
    inserer_cellule(grille, 11, 10)
    inserer_cellule(grille, 11, 9)
    inserer_cellule(grille, 10, 8)

    clock = pygame.time.Clock()
    running = True

    while running:
        # Gestion des événements pour quitter le jeu
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Mise à jour de la grille pour la prochaine génération
        grille = prochaine_generation(grille)
        # Affichage de la grille mise à jour.
        afficher_grille(grille, taille_case, screen)
        pygame.display.flip()
        clock.tick(10)  # Vitesse de mise à jour

    pygame.quit()

# Lancement du jeu avec une grille de 50x50 cases de taille 20 pixels chacune
Game(50, 50, 10)