import heapq
from mpmath import *
import csv
import numpy as np
import matplotlib as plt
from itertools import *
import tsp


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

# GENERATION DE TOUS LES CHEMINS POSSIBLES
# allPath = listeCheminsPossible(ville)
# allPath = list(allPath) 
# tousChemins = []
# for y in allPath:
#     y = list(y)
#     y.insert(0,sauve[0])
#     y.append(sauve[0])
#     tousChemins.append(y)

#Liste les distances de toutes les permutations de chemin
# listeTouteDistance = []
# for c in tousChemins:
#     tempo = calculDistanceChemin(c)
#     listeTouteDistance.append(tempo)

# timeTest = 1000.0
# for c in tousChemins:
#     tmp = calculDistanceChemin(c)
#     if tmp > timeTest:
#         tmp = timeTest
#     else:
#         timeTest = tmp
# print('tmp = ', tmp)
# print("timeTest = ", timeTest)

# print("Nombre de distance calculées ", len(listeTouteDistance),"\n")

# distMin = min(listeTouteDistance)
# indiceDistMin = listeTouteDistance.index(min(listeTouteDistance))
# print("indice du chemin le plus court", indiceDistMin,"\n")
# print("Distance la plus courte ", distMin,"\n")
# print("chemin le plus court\n ", tousChemins[indiceDistMin],"\n")




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


zozo = matriceDistance(sauve)

# FONCTION
# ensures : détermine la valeur minimum d'une liste, en exluant les valeurs présente d'une autre liste
# returns : (float) valeur minimum 
def min_gt(seq, visited):
    return min(v for v in seq if v not in visited)

#Rajout de la ville de depart en fin de liste

print("matrice de distance \n", zozo)
visit = [0,0]
indVisit = []
maDistance = []
for i, lig in enumerate(zozo):
    for j, col in enumerate(lig):
        #je cherche la valeur min , excluant les valeurs présentent dans visit[]
        t = min_gt(lig,visit)
        #je caste ma ligne en liste
        gg = list(zozo[i])
        #je recupere l'index de ma valeur min
        ggg= gg.index(t)
    #je sauvegarde ma distance pour calculer le total plus tard
    maDistance.append(t)
    #je sauvegarde l'index = mon chemin
    indVisit.append(ggg)
    #je garde la valeur i-1 pour mon comparatif suivant
    visit.append(t)
    #je supprime la valeur i-2
    del visit[1]


print("indVisit ", indVisit)
print("visit ", visit)
print("Distance Total ",round(sum(maDistance),2))
# reste a faire
# RAJOUTER UNE DERNIERE CONDITION pour la chemin soit hamiltonien
# creer une 2ème liste "visited2" qui contiendra les indices des sommets deja visites
# prendre en compte cette liste visited2 => 

# TO DO
# 

