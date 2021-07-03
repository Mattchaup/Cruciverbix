# -*- coding: utf-8 -*- 
def ouverturDico(name):
    dico=[]
    with open (name, 'r',encoding="utf-8") as doss:
        lmots=doss.readlines()
    for mot in lmots:
        dico.append(mot[0:-1].lower())
    return dico

def ecrirApparitionLettre(name,apparition,longMot,place):
    message = ""
    for lettre in apparition:
        message += f"{lettre}:{apparition[lettre]}&"
    with open(name,'a',encoding="utf-8") as doss:
        doss.write(f"{longMot}&{place}&{message}\n")
    return f"Fait : Longueur : {longMot}, Place : {place}"

def recupDonnee(name):
    info = []
    with open(name,'r',encoding="utf-8") as doss:
        currentListe = doss.readlines()
    for data in currentListe:
        liste = data.split("&")
        newDic = {}
        for asso in liste[2:-1]:
            newDic.update({asso[0]:float(asso[2:])})
        info.append([int(liste[0]),int(liste[1]),newDic])
    return info

def lettreCourante(dico,place):
    apparition = {'a':0,'z':0,'e':0,'r':0,'t':0,'y':0,'u':0,'i':0,'o':0,'p':0,'q':0,'s':0,'d':0,'f':0,'g':0,'h':0,
                'j':0,'k':0,'l':0,'m':0,'w':0,'x':0,'c':0,'v':0,'b':0,'n':0}
    for mot in dico:
        lettre = mot[place]
        apparition[lettre] += 1
    for lettre in apparition:
        apparition[lettre] = round(apparition[lettre]/len(dico)*100,2)
    return apparition

def findCorrectData(info,longMot,place):
    for data in info:
        if data[0] == longMot:
            if data[1] == place:
                return data[2]

def palymdrome(mot):
    if len(mot) < 2:
        return True
    if mot[0] == mot[-1]:
        return palymdrome(mot[1:-1])
    else:
        return False

def palymReturn(mot,coress):
    if len(mot)==0:
        return True
    elif len(mot) == 1:
        if mot in coress:
            if coress[mot] == mot:
                return True
    elif mot[0] in coress:
        if mot[-1] == coress[mot[0]]:
            return palymReturn(mot[1:-1],coress)
        return False
    return False

def findAllPalym(dico):
    listePalym = []
    for mot in dico:
        if palymdrome(mot):
            listePalym.append(mot)
    return listePalym

def findReturnWord(dico,coress):
    listeMot = []
    for mot in dico:
        if palymReturn(mot,coress):
            listeMot.append(mot)
    return listeMot

def bestWord(mot,score):
    dico = {}
    for i in range(50):
        j = score.index(max(score))
        #print(f"{i+1} - {mot[j]} : {score[j]}")
        dico.update({mot[j]:score[j]})
        del mot[j]
        del score[j]
    return dico

def isAnagraph(mot1,mot2):
    if len(mot1) != len(mot2) or mot1 == mot2:
        return False
    liste1 = [lettre for lettre in mot1]
    liste2 = [lettre for lettre in mot2]
    for lettre in liste1:
        if lettre in liste2:
            liste2.remove(lettre)
        else:
            return False
    return True

def allAnagraph(dico,mot):
    realDico = firstSort(dico,len(mot))
    allAna = []
    for m in realDico:
        if isAnagraph(mot,m):
            allAna.append(m)
    return allAna

def plusLongAnagraph(dico):
    #réponse : ('anticonstitutionnels', 'constitutionnalisent')
    nbr = 25
    for i in range(25):
        bonDico = firstSort(dico,nbr-i)
        for m1 in bonDico:
            for m2 in bonDico:
                if isAnagraph(m1,m2):
                    return m1,m2

def classify(liste):
    scores = [len(mot) for mot in liste]
    classement = []
    for _ in range(len(liste)):
        best = scores.index(max(scores))
        classement.append(liste[best])
        del scores[best]
        del liste[best]
    return classement

def testCondition(mot,condition):
    for ind in condition:
        if mot[ind] != condition[ind]:
            return False
    return True

def firstSort(dico,nbr,conditions):
    sortedList = []
    for mot in dico:
        if len(mot) == nbr:
            if testCondition(mot,conditions):
                sortedList.append(mot)
    return sortedList

def belAffichage(liste,nbr):
    if nbr > len(liste):
        nbr = len(liste)
    for i in range(nbr):
        print(f"{liste[i]}   -   {len(liste[i])}")

def affichagePoucent(liste,top):
    dic2=dict(sorted(liste.items(),key= lambda x:x[1],reverse=True))
    if top > len(dic2):
        top = len(dic2)
    for lettre in dic2:
        print(f"{lettre} : {dic2[lettre]} %")
        top -= 1
        if top<0:
            return

#########"MAIN"########
longueurMot = {'25': 1, '24': 2, '23': 7, '22': 27, '21': 68, '2': 81, '20': 157, '19': 353, 
                '3': 427, '18': 817, '4': 1799,'17': 1874, '16': 4066, '5': 5891, '15': 8212, 
                '6': 13901, '14': 15006, '13': 24771, '7': 25455, '12': 35713, '8': 38095, '11': 45224, 
                '9': 47249, '10': 49687}

dico = ouverturDico("GrandDico.txt")

######### Trouver les mot les plus courants #########

info = recupDonnee("apparitionLettre.txt")
dicoMot = firstSort(dico,11,{0:"e"})
listeDico = [firstSort(dico,9,{0:"e"}),firstSort(dico,9,{0:"c"}),firstSort(dico,9,{0:"a"}),firstSort(dico,9,{0:"r"}),firstSort(dico,9,{0:"d"})]
listeScore = {}
for mot in dicoMot:
    score = 0
    data = lettreCourante(listeDico[0],1)
    score += data[mot[1]]
    score += data[mot[6]]
    data = lettreCourante(listeDico[1],1)
    score += data[mot[2]]
    data = lettreCourante(listeDico[2],1)
    score += data[mot[3]]
    score += data[mot[8]]
    data = lettreCourante(listeDico[3],1)
    score += data[mot[4]]
    score += data[mot[7]]
    data = lettreCourante(listeDico[4],1)
    score += data[mot[5]]
    listeScore.update({mot:score})

affichagePoucent(listeScore,10)

######## Permet de créer le grand document txt ########
"""
for longMot in range(2,26):
    newDic = firstSort(dico,longMot)
    for place in range(longMot):
        bestLettre = lettreCourante(newDic,place)
        print(ecrirApparitionLettre("apparitionLettre.txt",bestLettre,longMot,place))
"""

######## Dictionnaire python ########
"""
retournement = {"b":"q","d":"p","h":"y","m":"w","n":"u","o":"o","p":"d","q":"b","s":"s","u":"n","w":"m","x":"x","y":"h","z":"z","h":"h","i":"i"}
miroir = {"b":"d","d":"b","i":"i","l":"l","m":"m","n":"n","o":"o","p":"q","q":"p","t":"t","u":"u","v":"v","w":"w","x":"x"}
"""

"""
caca = findReturnWord(dico,retournement)
belAffichage(classify(caca),5)
"""

#print(plusLongAnagraph(dico))

"""
while True:
    mot = input(">> : ")
    print(mot,allAnagraph(dico,mot))
"""

#allPal = findAllPalym(dico)
#belAffichage(classify(allPal),10)
