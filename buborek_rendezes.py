# Buborékos rendezés
# A legkisebb elem az első.
# Egy ciklussal végigmegyünk a sorozat utolsó elemétől a 2. eleméig
# Egy belső ciklussal végigmegyünk a első elemétől az vizsgált elem előtti elemig.
# Ha a belső ciklusban vizsgált elem nagyobb mint az azután következő, akkor cserélünk.
#
# Függvény BUBI(Elemtípus[ ] T): Elemtípus[ ]
# változó:  i, j: egész
# Függvény kezdete
#    Ciklus i = végindextől kezdőindex+1-ig lk = -1
#       Ciklus j = kezdőindextől i-1-ig lk = -1
#           Ha T[j] > T[j+1] akkor
#               Csere(T[j], T[j+1])
#           Elágazás vége
#       Ciklus vége
#   Ciklus Vége
#   BUBI = T
# Függvény vége

def buborekos_rendezes(sorozat):
    length = len(sorozat)
    for i in range(length-1, 0, -1):
        for j in range(0, i):
            if(sorozat[j] > sorozat[j+1]):
                tmp = sorozat[j+1]
                sorozat[j+1] = sorozat[j]
                sorozat[j] = tmp

L = [7,9,4,5,8,3,5,2,3,1,0,9]
buborekos_rendezes(L)
print(L)
