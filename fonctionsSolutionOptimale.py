import csv
import numpy as np
from mpmath import *
from itertools import *
from fonctionsSolutionOptimale import *


#FONCTION
# ensures : creation de la liste de toutes les villes à visiter
# param   : fichier CSV
# return dans l'ordre  : liste des villes (tuples X Y)
def listeCoordonneesVillesFromCSV (fichierCSV) :

    listeCoordonneesVilles = []
    with open(fichierCSV) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            for coord in row:
                coord = float(coord)

            #liste des villes (tuples x,y)
            listeCoordonneesVilles.append(row)

    #suppression de la ligne du nombre de villes
    del listeCoordonneesVilles[0]

    #renvoi ville
    return listeCoordonneesVilles



# FONCTION :
# ensures : Calcul la distance euclidienne entre deux villes
# param   : ville de depart et ville d'arrivee, en tuple(x,y)
# return  : float | distance
def distanceEntre2Villes(depart, arrivee):
    distance = (float(depart[0])-float(arrivee[0]))**2 + (float(depart[1])-float(arrivee[1]))**2
    distance = sqrt(distance)
    return distance


# FONCTION
# ensures : Calcule la distance de chaque chemin possible depuis la 1ere ville
# param   : liste des villes
# return  : float | liste de distances
def listeDistanceVilleDepartChaqueVille(listeVilles):
    listeDesDistances = []
    for vertice in listeVilles:
        teste = distanceEntre2Villes(listeVilles[0],vertice)
        if(teste != 0.0):
            listeDesDistances.append(teste)
    return listeDesDistances


#FONCTION
# ensures : Création de la liste de tous les chemins possibles
# param   : liste des villes (tuples) créées par la fonction correspondante
# return dans l'ordre  : liste de tous les chemins possibles SANS miroir | nombre de chemins possibles
def listeCheminsPossibles (ville) :
    chemins = list(permutations(ville[1:]))
    cheminsPossibles = []
    for p in chemins :
        if p[0] < p[1]:
            cheminsPossibles.append(p)


    return cheminsPossibles



# FONCTION
# ensures ; Trouve la ville la plus proche de la 1ere ville
# param   : liste des villes
# return  : integer | indice de la ville la plus proche dans la liste "ville"
def numeroVillePlusProcheVilleDepart(ville):
    listeDesDistance = []
    ville = np.array(ville)
    for (indice, sommet) in enumerate(ville):
        calculDistance = distanceEntre2Villes(ville[0],sommet)
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
        distancetemp = distanceEntre2Villes(Chemin[i], Chemin[j])
        #calcul distance totale
        distanceTotale = distanceTotale + distancetemp
        i = i + 1;
        j = j + 1;

    return distanceTotale