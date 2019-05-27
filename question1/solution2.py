###########################################
#### SOLUTION 2 : utilise une matrice #####
###########################################

from fonctionsSolutionOptimale import *
from itertools import permutations
import time
import numpy as np


liste = [0,1,2,3,4,5,6,7,8,9]
listeSansMiroir = []
listeChemins = []

listeVilles = listeCoordonneesVillesFromCSV('../data/test10.csv')

start_time = time.time()

#permutations
listePermutations = list(permutations(liste))

#retrait miroirs
for chemin in listePermutations :
    if (chemin[0] < chemin[1]):
        listeSansMiroir.append(chemin)

#retrait non ville depart 0

i = 0
for chemin in listeSansMiroir :
    if chemin[0] == 0 :
        listeChemins.append(chemin)


#ajout ville retour
i = 0
for chemin in listeChemins :
    listeChemins[i] = listeChemins[i] + (0,)

    i = i + 1

print("listes chemins - %s seconds ---" % (time.time() - start_time))


start_time = time.time()

matriceDistances = matriceDistance(listeVilles)

print("generation matrice %s seconds ---" % (time.time() - start_time))


start_time = time.time()

distanceChemin = 0
listeDistances = []

k = 0

for chemin in listeChemins :

    #print(chemin)

    i = 0
    j = 1

    distanceTMP = 0
    distanceChemin = 0

    while j < len(chemin) :

        distanceTMP = matriceDistances[ listeChemins[k][i] ] [ listeChemins[k][j] ]
        #print("distance tmp = ", distanceTMP)

        distanceChemin = distanceChemin + distanceTMP
        #print("distance chemin : ", distanceChemin)

        #print("")
        i = i + 1
        j = j + 1

    #print("distance chemin : ", distanceChemin)
    listeDistances.append(distanceChemin)

    k = k + 1

#print(len(listeDistances))

listeDistances.sort()

print(listeDistances[0])

print("algo chemin  %s seconds ---" % (time.time() - start_time))