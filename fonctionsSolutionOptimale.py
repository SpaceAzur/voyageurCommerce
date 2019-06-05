import csv #pour traiter les fichiers csv
import math #pour les calculs mathematiques
import numpy as np #pour les matrices
import time #pour les timers
import re #pour les expresions regulieres
from functools import wraps #pour monitorer les fonctions
from itertools import permutations #pour generer les permutations
import matplotlib.pyplot as plt #pour afficher les villes et le parcours (graphique)
import tsp


#FONCTION
#ENSURES : calcul le temps d'execution d'une fonction
#USAGE : ajouter @timing devant la fonction
#param : none
#RETURN : duree execution fonction
def timer_fonction(f):
    def wrap(*args):
        time1 = time.time()
        ret = f(*args)
        time2 = time.time()
        print('{:s} Temps d\'exécution de la fonction :  {:.3f} millisecondes'.format(f.__name__, (time2-time1)*1000.0))

        return ret
    return wrap


#FONCTION
# ensures : creation de la liste de toutes les villes à visiter
# param   : fichier CSV
# return dans l'ordre  : liste des villes (tuples X Y)
@timer_fonction
def liste_coordonnees_villes_from_csv (fichierCSV) :
    #initialisation liste coordonnees villes
    liste_coordonnees_villes_from_csv = []

    #initialiation du lecteur csv
    with open(fichierCSV) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        #pour chaque ligne du fichier csv
        for row in csv_reader:

            #ajout des coordonnnees de chaque ville a la liste (tuples x, y)
            liste_coordonnees_villes_from_csv.append(row)

    #suppression de la ligne qui indique le nombre de villes
    del liste_coordonnees_villes_from_csv[0]

    #renvoi liste coordonnees villes
    return liste_coordonnees_villes_from_csv


#FONCTION
#ENSURES : converti une liste de coordonnes de type str en liste de type float
#PARAM: liste de coordonnees de villes au format str
#RETURN : liste de coordonnees de villes au format float
def convertion_liste_coordonnees_str_liste_coordonnes_float (liste_coordonees_str) :

    #liste qui va recevoir les coordonnees des villes converties en type float
    liste_coordonnes_villes_float = [[] * nombre for nombre in range(0, len(liste_coordonees_str))]

    #sert a parcourir les indices
    i = 0
    #pour chaque coordonnee x et y de type str
    for coordonnee_ville_str in liste_coordonees_str :
        #converstion x str en x float et ajour a la liste
        liste_coordonnes_villes_float[i].append(float(coordonnee_ville_str[0]))
        # converstion y str en y float et ajour a la liste
        liste_coordonnes_villes_float[i].append(float(coordonnee_ville_str[1]))
        #indice suivant
        i = i + 1

    #renvoie la liste des coordonnees des villes de type floar
    return liste_coordonnes_villes_float

#FONCTION
#ENSURES : converti une liste de coordonnes de type str en liste de type float
#PARAM: liste de coordonnees de villes au format str
#RETURN : liste de coordonnees de villes au format float
def convertion_liste_coordonnees_str_liste_coordonnes_float (liste_coordonees_str) :

    #liste qui va recevoir les coordonnees des villes converties en type float
    liste_coordonnes_villes_float = [[] * nombre for nombre in range(0, len(liste_coordonees_str))]

    #sert a parcourir les indices
    i = 0
    #pour chaque coordonnee x et y de type str
    for coordonnee_ville_str in liste_coordonees_str :
        #converstion x str en x float et ajour a la liste
        liste_coordonnes_villes_float[i].append(float(coordonnee_ville_str[0]))
        # converstion y str en y float et ajour a la liste
        liste_coordonnes_villes_float[i].append(float(coordonnee_ville_str[1]))
        #indice suivant
        i = i + 1

    #renvoie la liste des coordonnees des villes de type floar
    return liste_coordonnes_villes_float



# FONCTION :
# ensures : Calcul la distance euclidienne entre deux villes
# param   : ville de depart et ville d'arrivee, en tuple(x,y)
# return  : float | distance
def calcul_distance_entre_2_villes(depart, arrivee):
    #premiere partie : calcul sous la racine
    distance = (float(depart[0])-float(arrivee[0]))**2 + (float(depart[1])-float(arrivee[1]))**2
    #deuxieme partie : racine du resultat obtenu precedemment
    distance = math.sqrt(distance)

    #renvoi distance euclidiennte entre 2 villes
    return distance



