NB_COLONNE = 4
NB_LIGNE = 3


class Rumba:
    """
    Création de Rumba, prend une organisation initiale dans "rumba" et l'organisation but dans "but"
    elle a aussi une option heuristique, list des mouvements précédents et top de chaque piles
    """
    def __init__(self, setRumba, setBut):
        self.rumba = setRumba
        self.lstMvmnt = []
        self.but = setBut
        self.top = self.create_topPile()
        self.heuristique = self.calculHeuristique()

    #creer la liste des top
    def create_topPile(self) :
        top=[]
        for i in range(NB_COLONNE) :
            top.append(self.getTop(i))
        return top

    #retourne l'indice de la valeur accessible d'une colonne
    def getTop(self, numCol):
        for i in range(NB_LIGNE) :
            if self.rumba[i][numCol] != 0:
                return i
        return NB_LIGNE

    #deplace la piece en haut de la colonne de "fromCol" a "toCol"
    #retourne True si possible et False si impossible
    def mouvPiece(self, fromCol, toCol):
        temp = Rumba([innerList[:] for innerList in self.rumba]
                , [innerList[:] for innerList in self.but])
        if not self.isMouvPossible(fromCol, toCol):
            return False, temp

        test = self.top[toCol]-1
        if temp.rumba[2][toCol] == 0:
            test =2

        temp.rumba[self.top[fromCol]][fromCol] = 0
        temp.top[fromCol] = temp.getTop(fromCol)
        temp.rumba[test][toCol] = self.rumba[self.top[fromCol]][fromCol]
        temp.top[toCol] = temp.getTop(toCol)

        temp.lstMvmnt = [innerList[:] for innerList in self.lstMvmnt]
        temp.lstMvmnt.append([fromCol, toCol])
        temp.heuristique = temp.calculHeuristique()

        return (True, temp)



    #retourne True si le mouvement est possible
    def isMouvPossible(self, fromCol, toCol) :
        return ((self.rumba[self.top[fromCol]][fromCol] != 0) and
                 (self.rumba[0][toCol] == 0) and (fromCol != toCol))

    #retourne true si le but est atteint
    def isButAtteint(self):
        return self.isEqual(self.but)

    #test si le rumba est égale a un autre rumba.rumba bis (rumbis)
    def isEqual(self, rumbis):
        return self.rumba == rumbis

    #renvoie quantité de nombres mal mis dans rumba par rapport au but
    def nombreMalMis(self):
        nbMalMis =0

        for i in range(NB_LIGNE):
            for j in range(NB_COLONNE):
                if self.rumba[i][j] != self.but[i][j]:
                    nbMalMis+=1

        return nbMalMis

    #calcul l'heuristique nombre mal mis
    def calculHeuristique(self):
        return len(self.lstMvmnt)+self.nombreMalMis()

#affiche la matrice avec code ansi
def AfficherMatrice(matrice):
    rslt =""
    for i in range(NB_LIGNE):
        rslt += "\n"
        for j in range(NB_COLONNE):
            chiffre = matrice[i][j]
            match chiffre :
                case 0 :
                    rslt += " | "
                case 1 | 2 | 3 :
                    rslt += "\33[43m " + str(chiffre) + " \33[0m" #\33[43m code Jaune
                case 4 | 5 | 6 :
                    rslt += "\33[44m " + str(chiffre) + " \33[0m" #\33[44m code Bleu
                case 7 | 8 | 9 :
                    rslt += "\33[41m " + str(chiffre) + " \33[0m" #\33[41m code Rouge

    rslt += "\n"
    return rslt

#affiche la matrice sans code ansi
def AfficherMatriceSansCouleurs(matrice):
    rslt =""
    for i in range(NB_LIGNE):
        rslt += "\n"
        for j in range(NB_COLONNE):
            chiffre = matrice[i][j]
            match chiffre :
                case 0 :
                    rslt += " | "
                case 1 | 2 | 3 :
                    rslt += " " + str(chiffre) + " "

                case 4 | 5 | 6 :
                    rslt += " " + str(chiffre) + " "

                case 7 | 8 | 9 :
                    rslt += " " + str(chiffre) + " "

    rslt += "\n"
    return rslt
