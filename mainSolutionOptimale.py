import csv
import numpy as np
from mpmath import *
from itertools import *
from fonctionsSolutionOptimale import *




#################################################################
##################  DEBUT DU PROGRAMME ##########################
#################################################################

#mesage accueil


import time
from functools import wraps


from fonctionsSolutionOptimale import *

start_time = time.time()

listeVilles = listeCoordonneesVillesFromCSV('data/test10.csv')
print("")
listeChemins = listeCheminsPossibles(listeVilles)
print("")
tableauDistances = calculDistancesCheminsPossibles(listeChemins)
print("")
cheminOptimal, distanceCheminOptimal = cheminOptimal(tableauDistances, listeChemins, listeVilles)
print("")

print("chemin optimal :", cheminOptimal)
print("")
print("distance chemin optimal :", distanceCheminOptimal)
print("")
print("--- %s seconds ---" % (time.time() - start_time))