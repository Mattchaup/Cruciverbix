# -*- coding: utf-8 -*- 
import time

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
    return apparition

def findCorrectData(info,longMot,place):
    for data in info:
        if data[0] == longMot:
            if data[1] == place:
                return data[2]

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

def findMini(mini,x):
    if mini > x:
        return x
    return mini

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

start = time.time()
dico = ouverturDico("GrandDico.txt")

######### Trouver les mot les plus courants #########

dicoMot = firstSort(dico,7,{0:"a",1:"r",2:"m"})
listeDico = [firstSort(dico,9,{0:"a",1:"b",2:"s"}),firstSort(dico,9,{0:"p",1:"o",2:"s"}),firstSort(dico,9,{0:"a",1:"n",2:"a"}),firstSort(dico,9,{0:"r",1:"a",2:"i"}),
            firstSort(dico,9,{0:"e",1:"t",2:"e"}),firstSort(dico,9,{0:"r",1:"e",2:"n"}),firstSort(dico,9,{0:"a",1:"r",2:"t"})]
datas = [lettreCourante(dico,3) for dico in listeDico] 
listeScore = {}

for mot in dicoMot:
    mini = datas[0][mot[3]]

    score = datas[1][mot[4]]
    mini = findMini(mini, score)

    score = datas[2][mot[5]]
    mini = findMini(mini, score)

    score = datas[3][mot[6]]
    mini = findMini(mini, score)

    if mini > 0:
        listeScore.update({mot:mini})


affichagePoucent(listeScore,30)
end = time.time()
total = end - start
print(f"temps : {round(total,3)} secondes")

######## Permet de créer le grand document txt ########
"""
for longMot in range(2,26):
    newDic = firstSort(dico,longMot)
    for place in range(longMot):
        bestLettre = lettreCourante(newDic,place)
        print(ecrirApparitionLettre("apparitionLettre.txt",bestLettre,longMot,place))
"""