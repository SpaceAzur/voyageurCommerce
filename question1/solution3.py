#pour TSP
from mpmath import *
import numpy as np
import matplotlib as plt
from itertools import *
import tsp, sys, gc, time, heapq, csv
from fonctions_main import *
from fonctionsSolutionOptimale import *

##########################################
#### SOLUTION 3 : utilise les listes #####
##########################################


print("##################################################\n"
      "################## SOLUTION 3 ####################\n"
      "################################################## \n\n")


#demande choix liste user
choix_user = demande_choix_ville()

#selection chemin fichier csv
fichier_csv = selection_chemin_fichier_csv(choix_user)

#debut chrono
start_time = time.time()

#recuperation coordonnees villes
liste_villes = liste_coordonnees_villes_from_csv(fichier_csv)

#debut chrono
start_time = time.time()

#calcul distances entre villes
matrice_distances = matrice_distances(liste_villes)

chemin, distance = solutionOptimalTSP(matrice_distances)

chrono = (round((time.time() - start_time), 4))

print("\n\nLe chemin le plus court est  : ", chemin)

print("\nSa distance est de ", distance, "unités. ")

print("\nTemps d'exécution du programme : %s secondes " %chrono)