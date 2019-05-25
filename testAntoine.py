import heapq
from mpmath import *
import csv
import numpy as np
import matplotlib as plt
from itertools import *


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

print("Nombre de ville :", len(ville),"\n")
print("Liste des distances entre 1ere ville et chaque ville :\n", listeDistance(ville),"\n")
print("Numero de ville la plus proche de la 1ere ville :", numVillePlusProche(ville),"\n")


# Liste toutes les permutations possibles de chemins
# Divise la liste en 2 car nous excluons les doublons mirroirs
def listeCheminsPossible(villes):
    chem = list(permutations(ville[1:]))
    cheminPossible= []
    for p in chem:
        if p[0] < p[1]:
            cheminPossible.append(p)
    return cheminPossible

print("Nb de permutation total ", len(list(permutations(ville[1:]))),"\n")
print("Nb de chemin possible", len(listeCheminsPossible(ville)),"\n")

def calculDistanceChemin (listeChemin) :
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
    return distanceTotal

cheminN2 = listeCheminsPossible(ville)
cheminN2 = list(cheminN2)

# Liste les distances de toutes les permutations
listeTouteDistance = []
for c in cheminN2:
    zaza = calculDistanceChemin(c)
    listeTouteDistance.append(zaza)

print("Nombre de distance calculées ", len(listeTouteDistance),"\n")

zozo = min(listeTouteDistance)
zazaMin = listeTouteDistance.index(min(listeTouteDistance))
print("indice du chemin le plus court", zazaMin,"\n")
print("Distance la plus courte ", zozo,"\n")
print("chemin le plus court ", cheminN2[zazaMin],"\n")