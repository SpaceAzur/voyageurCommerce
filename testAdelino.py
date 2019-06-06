def algorithme_permutation_heap(liste_nombres, n):
    # variable pour swap
    tmp = 0

    if n > 2:
        # print(n, "> 2")
        # print("Appel recursif haut ")
        algorithme_permutation_heap(liste_nombres, n - 1)

    # ETAPE 2
    for i in range(0, n - 1):
        # print("\n\nfor ", i)
        # print("valeur n : ", n)
        # print("valeur i : ", i)

        if n % 2 != 0:
            # print("if n", liste_nombres[n-1])
            # print("Impair")
            # print("Avant swap : ",liste_nombres[0], "et", liste_nombres[n - 1] )

            # print(liste_nombres)
            tmp = liste_nombres[0]
            liste_nombres[0] = liste_nombres[n - 1]
            liste_nombres[n - 1] = tmp

            # print("Apres swap : ",liste_nombres[0], "et", liste_nombres[n - 1] )
            # compteur_permutation = compteur_permutation + 1
            # print(liste_nombres)

        # print("")

        else:
            # print("pair")
            # print("Avant swap : ", liste_nombres[i], "et", liste_nombres[n - 1] )
            # print(liste_nombres)
            tmp = liste_nombres[i]
            liste_nombres[i] = liste_nombres[n - 1]
            liste_nombres[n - 1] = tmp

            # print("Apres swap ")
            # print(liste_nombres)
            # print("")

        if n > 2:
            # print("valeur n : ", n)
            # print("go rec 2")
            algorithme_permutation_heap(liste_nombres, n - 1)

        # PROCESS

    return






