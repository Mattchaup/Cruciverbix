#import
from grille import*
from cruciverbix import*
from binaryTree import*

# Dictionnaire
dico = ouverturDico("dicoPratique.txt")

### création de la grille ###
grille = createGrid(7,7)

### création de toute les apparitions ###
listeApparition = [lettreCourante(dico,i) for i in range(7)]

"""
Trouver un rapport entre le nombre minimum de mot dispo
et le nombre que l'on pour ajouter
"""

classement = wordTree()
for mot in dico:
    s,nbMot = getScore(mot,listeApparition[0])
    score = s + nbMot/1000
    classement.add(mot,score,nbMot,0,0,"verti")

for i in range(5):
    best,parent = classement.bestWord()
    print(best.info)
    classement.deleteBest(best,parent)