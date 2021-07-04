#grille de 4 par 4
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

def canFill(mot,x,y,ori,grille,long,haut):
    if ori == "hori":
        if x + len(mot) > long:
            return False
        for i in range (len(mot)):
            if grille[y][x+i] != " " and grille[y][x+i] != mot[i]:
                return False     
    elif ori == "verti":
        if y + len(mot) > haut:
            return False
        for i in range (len(mot)):
            if grille[y+i][x] != " " and grille[y+i][x] != mot[i]:
                return False
    return True

######### Main #########
"""
grille[5][2] = "a"
2 : x
5 : y
"""
#création grille
long = 5
haut = 5
grille = createGrid(long,haut)

mot1 = ("arme",1,1,"hori")
mot2 = ("carte",1,0,"verti")

if canFill(mot1[0],mot1[1],mot1[2],mot1[3],grille,long,haut):
    grille = fillWord(mot1[0],mot1[1],mot1[2],mot1[3],grille)
if canFill(mot2[0],mot2[1],mot2[2],mot2[3],grille,long,haut):
    grille = fillWord(mot2[0],mot2[1],mot2[2],mot2[3],grille)
afficherGrid(grille)