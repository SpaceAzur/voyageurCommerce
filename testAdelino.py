import time
from functools import wraps
from fonctionsSolutionOptimale import *



listeVillesRestantes = liste_coordonnees_villes_from_csv('data/test10.csv')

@timer_fonction
def calcul_distance_ville_depart_ville_plus_proche (villeDepart, villesRestantes) :

    #compteurs
    i = 0
    j = 1

    #liste des distances
    listeDistances = []

    #iteration
    while j < len(villesRestantes) :

        #calcul de la distance entre ville depart toutes les villes restantes
        distanceEntre2villes = calcul_distance_entre_2_villes(villesRestantes[i], villesRestantes[j])

        #ajout de la distance a la liste des distances
        listeDistances.append(distanceEntre2villes)

        #on passe a la ville suivante
        j = j + 1

    #tri des distances par ordre croissant
    listeDistances.sort()

    #distance la plus courte = distance en indice 0
    dpc = listeDistances[0]

    return listeDistances



print(calcul_distance_ville_depart_ville_plus_proche(listeVillesRestantes[0], listeVillesRestantes))

