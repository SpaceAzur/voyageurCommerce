from fonctionsSolutionOptimale import *
from itertools import permutations
from fonctions_main import *
import time
import numpy as np


##########################################
#### SOLUTION 1 : utilise les listes #####
##########################################


print("##################################################\n"
      "################## SOLUTION 2 ####################\n"
      "################################################## \n\n")


#demande choix liste user
choix_user = demande_choix_ville()

#selection chemin fichier csv
fichier_csv = selection_chemin_fichier_csv(choix_user)

#debut chrono
print("\nDépart du chrono ! ")
start_time = time.time()

#recupertion coordonnees villes
liste_villes = liste_coordonnees_villes_from_csv(fichier_csv)

#recuperation nombre villes
nombre_villes = len(liste_villes)

#generation chemins hamiltoniens possibles
liste_chemins_possibles = liste_chemins_possibles_numeros_villes(nombre_villes)

#calcul distances entre villes
matrice_distances = matrice_distances(liste_villes)

#calcul plus court chemin | villes parcours
parcours, distance = calcul_distance_chemin_plus_court_numeros_villes(liste_chemins_possibles, matrice_distances)

#fin chrono
chrono = (round((time.time() - start_time), 4))

print("\n\nLe chemin le plus court est  : ", convertion_chemin_liste_pour_user(parcours))

print("\nSa distance est de ", round((distance), 4), "unités. ")

print("\nTemps d'exécution du programme : %s secondes " %chrono)



#converti ces coordonnees en float (besoin graphique)
coordonnees_float = convertion_liste_coordonnees_str_liste_coordonnes_float(liste_villes)

#affichage ville + parcours
dessiner_parcours_voyageur_commerce(coordonnees_float, convertion_chemin_liste_pour_user(parcours))