#FONCTION
# ensures : Création de la liste de tous les chemins possibles sous forme de liste de coordonnees
# param   : liste des villes (tuples) créées par la fonction correspondante
# return  : liste chemins possibles SANS miroir avec ville 0 comme ville depart
@timer_fonction
def liste_chemins_possibles(listeVilles) :
    #liste chemins sans filtre
    cheminsSansFiltre = list(permutations(listeVilles))

    #initialisation liste chemins possibles temporaire
    cheminsPossiblesTMP = []

    # initialisation liste chemins possibles finale
    cheminsPossibles = []

    #retrait des miroirs de la liste temporaire
    for chemin in cheminsSansFiltre :
        if (chemin[0] < chemin[1]):
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

    #renvoi la liste de tous les chemins possibles avec coorodonnes villes
    return cheminsPossibles


# FONCTION
# ENSURES : creation liste tous chemins possible sous forme de numeros villes
# PARAM : int | nombre de villes
# RETURN : liste chemins possibles | numeros de villes
@timer_fonction
def liste_chemins_possibles_numeros_villes(nombre_villes):
    # liste des numeros de villes
    liste = list(range(nombre_villes))

    # liste filtre chemins possibles sans miroir
    liste_sans_miroir = []

    # liste chemins possibles finale
    liste_chemins_possibles = []

    # liste des permutations des chemins sans filtre
    liste_permutations_sans_filtre = list(permutations(liste))

    # retrait chemins miroirs
    for chemin in liste_permutations_sans_filtre:
        if (chemin[0] < chemin[1]):
            liste_sans_miroir.append(chemin)

    # retrait chemins sans ville depart ville 0
    i = 0
    # pour chaque chemin
    for chemin in liste_sans_miroir:
        # si chemin commentce par ville 0
        # ajout chemin liste chemins possibles
        if chemin[0] == 0:
            liste_chemins_possibles.append(chemin)
            liste_chemins_possibles[i] = liste_chemins_possibles[i] + (0,)

        i = i + 1

    # renvoie liste chemin possibles avec numeros villes
    return liste_chemins_possibles



#FONCTION
#ensures : calcul les distances de tous les chemins possibles
#param : liste de tous les chemins possibles
#return : liste des distances de tous les chemins
@timer_fonction
def calcul_distances_chemins_possibles (liste_chemins_possibles) :

    #initialisation liste distances chemins possibles
    liste_distances_cheminsPossibles = []

    listeIndices = []
    indiceChemin = 0

    #pour chaque chemin de la liste des chemins possibles
    for chemin in liste_chemins_possibles :

        #calcul distance du chemin
        distance = calcul_distance_un_chemin(chemin)

        #ajout distance au tableau des distances
        liste_distances_cheminsPossibles.append(distance)

    #renvoi la liste des distances des chemins possibles
    return liste_distances_cheminsPossibles


#FONCTION
#ENSURES : Calcul la distance d'un chemin donné
#PARAM : un chemin
#RETURN : distance du chemin
def calcul_distance_un_chemin (chemin) :

    #compteurs
    i = 0 ;
    j = 1 ;

    #variable temporaire
    distancetemp = 0;

    #distance du chemin
    distanceUnChemin = 0;

    #tant qu'il ait possible d'itérer les villes du chemin
    while j < (len(chemin)):
        #calcul distance entre 2 villes
        distancetemp = calcul_distance_entre_2_villes(chemin[i], chemin[j])
        #distance chemin égale somme des distances entre chaque ville
        distanceUnChemin = distanceUnChemin + distancetemp
        i = i + 1;
        j = j + 1;

    #renvoi la distance du chemin
    return distanceUnChemin


#FONCTION
#ENSURES : calcul le chemin le plus court parmi tous les chemins possibles
#PARAM : distances chamins possibles, liste des chemins possibles, liste des ville
#RETURN : chemin optimal (numero villes), distance chemin optimal
@timer_fonction
def calcul_chemin_optimal(distancesCheminPossibles, cheminsPossibles, villes) :

    #initialisation cheminOptimal
    cheminOptimal = []

    #tri de de la liste des distances par ordre croissant
    distancesCheminPossibles.sort()

    #initialisation liste distance temporaire
    listeDistancesTMP = distancesCheminPossibles

    #creation lise distances non triee
    listeDistances = calcul_distances_chemins_possibles(cheminsPossibles)

    #distance la plus courte égale 1ere distance de la liste triee par ordre croissant
    distancePlusCourte = listeDistancesTMP[0]

    #on recupere le numero du chemin le plus court
    indexChemin = listeDistances.index(distancePlusCourte)

    #on recupere le chemin le plus court avec son numero
    cheminFinal = cheminsPossibles[indexChemin]

    #pour chaque ville du chemin final
    for ville in cheminFinal :

        #ajout de son numero dans la liste du parcours chemin optimal
        cheminOptimal.append(villes.index(ville))

    #renvoi le chemin optimal et sa distance
    return cheminOptimal, distancePlusCourte


