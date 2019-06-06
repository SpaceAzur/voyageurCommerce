from fonctions_main import *
from fonctionsSolutionOptimale import *

##########################################
#### SOLUTION 1 : utilise les listes #####
##########################################


print("##################################################\n"
      "################## SOLUTION 1 ####################\n"
      "################################################## \n\n")


#demande choix liste user
choix_user = demande_choix_ville()

#selection chemin fichier csv
fichier_csv = selection_chemin_fichier_csv(choix_user)

#debut chrono
print("\nDépart du chrono ! ")
start_time = time.time()

#recuperation coordonnees villes
liste_villes = liste_coordonnees_villes_from_csv(fichier_csv)

#generation chemins hamiltoniens
liste_chemins = liste_chemins_possibles_tuples_coordonnees(liste_villes)

#tableau distances chemins hamiltoniens
tableau_distances = calcul_distances_chemins_possibles(liste_chemins)


#calcul parcours optimal | distance parcours optimal
cheminOptimal, distanceCheminOptimal = calcul_chemin_optimal_methode_liste(tableau_distances, liste_chemins, liste_villes)

chrono = (round((time.time() - start_time), 4))

print("\n\nLe chemin le plus court est  : ", convertion_chemin_liste_pour_user(cheminOptimal))

print("\nSa distance est de ", round((distanceCheminOptimal), 4), "unités. ")

print("\nTemps d'exécution du programme : %s secondes " %chrono)


#Affichage chemin

#converti ces coordonnees en float (besoin graphique)
coordonnees_float = convertion_liste_coordonnees_str_liste_coordonnes_float(liste_villes)

#affichage ville + parcours
dessiner_parcours_voyageur_commerce(coordonnees_float, convertion_chemin_liste_pour_user(cheminOptimal))