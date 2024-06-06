##########################################################################
#                                                                        #
#   Nom du programme : SimulationGraphiqueFeuDeForêt                     #
#                                                           ### #   ###  #
#   Date : 2022-2023                                         #  #    #   #
#   Auteur : Josselin LE TALLEC                            ###  ###  #   #
#                                                                        #
##########################################################################

##################### Importation des modules ou fonctions externes #######################

import tkinter as tk
import simulation
import time

##################### Définition des fontions locales ######################

def afficher_grille(grille, labels):
    """
    Fonction pour mettre à jour l'affichage de la grille en utilisant les valeurs de la grille donnée.

    Données : grille, de type list, est un la grille de valeurs à afficher et labels, de type list, est la liste stockant les cases et leur chiffre correspondant.
    Résultat : La liste des labels utilisés pour afficher la grille.
    """
    for i in range(len(grille)):
        for j in range(len(grille[i])):
            # Mettre à jour le texte du label pour afficher la nouvelle valeur de la cellule
            if grille[i][j] == 0:
                labels[i][j].configure(text=grille[i][j], bg="white", padx=20, pady=20, width=5, height=2)
            elif grille[i][j] == 1:
                labels[i][j].configure(text=grille[i][j], bg="green", padx=20, pady=20, width=5, height=2)
            elif grille[i][j] == 2:
                labels[i][j].configure(text=grille[i][j], bg="orange", padx=20, pady=20, width=5, height=2)
            elif grille[i][j] == 3:
                labels[i][j].configure(text=grille[i][j], bg="black", padx=20, pady=20, width=5, height=2)

def affichage(taille,pourcentage,temps):
    """
    Fonction pour afficher dans une fenêtre tkinter la simulation de feu de forêt

    Données : taille, de type int, est la taille de la grille, pourcentage, de type float, est la proportion d'arbres dans la grille, temps, de type float, est le temps que met la fenêtre à se mettre à jour
    Résultat : Fenêtre Tkinter
    """

    # Crée la fenêtre principale
    fenetre = tk.Tk()
    # On définie le titre de la fenêtre principale
    fenetre.title("Simulation de Feu de Forêt")
    # On définie la taille de la fenêtre
    fenetre.geometry("500x500")

    stockage_grilles = simulation.evolution(simulation.creation(taille,pourcentage))


    # Crée une liste pour stocker les labels (= Chiffre de la grille) pour chaque cellule de la grille
    labels = [[0]*len(stockage_grilles[0][0]) for i in range(len(stockage_grilles[0]))]

    for i in range(len(stockage_grilles[0])):
        fenetre.grid_rowconfigure(i, weight=1)
        for j in range(len(stockage_grilles[0][0])):
            # Créer un label pour afficher la valeur de la cellule
            labels[i][j] = tk.Label(fenetre, borderwidth=2, relief="solid")
            # Ajouter le label à la disposition de la grille
            labels[i][j].grid(row=i, column=j)
            fenetre.grid_columnconfigure(j, weight=1)

    for grille in stockage_grilles:
        # Mets à jour la grille affichée dans la fenêtre
        afficher_grille(grille, labels)
        fenetre.update()
        time.sleep(temps)

    # Garde la fenêtre ouverte
    fenetre.mainloop()

##################### Programme principale ou tests ########################

if __name__ == '__main__':
    # Affiche une simulation de feu de forêt dans une grille de 10 cases de côté, avec une probabilité d'appartition d'arbres de 55.5% et de 0.1 secondes de rafraîchissement
    affichage(13,55.5,0.1)