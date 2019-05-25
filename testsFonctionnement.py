import csv
import numpy as np
from mpmath import *
from itertools import *
from fonctionsSolutionOptimale import *



#Ouvre le fichier CSV et attribue ses 2 RETURNS aux variables "ville" et "nbVille"
villes = listeCoordonneesVillesFromCSV('test10.csv')



####### CREATION DE LA LISTE DE TOUS LES CHEMINS POSSIBLES et de leur nombre ########
cheminsPossibles = listeCheminsPossibles(villes)



############### TESTS DE FONCTIONNEMENT ##############################

print("Nombre de ville :", len(villes))

print("Liste des distances entre 1ere ville et chaque ville :\n", listeDistanceVilleDepartChaqueVille(villes))

print("Numero de ville la plus proche de la 1ere ville :", numeroVillePlusProcheVilleDepart(villes))

print("Nombre des vrais chemins possibles ", len(cheminsPossibles))

print("Nombre total des chemins avec chemins miroir ", len(list(permutations(villes[1:]))))

print("Distance Totale du chemin [2]", calculDistanceTotaleChemin(cheminsPossibles[2]))


