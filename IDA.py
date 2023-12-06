class Tree:
    def __init__(self, pere, valeur, cout):
        self.pere= pere
        self.valeur= valeur
        self.cout= cout
        self.fils= []
        self.nbFils =0

    def ajoutFils(self, fils):
        self.fils.append(fils)
        self.nbFils+=1
    
    def getPere(self):
        return self.pere
    
    def getFils(self, indice):
        return self.fils[indice]

x= [[None]*3]*4
print(x)

    
"""
x= Tree(value=12, cost= 35)
y= Tree(value=20, cost=20)
x.child.append(y)
y.root = x
"""

#dataTree est l'arbre de toutes les datas


def ProfondeurBornee(data):
    nSeuil = None
    vue= None
    enAttente = []


MAX_COLONNE=3
MAX_LIGNE =4

vraie_liste= []
top =[]

i_colonne =0
i_ligne=0
for i_colonne in range(MAX_COLONNE):
    while len(top) < i_colonne+1:
        if vraie_liste[i_ligne][i_colonne] != None:
            top.append(vraie_liste[i_ligne][i_colonne])
        elif i_ligne+1 >= MAX_LIGNE:
            top.append(None)
        i_ligne +=1
