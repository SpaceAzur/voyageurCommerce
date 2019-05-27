from fonctionsSolutionOptimale import *


##########################################
#### SOLUTION 1 : utilise les listes #####
##########################################

#debut chrono
start_time = time.time()

#recuperation coordonnees villes
liste_villes = liste_coordonnees_villes_from_csv('../data/test10.csv')

#generation chemins hamiltoniens
liste_chemins = liste_chemins_possibles(liste_villes)

#calcul distances chemins hamiltoniens
tableauDistances = calcul_distances_chemins_possibles(liste_chemins)

#calcul parcours optimal | distance parcours optimal
cheminOptimal, distanceCheminOptimal = calcul_chemin_optimal(tableauDistances, liste_chemins, liste_villes)


print("\n\nchemin optimal : ", cheminOptimal)

print("\ndistance chemin optimal :", distanceCheminOptimal)


print("\ntimer programme  %s seconds ---" % (time.time() - start_time))