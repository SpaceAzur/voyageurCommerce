import csv
import numpy as np
from mpmath import *
from itertools import *
from fonctionsSolutionOptimale import *





#################################################################
##################  DEBUT DU PROGRAMME ##########################
#################################################################


############## EXPLOITATION DU FICHIER CSV ##########################

#Ouvre le fichier CSV et attribue ses 2 RETURNS aux variables "ville" et "nbVille"
ville, nbVille = exploitationFichierCSV('test10.csv')



parcours = []
parcours.append(0)

sauve = ville

print("Nombre de ville :", len(ville))
print("Liste des distances entre 1ere ville et chaque ville :\n", listeDistance(ville))
print("Numero de ville la plus proche de la 1ere ville :", numVillePlusProche(ville))


## ToDo A supprimer ?
zaza = numVillePlusProche(ville)
print(ville[zaza])

## ToDo A supprimer ?
chem = list(permutations(ville[1:]))
cheminPossible= []
for p in chem:
    if p[0] < p[1]:
        cheminPossible.append(p)


############### TESTS DE FONCTIONNEMENT ##############################

print("Nombre des vrais chemins possibles ", len(cheminPossible))

print("Nombre total des chemins avec chemins miroir ", len(list(permutations(ville[1:]))))

print("Distance Totale du chemin [2]", calculDistanceTotaleChemin(cheminPossible[2]))

