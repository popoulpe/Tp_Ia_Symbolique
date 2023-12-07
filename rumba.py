NB_COLONNE = 4
NB_LIGNE = 3


class Rumba:
    def __init__(self, setRumba, setBut):
        self.rumba = setRumba
        self.but = setBut
        self.top = self.create_topPile()

    #creer la liste des top
    def create_topPile(self) :
        top=[]
        for i in range(NB_COLONNE) :
            top.append(self.rumba[self.getTop(i)][i])
        return top
    
    #retourne l'indice de la valeur accessible d'une colonne
    def getTop(self, numCol):
        for i in range(NB_LIGNE) :
            if self.rumba[i][numCol] != 0:
                return i
        return NB_LIGNE-1
    
    #deplace la piece en haut de la colonne de "fromCol" a "toCol"
    #retourne True si possible et False si impossible
    def mouvPiece(self, fromCol, toCol):
        temp = Rumba([innerList[:] for innerList in self.rumba]
                     , [innerList[:] for innerList in self.but])
        if not self.isMouvPossible(fromCol, toCol):
            return (False, temp)
        ligFromCol = temp.getTop(fromCol)
        ligToCol = temp.getTop(toCol)-1

        temp.rumba[ligToCol][toCol] = temp.rumba[ligFromCol][fromCol]
        temp.top[toCol] = temp.rumba[ligFromCol][fromCol]
        temp.rumba[ligFromCol][fromCol] = 0
        temp.top[fromCol] = temp.rumba[temp.getTop(fromCol)][fromCol]
        return (True, temp)

    #retourne True si le mouvement est possible 
    def isMouvPossible(self, fromCol, toCol) :
        return ((self.top[fromCol] != 0) and (self.rumba[0][toCol] == 0) and (fromCol != toCol))
    
    #retourne true si le but est atteint
    def isButAtteint(self):
        return self.isEqual(self.but)
    
    #test si le rumba est égale a un autre rumba.rumba bis (rumbis)
    def isEqual(self, rumbis):
        return self.rumba == rumbis
    
    #test is le rumba self est inclu dans une liste de rumba
    def isIn (self, listTest):
        for e in listTest:
            if self.isEqual(e.rumba):
                return True
        return False