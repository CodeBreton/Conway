##########################################################################
#                                                                        #
#   Nom du programme : SimulationFeuDeForêt                              #
#                                                           ### #   ###  #
#   Date : 2022-2023                                         #  #    #   #
#   Auteur : Josselin LE TALLEC                            ###  ###  #   #
#                                                                        #
##########################################################################

##################### Importation des modules ou fonctions externes #######################

import random
from copy import deepcopy


##################### Définition des fontions locales ######################

def creation(n, p):
    """
    Crée une grille carrée de dimensions n * n, remplie de zéros (vide). Certains éléments de la grille sont alors assignés la valeur 1 (arbre) avec une probabilité p.

    Données : n, de type int, est le nombres de lignes et p, de type float, est la probabilité d'apparition d'un arbre
    Résultat : grille, de type list, est un tableau de tableaux
    """
    grille = [[0 for i in range(n)] for j in range(n)]  # Initialise la grille avec n lignes et n colonnes remplies de zéros
    for ligne in grille:
        for i in range(len(ligne)):
            apparition = (random.randint(0, 100) <= p)  # Génère un nombre aléatoire entre 0 et 100, et vérifie si c'est inférieur ou égal à la probabilité p
            if apparition:
                ligne[i] = 1  # Si c'est le cas, on assigne la valeur 1 (arbre) à la case de la grille
    return grille


def affiche(grille):
    """
    Affiche la grille de manière plus facilement lisible dans le terminal.

    Donnée : grille, de type list, est un tableau de tableaux
    """
    print("\n")
    for i in range(len(grille)):
        print(grille[i])
    print("\n")


def choix_depart_feu(grille):
    """
    Retourne un tuple (ligne, colonne) représentant la position d'un élément aléatoire de la grille qui n'est pas déjà en feu.

    Données : grille, de type list, est un tableau de tableaux
    Résultat : position, de type tuple, comme (ligne, colonne)
    """
    positions_possibles = []
    for i in range(len(grille)):
        for j in range(len(grille[i])):
            if (grille[i][j] != 1):  # Si la case de la grille n'est pas un arbre (donc vaut 0)
                positions_possibles.append((i, j))

    position = positions_possibles[random.randint(0, len(positions_possibles))]
    return position


def cases_voisines(i, j, n):
    """
    Retourne une liste de tuples (ligne, colonne) représentant les positions des cases adjacentes (horizontalement, verticalement et en diagonale) à la case donnée.

    Données : i, de type int, est la ligne de la case, j, de type int, est la colonne de la case et n, de type n, est le nombre de lignes
    Résultat : cases, de type list, est une liste de tuples
    """
    cases = []
    if i - 1 >= 0:
        cases.append((i - 1, j))
    if i + 1 <= n - 1:
        cases.append((i + 1, j))
    if j - 1 >= 0:
        cases.append((i, j - 1))
    if j + 1 <= n - 1:
        cases.append((i, j + 1))
    if i - 1 >= 0 and j - 1 >= 0:
        cases.append((i - 1, j - 1))
    if i - 1 >= 0 and j + 1 <= n - 1:
        cases.append((i - 1, j + 1))
    if i + 1 <= n - 1 and j - 1 >= 0:
        cases.append((i + 1, j - 1))
    if i + 1 <= n - 1 and j + 1 <= n - 1:
        cases.append((i + 1, j + 1))
    return cases


def evolution(grille, affichage=False):
    """
    Simule l'évolution du feu à travers une grille. La grille est modifiée en place.

    Données : grille, de type list, est un tableau de tableaux
    Résultat : Simulation de la forêt
    """

    # Création de la case de départ
    depart_feu = choix_depart_feu(grille)
    grille[depart_feu[0]][depart_feu[1]] = 2

    propagation = [[depart_feu]]
    cases_par_tour = {}
    stockage_grilles = []
    
    tour = 0
    boucle = True
    while boucle:
        # Ajout de la grille du précédent tour
        stockage_grilles.append(deepcopy(grille))
        
        # Propagation
        cases_en_feu = []

        for ligne in range(len(grille)):
            for colonne in range(len(grille[ligne])):
                if grille[ligne][colonne] == 2:
                    propagation.append(cases_voisines(ligne, colonne, len(grille)))

        for cases_adj in propagation:
            for case in cases_adj:
                if grille[case[0]][case[1]] != 0:
                    grille[case[0]][case[1]] = 2
                    cases_en_feu.append(case)

        cases_par_tour[tour] = cases_en_feu

        if tour >= 1:
            for case in cases_par_tour[tour-1]:
                grille[case[0]][case[1]] = 3

        # Fin du programme quand la grille précédente est la même que celle actuellement
        if stockage_grilles[-1] == grille:
            boucle = False
        else:
            if affichage:
                affiche(grille)
        tour = tour + 1
        
    return stockage_grilles

##################### Programme principale ou tests ########################

if __name__ == '__main__':
    matrice = creation(10, 75) # Crée une grille de 10 cases de côté et avec une probabilité d'apparition d'arbres de 75%
    print(evolution(matrice,True)) # Affiche la simulation
