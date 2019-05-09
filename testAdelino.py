from fonctionsSolutionOptimale import *



def ouvrirFichierCSV (fichiercsv) :
    ville = []
    with open(fichiercsv) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            for coord in row:
                coord = float(coord)

            ville.append(row)

    return ville