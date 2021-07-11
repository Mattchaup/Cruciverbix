"""
- Créer un grille :                                             createGrid(x,y)
- Affiche la grille de manière agréable :                       afficherGrid(grille)
- Ajouter un mot selon les coordonées x,y et l'orientation :    fillWord(mot,x,y,ori,grille)
- N'ajoute pas le mot s'il ne peut pas être posé :              canFill(mot,x,y,ori,grille)
- Supprime un mot selon les coordonées x,y et l'orientation :   deleteWord(grille,x,y,ori)
"""


def createGrid(x,y):
    """
    x, y = longueur, hauteur
    """
    return [[" " for i in range(x)] for j in range (y)]

def afficherGrid(grille):
    grid = "|"
    for raw in grille:
        for lettre in raw:
            grid += lettre + '|'
        grid += "\n|"
    print(grid[:-1])

def fillWord(mot,x,y,ori,grille):
    if ori == "hori":
        for i in range (len(mot)):
            grille[y][x+i] = mot[i]
    elif ori == "verti":
        for i in range (len(mot)):
            grille[y+i][x] = mot[i]
    return grille

def canFill(mot,x,y,ori,grille):
    if ori == "hori":
        if x + len(mot) > len(grille[0]):
            return False
        for i in range (len(mot)):
            if grille[y][x+i] != " " and grille[y][x+i] != mot[i]:
                return False     
    elif ori == "verti":
        if y + len(mot) > len(grille):
            return False
        for i in range (len(mot)):
            if grille[y+i][x] != " " and grille[y+i][x] != mot[i]:
                return False
    return True

def nearClearVerti(grille,x,y):
    if x > 0:
        if grille[y][x-1] != " ":
            return False
    if x < len(grille[0])-1:
        if grille[y][x+1] != " ":
            return False
    return True

def nearClearHori(grille,x,y):
    if y > 0:
        if grille[y-1][x] != " ":
            return False
    if y < len(grille) -1:
        if grille[y+1][x] != " ":
            return False
    return True

def deleteWord(grille,x,y,ori):
    if ori == "verti":
        while y < len(grille):
            if grille[y][x] != " ":
                if nearClearVerti(grille,x,y):
                    grille[y][x] = " "
                y += 1
    elif ori == "hori":
        while x < len(grille[0]):
            if grille[y][x] != " ":
                if nearClearHori(grille,x,y):
                    grille[y][x] = " "
                x += 1


######### Main #########
"""
grille[5][2] = "a"
2 : x
5 : y
len(grille) = hauteur
len(grille[0]) = longueur
"""

"""
#création grille
long = 10
haut = 5
grille = createGrid(long,haut)

mot1 = ("chouquette",0,4,"hori")
mot2 = ("carte",6,0,"verti")
mot3 = ("abaissable",0,1,"hori")

listeMot = [mot1,mot2,mot3]

for mot in listeMot:
    if canFill(mot[0],mot[1],mot[2],mot[3],grille,long,haut):
        grille = fillWord(mot[0],mot[1],mot[2],mot[3],grille)
afficherGrid(grille)
deleteWord(grille,6,0,"verti")
deleteWord(grille,0,1,"hori")
afficherGrid(grille)
"""