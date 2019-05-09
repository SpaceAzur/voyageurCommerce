# FONCTION
# ensures : creer une liste de tous les chemins possible, sans doublon mirroir, avec la ville de depart en debut et fin de chaque chemin
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