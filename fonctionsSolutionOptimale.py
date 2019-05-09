import csv
import numpy as np
from mpmath import *
from itertools import *
from fonctionsSolutionOptimale import *


#FONCTION
# ensures : Ouvre le fichier CSV est exploite ses données
# param   : fichier CSV
# return dans l'ordre  : liste des villes (tuples) | Nombre de villes
def exploitationFichierCSV (fichiercsv) :
    listeTuplesVille = []
    with open(fichiercsv) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            for coord in row:
                coord = float(coord)

            #liste des villes (tuples x,y)
            listeTuplesVille.append(row)

    #nombre de villes
    nbVille = listeTuplesVille[0]
    #suppression ligne du nombre de villes
    del listeTuplesVille[0]

    #renvoi ville et nbVille
    return listeTuplesVille, nbVille



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
# ensures : creer une liste de tous les chemins possibles, sans mirroir, avec la ville de depart en debut et fin de chaque chemin
# param   : liste des villes fichier csv
# return  : type liste de liste 
def listeCompleteChemin(ville):
    chem = list(permutations(ville[1:]))
    cheminPossible= []
    for p in chem:
        if p[0] < p[1]:
            cheminPossible.append(p)

    cheminPossible = list(cheminPossible)

    for i, chemin in enumerate(cheminPossible):
        chemin = list(chemin)
        chemin.insert(0, ville[0])
        chemin.append(ville[0])

    return cheminPossible


# FONCTION
# ensures ; Trouve la ville la plus proche de la 1ere ville
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


#FONCTION
#Calcul la distance totale d'un chemin donné
def calculDistanceTotaleChemin (Chemin) :
    i = 0 ;
    j = 1 ;
    chemin = 0 ;
    ville = 0 ;
    distancetemp = 0;
    distanceTotale = 0;


    while j < (len(Chemin)):
        #calcul distance temporaire
        distancetemp = distance(Chemin[i], Chemin[j])
        #calcul distance totale
        distanceTotale = distanceTotale + distancetemp
        i = i + 1;
        j = j + 1;

    return distanceTotale