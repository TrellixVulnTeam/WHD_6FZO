from random import randint
import csv

with open('parametros.csv', 'w') as csvfile:
    filewriter = csv.writer(csvfile, delimiter=',',quotechar='|', quoting=csv.QUOTE_MINIMAL)
    filewriter.writerow(['fc', 'fr','dream'])
    for fc in range(40,71):
        for rc in range(8,19):
            filewriter.writerow([fc,rc])