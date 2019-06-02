from fonctionsSolutionOptimale import *


#recupere les coordonnes des villes (tuples de str)
coordonnees_villes = liste_coordonnees_villes_from_csv('data/test10.csv')

#converti ces coordonnees en float (besoin graphique)
coordonnees_float = convertion_liste_coordonnees_str_liste_coordonnes_float(coordonnees_villes)

#affiche villes

#USAGE
#mettre 0 si affichage villes uniquement
#mettre chemin sous la forme '1-x-x-x-x-x-x-x-x-x-1' pour afficher parcours

#affichage villes
#dessiner_parcours_voyageur_commerce(coordonnees_float, 0)

#affichage ville + parcours
dessiner_parcours_voyageur_commerce(coordonnees_float, '1-2-4-5-6-9-10-8-7-3-1')