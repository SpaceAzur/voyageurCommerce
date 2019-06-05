from mpmath import *
import numpy as np
import matplotlib as plt
from itertools import *
import tsp, sys, gc, time, heapq, csv
from fonctions_main import *
from fonctionsSolutionOptimale import *

print("##################################################\n"
      "################## SOLUTION 1 ####################\n"
      "################################################## \n\n")

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

print("\n Algorithme glouton 'le plus proche voisin' : ", chemin)

print("Sa distance est de :", distance)

print("\nTemps d'exécution du programme : %s secondes " %chrono)