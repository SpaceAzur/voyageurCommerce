from mpmath import *
import numpy as np
import matplotlib as plt
from itertools import *
import tsp, sys, gc, time, heapq, csv
from fonctions_main import *
from fonctionsSolutionOptimale import *

print("##################################################\n"
      "################## SOLUTION 1 ####################\n"
      "###### Algorithme du plus court chemin ########### \n\n")

#demande choix liste user
choix_user = demande_choix_ville()

#selection chemin fichier csv
fichier_csv = selection_chemin_fichier_csv(choix_user)

#debut chrono
print("\nDépart du chrono ! ")
start_time = time.time()

#recuperation coordonnees villes
liste_villes = liste_coordonnees_villes_from_csv(fichier_csv)

#calcul distances entre villes
matrice_distances = matrice_distances(liste_villes)


visited = [0.0]
indiceVisites= []
distanceTotale = []
chemin, distance = recursiveChemin(matrice_distances, visited, indiceVisites, 0, distanceTotale)

chrono = (round((time.time() - start_time), 4))

chemin.insert(0,0)

print("\nLe chemin le plus court est  : ", convertion_chemin_liste_pour_user(chemin))

print("Sa distance est de :", round((distance), 4))

print("\nTemps d'exécution du programme : %s secondes " %chrono)



#Affichage chemin

#converti ces coordonnees en float (besoin graphique)
coordonnees_float = convertion_liste_coordonnees_str_liste_coordonnes_float(liste_villes)

#affichage ville + parcours
dessiner_parcours_voyageur_commerce(coordonnees_float, convertion_chemin_liste_pour_user(chemin))