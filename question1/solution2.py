###########################################
#### SOLUTION 2 : utilise une matrice #####
###########################################

from fonctionsSolutionOptimale import *
from itertools import permutations
import time
import numpy as np


#debut chrono
start_time = time.time()

#recupertion coordonnees villes
liste_villes = liste_coordonnees_villes_from_csv('../data/test10.csv')

#recuperation nombre villes
nombre_villes = len(liste_villes)

#generation chemins hamiltoniens possibles
liste_chemins_possibles = liste_chemins_possibles_numeros_villes(nombre_villes)

#calcul distances entre villes
matrice_distances = matrice_distances(liste_villes)

#calcul plus court chemin | villes parcours
parcours, distance = calcul_distance_chemin_plus_court_numeros_villes(liste_chemins_possibles, matrice_distances)

print("\n\nparcours : ", parcours)
print("distance : ", distance)

print("\n timer programme  %s seconds ---" % (time.time() - start_time))