# FONCTION
# ensures : Calcule la distance entre ville depart et chaque ville
# param   : liste des villes
# return  : float | liste de distances
def liste_distance_ville_depart_chaque_ville(listeVilles):
    listeDesDistances = []
    for vertice in listeVilles:
        teste = calcul_distance_entre_2_villes(listeVilles[0],vertice)
        if(teste != 0.0):
            listeDesDistances.append(teste)
    return listeDesDistances


# FONCTION
# ensures : Trouve la ville la plus proche de la 1ere ville
# param   : liste des villes
# return  : integer | indice de la ville la plus proche dans la liste "ville"
def numeroVillePlusProcheVilleDepart(ville):
    listeDesDistance = []
    ville = np.array(ville)
    for (indice, sommet) in enumerate(ville):
        calculDistance = calcul_distance_entre_2_villes(ville[0],sommet)
        if(calculDistance != 0.0):
            listeDesDistance.append(calculDistance)
    indiceVillePlusProche = listeDesDistance.index(min(listeDesDistance)) + 1
    return indiceVillePlusProche



@timer_fonction
#FONCTION
#ENSURES : creer la matrice des distances entre toutes les villes
#PARAM : liste des villes avec leurs coordonnées
#RETURN : matrice des distances
def matrice_distances(listeVille):
    # Conversion de la liste des villes en tableau
    x = np.array(listeVille)

    # initialisation de la matrice des distances
    matDist = np.zeros((len(x), len(x)))

    # Calcul des distances entre chaque ville
    for i, lig in enumerate(matDist):
        for j, col in enumerate(lig):
            matDist[i][j] = calcul_distance_entre_2_villes(listeVille[i], listeVille[j])

    #renvoi la matrice des distances
    return matDist



#FONCTION
#ENSURES : calcul distance plus court chemin avec numeros villes
#PARAM : listes chemins avec numeros villes | matrice des distances
#RETURN : chemin hmiltonien | distance chemin hamiltonien
@timer_fonction
def calcul_distance_chemin_plus_court_numeros_villes (liste_chemins, matrice_distances) :

    #liste distances chemins possibles
    liste_distances = []
    liste_distances_2 = []

    #ville depart egale ville 0
    k = 0

    #pour chaque chemin des chemins possibles
    for chemin in liste_chemins :

        #compteurs
        i = 0
        j = 1

        #distance temporaire pour calcul
        distance_tmp = 0
        #distance plus court chemin
        distance_chemin = 0

        while j < len(chemin) :

            #distance trajet ville actuelle prochaine ville
            distance_tmp = matrice_distances[ liste_chemins[k][i] ] [ liste_chemins[k][j] ]

            #distance chemin complet egale somme tous trajets
            distance_chemin = distance_chemin + distance_tmp

            i = i + 1
            j = j + 1

        #print("distance chemin : ", distanceChemin)
        liste_distances.append(distance_chemin)
        liste_distances_2.append(distance_chemin)

        #passage ville suivante comme ville depart
        k = k + 1

    #trie distances ordre croissant
    liste_distances.sort()

    #distance parcours le lus court
    distance_parcours = liste_distances[0]

    #recuperation villes parcours
    index_parcours_ville = liste_distances_2.index(distance_parcours)
    parcours_ville = liste_chemins[index_parcours_ville]

    #renvoie la distance du chemin le plus court
    return parcours_ville, distance_parcours

#FONCTION
#ENSURES : converti un chemin de la forme 1-2-3-4-5-6-7-8-9-10 en 0-1-2-3-4-5-6-7-8-9
#PARAM : chemin sous la forme user : 1-2-3-4-5-6-7-8-9-10
#RETURN : chemin sous la forme indice 0-1-2-3-4-5-6-7-8-9
def conversion_chemin_numero_ville_chemin_indice_ville (chemin) :

    #liste des villes sous forme d'indices
    chemin_indice_ville = []

    #extrait les nombres au format str de la saisie User
    chemin = re.findall(r'\d+', chemin)

    #pour chaque nombre str
    for nombre in chemin :
        #converstion nombre str en nombre int
        nombre = int(nombre)

        #retrait de 1 du nombre pour correspondre a l'indice de la ville
        nombre = nombre - 1

        #ajout du nombre int au chemin
        chemin_indice_ville.append(nombre)

    #renvoi le chemin sous forme de liste d'indices des villes
    return chemin_indice_ville




