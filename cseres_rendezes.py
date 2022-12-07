# Cserés rendezés:
# A legkisebb elem lesz az első elem.
# Kezdetben van egy rendezetlen sorozatunk. Egy ciklussal végigmegyünk az elemein, kivéve az utolsót.
# Ezen belül még egy ciklust indítunk a jelenleg vizsgált elemet követő elemtől az utolsó elemig.
# Ha a külső ciklus eleme nagyobb, mint a belsőé, akkor cserélünk, különben megyünk tovább.
# 
# Függvény ECS(elemtípus[ ] T): elemtípus[ ]
# változó:  i,j: egész
# Függvény kezdete
#   Ciklus i = kezdőindextől végindex-1-ig
#       Ciklus j = i+1-től végindexig
#           Ha T[i] > T[j] akkor
#               Csere(T[i], T[j])
#           Elágazás vége
#       Ciklus vége
#   Ciklus vége
#   ESC = T
# Függvény vége
# 
# A csere, amit eljárásban, vagy függvényben is meg lehet írni:
# Seged = T[i]
# T[i] = T[j]
# T[j] = Seged
import random

def cseres_rendezes(sorozat):
    length = len(sorozat)
    for i in range(length-1):
        for j in range(i+1, length):
            if sorozat[i] > sorozat[j]:
                sorozat[i], sorozat[j] = sorozat[j], sorozat[i]
                #tmp = sorozat[i]
                #sorozat[i] = sorozat[j]
                #sorozat[j] = tmp

elemszam = int(input("Hány elem legyen? "))
T = []
for i in range(elemszam):
    T.append(random.randint(0, elemszam*3))
print(T)
cseres_rendezes(T)
print(T)
