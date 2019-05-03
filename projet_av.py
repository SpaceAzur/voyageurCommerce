
from mpmath import *
import csv
import scipy
import numpy as np


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

# Sauvegarde la taille de la liste extraite du fichier
# sommet = integer
sommet = len(ville) - 1
# Supprime la 1ere ligne de la liste extraite (supprime le nombre de ligne)
del ville[0]


# FONCTION : 
# ensures : Calcul la distance euclidienne entre deux villes
# input   : ville de depart et ville d'arrivée, en tuple(x,y)
# return  : float | distance
def distance(depart, arrivee):
    dist = (float(depart[0])-float(arrivee[0]))**2 + (float(depart[1])-float(arrivee[1]))**2
    dist = sqrt(dist)
    return dist


# FONCTION
# ensures : Calcule la distance de chaque chemin possible depuis la 1ere ville
# input   : liste des villes
# return  : float | liste de distances
def listeDistance(ville):
    parcours = []
    for vertice in ville:
        teste = distance(ville[0],vertice)
        if(teste != 0.0):
            parcours.append(teste)
    return parcours

# FONCTION  
# ensures ; Trouve la ville la plus proches de la 1ere ville
# input   : liste des villes
# return  : integer | indice de la ville la plus proche dans la liste "ville"
def numVillePlusProche(ville):
    dist = []
    ville = np.array(ville)
    for (indice, sommet) in enumerate(ville):
        toto = distance(ville[0],sommet)
        if(toto != 0.0):
            dist.append(toto)
    solu = dist.index(min(dist)) + 1
    return solu

print(ville)
print(listeDistance(ville))
print(numVillePlusProche(ville))

