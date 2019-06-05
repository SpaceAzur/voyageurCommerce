#FONCTION
#ENSURES : demande a utilisateur le numero de la liste a utiliser
#PARAM : numero de liste
#return : numero
def demande_choix_ville () :

    validation_reponse = 1

    print("Voici les listes de coordonnées disponibles : \n\n"
            "1/ Test10 : 10 villes \n"
            "2/ Berlin :  52 villes\n"
            "3/ Burma : 14 villes\n"
            "4/ Djibouti : 38 villes\n"
            "5/ Lu : 980 villes \n"
            "6/ Qatar : 194 villes\n"
            "7/ Ulysses : 16 villes\n"
            "8/ UY : 734 villes\n"
            "9/ West Sahara : 29 villes\n\n")

    while validation_reponse == 1 :

        print("Entrer le numéro de la liste que vous souhaitez utiliser : \n")

        choix_fichier = input()

        if choix_fichier not in ["1","2","3","4","5","6","7"] :

              print("\nNuméro de ville incorrecte. \n")

        else:

            validation_reponse = 0


    return choix_fichier


#FONCTION
#ENSURES : convertit un chemin sous forme d'une liste en x-x-x-x-x-x-x-x
#PARAM : chemin sour forme de liste
#RETURN : str | chemin
def convertion_chemin_liste_pour_user(chemin_liste) :

    chemin = "{}".format(chemin_liste[0] + 1)
    taille_chemin = len(chemin_liste)
    compteur = 1

    while compteur < taille_chemin :

        chemin += "-{}".format(chemin_liste[compteur] + 1)
        compteur = compteur + 1


    return chemin



#FONCTION
#ENSURES
#PARAM : numero liste choix utilisateur
#RETURN : chemin fichier csv
def selection_chemin_fichier_csv (choix_user) :

    fichier_csv = 0

    if choix_user == "1" :

        fichier_csv = "data/test10.csv"

    elif choix_user == "2" :

        fichier_csv = "data/berlin52.csv"

    elif choix_user == "3" :

        fichier_csv = "data/burma14.csv"

    elif choix_user == "4" :

        fichier_csv = "data/djibouti38.csv"

    elif choix_user == "5" :

        fichier_csv = "data/lu980.csv"

    elif choix_user == "6" :

        fichier_csv = "data/qatar194.csv"

    elif choix_user == "7" :

        fichier_csv = "data/ulysses16.csv"

    elif choix_user == "8" :

        fichier_csv = "data/uy734.csv"

    elif choix_user == "9" :

        fichier_csv = "data/westsahara29.csv"


    return fichier_csv

