



from fonctionsSolutionOptimale import *

listeVilles = listeCoordonneesVillesFromCSV('test10.csv')

listeChemins = listeCheminsPossibles(listeVilles)

tableauDistances = calculDistancesCheminsPossibles(listeChemins)



cheminOptimal, distanceCheminOptimal = cheminOptimal(tableauDistances, listeChemins, listeVilles)

print("chemin optimal :", cheminOptimal)
print("")
print("distance chemin optimal :", distanceCheminOptimal)





