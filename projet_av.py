from mpmath import *
import csv
import scipy
import numpy


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
# return  : distance en float
def distance(depart, arrivee):
    dist = (float(depart[0])-float(arrivee[0]))**2 + (float(depart[1])-float(arrivee[1]))**2
    dist = sqrt(dist)
    return dist

parcours = []
for vertice in ville:
    teste = distance(ville[0],vertice)
    parcours.append(teste)

print(parcours)