#FONCTION
#ENSURES : affichage des villes
#PARAM : coordonnes des villes au format float
#RETURN : affichage villes
def dessiner_parcours_voyageur_commerce (coordonnees_float, chemin_numero_ville) :

    #listes coordonnees X
    liste_x_villes = []

    #listes coordonnees Y
    liste_y_villes = []

    #CREATION LISTE X ET Y POUR AFFICHAGE VILLES

    #pour chaque coordonnee xy d'une ville
    for coordonnee in coordonnees_float :
        #ajout coordonnee x a la liste des x
        liste_x_villes.append(coordonnee[0])
        # ajout coordonnee y a la liste des y
        liste_y_villes.append(coordonnee[1])

    #AFFICHAGE DES VILLES

    #affiche les villes sous forme de points
    fig, ax = plt.subplots()
    ax.scatter(liste_x_villes,liste_y_villes, s = 20, color='red')

    #nom des villes à afficher
    noms = [nombre for nombre in range(1, len(liste_x_villes) + 1)]



    #pour chaque ville / point associe le nom correspondant
    for i, txt in enumerate(noms) :
        ax.annotate(txt, (liste_x_villes[i], liste_y_villes[i]))


    #SI CHEMIN DONNE PAR UTILISATEUR
    if chemin_numero_ville != 0 :

        # conversion du chemin 1-x-x-x-x-x-1 en chemin de type indices 0-x-x-x-x-x-0
        chemin = conversion_chemin_numero_ville_chemin_indice_ville(chemin_numero_ville)

        #CREATION LISTE X Y DANS ORDRE CHEMIN POUR AFFICHAGE CHEMIN

        #listes coordonnees X pour le chemin
        liste_x_villes_chemin = []

        # listes coordonnees Y pour le chemin
        liste_y_villes_chemin = []

        #pour chaque xy d'une ville
        for coordonnee in chemin :
            #ajout coordonnee x a la liste x du chemin
           liste_x_villes_chemin.append(liste_x_villes[coordonnee])
            #ajour coordonne y a la liste y du chemin
           liste_y_villes_chemin.append(liste_y_villes[coordonnee])


        #AFFICHAGE CHEMIN

        #affiche le chemin a parcourir
        plt.plot(liste_x_villes_chemin, liste_y_villes_chemin)


    #echelle identique pour x et y
    plt.axis('scaled')

    #affiche le graphique
    plt.show()


# FONCTION RECURSIVE PLUS COURT CHEMIN 
# ALGORITHME GLOUTON
#@timer_fonction
def recursiveChemin(matriceDeDistance, visited, indiceVisites, indiceEnCours, compteurDistance):

    villa = list(matriceDeDistance[indiceEnCours])

    for k, ville in enumerate(villa):
        if k in indiceVisites:
            visited.append(ville)

    mini = min_gt(villa,visited)     # je recupere la distance minimum hors visited
    inda = villa.index(mini)         # je recupere l'indice de la valeur minimum = prochaine ville
    visited.insert(1,mini)           # je sauvegarde la valeur minimum dans visited pour ne pas boucler dessus
    compteurDistance.append(mini)    # je cumule la distance
    indiceVisites.append(inda)       # je sauvegarde la ville comme parcourue
    del visited[2:]                  # je reinitialise visited pour la prochaine iteration, en gardant le min de l iteration precedente

    while len(indiceVisites) != len(matriceDeDistance):
        recursiveChemin(matriceDeDistance, visited, indiceVisites, inda, compteurDistance)
    
    return indiceVisites, sum(compteurDistance)

# FONCTION
# ensures : détermine la valeur minimum d'une liste, en exluant les valeurs présente d'une autre liste
# returns : (float) valeur minimum 
def min_gt(seq, visited):
    return min(v for v in seq if v not in visited)

#FONCTION
# ensures : Calcul la chemin optimal
# returns : (tuple) distance du chemin optimal , chemin optimal
def solutionOptimalTSP(matriceDistance):

    r = range(len(matriceDistance))
    dist = {(i, j): matriceDistance[i][j] for i in r for j in r}
    solution = tsp.tsp(r,dist)

    return solution