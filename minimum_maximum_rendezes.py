# Minimum/maximum kiválasztásos rendezés
# A két rendezés hasonlít egymáshoz.
# Minimum kiválasztásos rendezés: egy ciklussal végig megyünk a sorozat első elemétől az utolsó előtti elemig.
# A ciklus elején a 'min' változót a ciklusváltozóra állítjuk.
# Egy belső ciklussal végigmegyünk a vizsgálandó elemet követő elemtől a sorozat végéig.
# Ha a 'min' indexű elem nagyobb mint a belső ciklus által vizsgálté, akkor 'min'-t a belső ciklus változójára állítjuk.
# A külső ciklus végén megcsréljük a a sorozat 'min' indexű elemét a jelenleg vizsgált elemmel.
#
# Függvény MKR(elemtípus[ ] T): elemtípus[ ]
# változó: i,j,min: egész
# Függvény kezdete
#   Ciklus i = kezdőindextől végindex-1-ig
#       min = i
#       Ciklus j = i+1-től végindexig
#           Ha T[j] < T[min] akkor
#               min = j
#           Elágazás vége
#       Ciklus vége
#       Csere(T[i], T[min])
#   Ciklus vége
#   MKR = T
# Függvény vége


def minimum_kivalasztas(sorozat):
    length = len(sorozat)
    for i in range(0, length-1):
        min = i
        for j in range(i+1, length):
            if sorozat[j] < sorozat[min]:
                min = j
        if i != min:
            tmp = sorozat[i]
            sorozat[i] = sorozat[min]
            sorozat[min] = tmp

# Maximum kiválasztásos rendezés: egy ciklussal végig megyünk a sorozat utolsó elemétől az első elemig.
# A ciklus elején a 'max' változót a ciklusváltozóra állítjuk.
# Egy belső ciklussal végigmegyünk a sorozat elejétől a vizsgálandó elem előtti elemig.
# Ha a 'max' indexű elem kisebb mint a belső ciklus által vizsgálté, akkor 'max'-t a belső ciklus változójára állítjuk.
# A külső ciklus végén megcsréljük a a sorozat 'max' indexű elemét a jelenleg vizsgált elemmel.

# ~ def maximum_kivalasztas(sorozat):
    # ~ length = len(sorozat)
    # ~ for i in range(length-1, -1, -1):
        # ~ max = i
        # ~ for j in range(0, i):
            # ~ if sorozat[j] > sorozat[max]:
                # ~ max = j
        # ~ tmp = sorozat[i]
        # ~ sorozat[i] = sorozat[max]
        # ~ sorozat[max] = tmp
import random

elemszam = int(input("Hány elem legyen? "))
T = []
for i in range(elemszam):
    T.append(random.randint(0, elemszam*3))
print(T)
minimum_kivalasztas(T)
print(T)
# ~ maximum_kivalasztas(T)
# ~ print(T)

