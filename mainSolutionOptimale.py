import csv
import numpy as np
from mpmath import *
from itertools import *
from fonctionsSolutionOptimale import *





#################################################################
##################  DEBUT DU PROGRAMME ##########################
#################################################################


############## IMPORTATION FICHIER CSV ##########################

# Importe le fichier.csv et le stock dans un tableau ville
# fichier par defaut pour l'instant = test10.csv
ville = []
with open('test10.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        for coord in row:
            coord = float(coord)
        ville.append(row)


# Supprime la 1ere ligne de la liste extraite (supprime le nombre de ligne)
del ville[0]
# Sauvegarde la taille de la liste extraite du fichier
# sommet = integer
nbVille = len(ville)


parcours = []
parcours.append(0)

sauve = ville


print("Nombre de ville :", len(ville))
print("Liste des distances entre 1ere ville et chaque ville :\n", listeDistance(ville))
print("Numero de ville la plus proche de la 1ere ville :", numVillePlusProche(ville))

zaza = numVillePlusProche(ville)
print(ville[zaza])

chem = list(permutations(ville[1:]))
cheminPossible= []
for p in chem:
    if p[0] < p[1]:
        cheminPossible.append(p)



print("lenght de chemin2 ", len(cheminPossible))

print("permutation ", len(list(permutations(ville[1:]))))





print(calculDistanceChemin(cheminPossible[2]))

