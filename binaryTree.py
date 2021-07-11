#vérifier si le best est la root

class Word:
    def __init__ (self,mot,score,nbMot,x,y,ori):
        self.mot = [mot]
        self.score = score
        self.nbMot = nbMot
        self.x = x
        self.y = y
        self.ori = ori
    
    def __str__(self):
        if len(self.mot)>1:
            listeMot = ""
            for mot in self.mot:
                listeMot += f"{mot}, " 
            return f"score : {self.score} | nbMot : {self.nbMot} | Mots : {listeMot[:-2]}"
        return f"Score : {self.score} | nbMot : {self.nbMot} | Mots : {self.mot[0]}"


class Node:
    def __init__(self,info,left,right):
        self.info = info
        self.left = left
        self.right = right

class wordTree:
    def __init__(self):
        self.root = None
    
    def add(self,mot,score,nbMot,x,y,ori):
        if self.root == None:
            self.root = Node(Word(mot,score,nbMot,x,y,ori),None,None)
        else:
            current = self.root
            parent = None
            
            while current != None:
                parent = current
                if score == current.info.score:
                    """
                    if nbMot < current.info.nbMot:
                        current = current.right
                    elif nbMot > current.info.nbMot:
                        current = current.left
                    else:
                        current.info.mot.append(mot)
                        return
                    """
                    current.info.mot.append(mot)
                    return
                elif score > current.info.score:
                    current = current.right
                else:
                    current = current.left
            current = Node(Word(mot,score,nbMot,x,y,ori),None,None)
            if score >= parent.info.score:
                parent.right = current
            else:
                parent.left = current
    
    def bestWord(self):
        if self.root == None:
            return "Le classement est vide"
        return wordTree.findBest(self.root,None)
    
    @staticmethod
    def findBest(r,parent):
        if r.right != None:
            return wordTree.findBest(r.right,r)
        return r,parent
    
    def deleteBest(self,r,parent):
        if r.left != None:
            parent.right = r.left
        else:
            parent.right = None

"""
bdico = ouverturDico("GrandDico.txt")
dico = firstSort(bdico,10)

classement = wordTree()
for mot in dico:
    classement.add(mot,getScore(mot,point),0,0)

for i in range(5):
    best,parent = classement.bestWord()
    print(best.info)
    classement.deleteBest(best,parent)
"""