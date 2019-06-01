import heapq
from mpmath import *
import csv
import numpy as np
import matplotlib as plt
from itertools import *
import tsp
import sys
import gc
import time

def timer_fonction(f):
    def wrap(*args):
        time1 = time.time()
        ret = f(*args)
        time2 = time.time()
        print('{:s} function took {:.3f} ms'.format(f.__name__, (time2-time1)*1000.0))

        return ret
    return wrap

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

# FONCTION :
# ensures : Calcul la distance euclidienne entre deux villes
# param   : ville de depart et ville d'arrivee, en tuple(x,y)
# return  : float | distance
def distance(depart, arrivee):
    dist = (float(depart[0])-float(arrivee[0]))**2 + (float(depart[1])-float(arrivee[1]))**2
    dist = sqrt(dist)
    return dist

# FONCTION
# ensures : Calcule la distance de chaque chemin possible depuis la 1ere ville
# param   : liste des villes
# return  : float | liste de distances
def listeDistance(ville):
    listeDesDistances = []
    for vertice in ville:
        teste = distance(ville[0],vertice)
        if(teste != 0.0):
            listeDesDistances.append(teste)
    return listeDesDistances

# FONCTION
# ensures ; Trouve la ville la plus proches de la 1ere ville
# param   : liste des villes
# return  : integer | indice de la ville la plus proche dans la liste "ville"
def numVillePlusProche(ville):
    listeDesDistance = []
    ville = np.array(ville)
    for (indice, sommet) in enumerate(ville):
        calculDistance = distance(ville[0],sommet)
        if(calculDistance != 0.0):
            listeDesDistance.append(calculDistance)
    indiceVillePlusProche = listeDesDistance.index(min(listeDesDistance)) + 1
    return indiceVillePlusProche

parcours = []
parcours.append(0)

sauve = ville
print("\nNombre de ville :", len(ville),"\n")

# Liste toutes les permutations possibles de chemins
# Divise la liste en 2 car nous excluons les doublons mirroirs
def listeCheminsPossible(villes):

    chem = list(permutations(ville[1:]))
    cheminPossible= []
    for p in chem:
        if p[0] < p[1]:
            cheminPossible.append(p)

    return cheminPossible

# print("Nb de chemin possible", len(listeCheminsPossible(ville)),"\n")

# Calcul la distance total d un chemin
def calculDistanceChemin (listeChemin) :
    global sauve
    i = 0 ;
    j = 1 ;
    chemin = 0 ;
    ville = 0 ;
    distancetemp = 0;
    distanceTotal = 0;
    while j < (len(listeChemin)):
        #calcul distance temporaire
        distancetemp = distance(listeChemin[i], listeChemin[j])
        #calcul distance totale
        distanceTotal = distanceTotal + distancetemp
        i = i + 1;
        j = j + 1;
    #On ajoute la distance entre la derniere ville et la ville de depart
    # + distance(sauve[0],listeChemin[i]) 
    return distanceTotal

# timeTest = 1000.0
# for c in tousChemins:
#     tmp = calculDistanceChemin(c)
#     if tmp > timeTest:
#         tmp = timeTest
#     else:
#         timeTest = tmp

#--------------------------------------------------------------------------------------------
# FONCTION
# ensures : calcul la distance entre 2 villes, arrondi a 2 decimal
# returns : distance (float 2 decimals)
def distance2(depart, arrivee):
    dist = (float(depart[0])-float(arrivee[0]))**2 + (float(depart[1])-float(arrivee[1]))**2
    dist = sqrt(dist)
    dist = round(dist,2)
    return dist

#FONCTION
# ensures : Calcul la matrice des distances entre chaque ville
# returns : matricde de distance
def matriceDistance(listeVille):

    # Conversion de la liste des villes en tableau
    x = np.array(listeVille)

    # initialisation de la matrice de distance
    matDist = np.zeros((len(x),len(x)))

    # Calcul des distances entre chaque ville
    for i, lig in enumerate(matDist):
        for j, col in enumerate(lig):
            matDist[i][j] = distance2(listeVille[i],listeVille[j])

    return matDist

#FONCTION
# ensures : Calcul la chemin optimal
# returns : (tuple) distance du chemin optimal , chemin optimal
def solutionOptimalTSP(matriceDistance):

    r = range(len(matriceDistance))
    dist = {(i, j): matriceDistance[i][j] for i in r for j in r}
    solution = tsp.tsp(r,dist)

    return solution


DistanceMatrix = matriceDistance(sauve)

# FONCTION
# ensures : détermine la valeur minimum d'une liste, en exluant les valeurs présente d'une autre liste
# returns : (float) valeur minimum 
def min_gt(seq, visited):
    return min(v for v in seq if v not in visited)

#Rajout de la ville de depart en fin de liste

print("matrice de distance \n", DistanceMatrix)
visit = [0]
indVisit = []
maDistance = []
for i, lig in enumerate(DistanceMatrix):
    for j, col in enumerate(lig):
        #simuler nouvelle liste "visit" de la ligne i
        # for k, node in enumerate(zozo[i]):
        if j in indVisit:
            visit.append(DistanceMatrix[i][j]) 
        #je cherche la valeur min , excluant les valeurs présentent dans visit[]
        t = min_gt(lig,visit)
        #je caste ma ligne en liste
        gg = list(DistanceMatrix[i])
        #je recupere l'index de ma valeur min
        ggg= gg.index(t)
    #je sauvegarde ma distance pour calculer le total plus tard
    maDistance.append(t)
    #je sauvegarde l'index = mon chemin
    indVisit.append(ggg)
    #je garde la valeur i-1 que j'ai visite pour mon comparatif suivant
    visit.append(t)
    #je supprime la valeur que j'ai trouve lors de ma visite en i-2
    del visit[2:]

print("Distance Total ",round(sum(maDistance),2))

# FONCTION RECURSIVE PLUS COURT CHEMIN 
@timer_fonction
def recursiveChemin(matriceDeDistance, visited, indiceVisites, indiceEnCours, compteurDistance):

    villa = list(matriceDeDistance[indiceEnCours])

    for k, ville in enumerate(villa):
    # for k, ville in enumerate(matriceDeDistance[indiceEnCours]):
        if k in indiceVisites:
            visited.append(ville)
    # je recupere la distance minimum hors visited
    mini = min_gt(villa,visited)
    # je recupere l'indice de la valeur minimum = prochaine ville
    inda = villa.index(mini)
    # je sauvegarde la valeur minimum dans visited pour ne pas boucler dessus
    visited.append(mini)
    # je cumule la distance
    compteurDistance.append(mini)
    # je sauvegarde la ville comme parcourue
    indiceVisites.append(inda)
    print("\nvilla ",indiceEnCours, " ", villa)
    print("mini ", mini, "indiceMin ", inda)
    print("visited ", visited)
    print("indiceVisites ", indiceVisites)
    print("distanceCumul ", compteurDistance)
    del visited[2:]
    # print("visited2 ", visited)
    while len(indiceVisites) != len(matriceDeDistance):
        recursiveChemin(matriceDeDistance, visited, indiceVisites, inda, compteurDistance)
    
    return indiceVisites, sum(compteurDistance)

visited = [0.0]
indiceVisites= []
distanceTotale = []
Recu = recursiveChemin(DistanceMatrix, visited, indiceVisites, 0, distanceTotale)
print("recursive ", Recu)

testa = distance2(ville[2],ville[9])
print(testa)
testo = distance2(ville[7],ville[9])
print(testo)