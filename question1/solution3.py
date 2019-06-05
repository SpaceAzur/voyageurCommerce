#pour TSP
from fonctionsSolutionOptimale import *
from itertools import permutations
import time, tsp 
import numpy as np

#debut chrono
start_time = time.time()

#recupertion coordonnees villes
liste_villes = liste_coordonnees_villes_from_csv('../data/test10.csv')

#recuperation nombre villes
nombre_villes = len(liste_villes)

#calcul distances entre villes
matrice_distances = matrice_distances(liste_villes)

parcours, distance = solutionOptimalTSP(matrice_distances)

print("\n\nparcours : ", parcours)
print("distance : ", distance)

print("\n timer programme  %s seconds ---" % (time.time() - start_time))