import csv
from mpmath import *
from itertools import *
from fonctionsSolutionOptimale import *


#FONCTION
# ensures : creation de la liste de toutes les villes à visiter
# param   : fichier CSV
# return dans l'ordre  : liste des villes (tuples X Y)

def listeCoordonneesVillesFromCSV (fichierCSV) :
    #initialisation liste coordonnees villes
    listeCoordonneesVilles = []

    #initialiation du lecteur csv
    with open(fichierCSV) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        #pour chaque ligne du fichier csv
        for row in csv_reader:
            for coord in row:
                coord = float(coord)

            #ajout des coordonnnees de chaque ville a la liste (tuples x, y)
            listeCoordonneesVilles.append(row)

    #suppression de la ligne qui indique le nombre de villes
    del listeCoordonneesVilles[0]

    #renvoi liste coordonnees villes
    return listeCoordonneesVilles



# FONCTION :
# ensures : Calcul la distance euclidienne entre deux villes
# param   : ville de depart et ville d'arrivee, en tuple(x,y)
# return  : float | distance
def distanceEntre2Villes(depart, arrivee):
    distance = (float(depart[0])-float(arrivee[0]))**2 + (float(depart[1])-float(arrivee[1]))**2
    distance = sqrt(distance)

    #renvoi distance entre 2 villes
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
# return  : liste chemins possibles SANS miroir avec ville 0 comme ville depart
def listeCheminsPossibles (listeVilles) :
    #liste chemins sans filtre
    cheminsSansFiltre = list(permutations(listeVilles))

    #initialisation liste chemins possibles temporaire
    cheminsPossiblesTMP = []

    # initialisation liste chemins possibles finale
    cheminsPossibles = []

    #retrait des miroirs de la liste temporaire
    for chemin in cheminsSansFiltre :
        if chemin[0] < chemin[1]:
            cheminsPossiblesTMP.append(chemin)

    #retrait des chemins qui ne commencent pas par la ville choisie comme ville de depart
    for chemin in cheminsPossiblesTMP :
        #si la ville de depart est la ville voulue
        if chemin[0] == ['2.00', '36.05'] :
            cheminsPossibles.append(chemin)


    #compteur iteration chemin
    i = 0
    #pour chaque chemin de tous les chemins possibles
    for chemin in cheminsPossibles :
        #ajout de la ville de depart comme ville de retour a la fin de la liste
        cheminsPossibles[i] = cheminsPossibles[i] + (['2.00', '36.05'],)
        #on passe au chemin suivant
        i = i + 1

    #renvoi la liste de tous les chemins possibles
    return cheminsPossibles


#FONCTION
#ensures : calcul les distances de tous les chemins
#param : liste de tous les chemins possibles
#return : liste des distances de tous les chemins
def calculDistancesCheminsPossible (listeCheminsPossibles) :
    #initialisatin liste distances chemins possibles
    listeDistancesCheminsPossibles = []

    #pour chaque chemin de la liste des chemins possibles
    for chemin in listeCheminsPossibles :

        #calcul distance du chemin
        distance = calculDistanceUnChemin(chemin)

        #ajout distance au tableau des distances
        listeDistancesCheminsPossibles.append(distance)

    return listeDistancesCheminsPossibles



# FONCTION
# ensures : Trouve la ville la plus proche de la 1ere ville
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
def calculDistanceUnChemin (Chemin) :
    i = 0 ;
    j = 1 ;
    chemin = 0 ;
    ville = 0 ;
    distancetemp = 0;
    distanceUnChemin = 0;


    while j < (len(Chemin)):
        #calcul distance temporaire
        distancetemp = distanceEntre2Villes(Chemin[i], Chemin[j])
        #calcul distance totale
        distanceUnChemin = distanceUnChemin + distancetemp
        i = i + 1;
        j = j + 1;

    return distanceUnChemin