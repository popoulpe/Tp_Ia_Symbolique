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
        if self.isMouvPossible(fromCol, toCol):
            return (False, temp)
        ligFromCol = temp.getTop(fromCol)
        ligToCol = temp.getTop(toCol)-1

        temp.rumba[ligToCol][toCol] = temp.rumba[ligFromCol][fromCol]
        print("a", toCol, " ", ligFromCol, " ", fromCol, " et ", len(temp.rumba))
        temp.top[toCol] = temp.rumba[ligFromCol][fromCol]
        temp.rumba[ligFromCol][fromCol] = 0
        temp.top[fromCol] = temp.rumba[temp.getTop(fromCol)][fromCol]
        return (True, temp)

    #retourne True si le mouvement est possible 
    def isMouvPossible(self, fromCol, toCol) :
        return not((self.top[fromCol] == 0) or (self.rumba[0][toCol] != 0))
    
    #retourne true si le but est atteint
    def isButAtteint(self):
        return self.rumba == self.but
    
    def isEqual(self, test):
        return self.rumba == test.rumba
    
    def isIn (self, listTest):
        for e in listTest:
            if self.isEqual(e):
                return True
        return False

    """ commentaire pour pouvoir compiler
    #def testEtatBut(etat) :                            #testEtatBut(etat) ; {prédicat caractérisant les buts}

    def filsEtat(etat):                                 #filsEtat(etat) ; {retourne la liste des fils d'un état}
        fils = []
        truc =
        if isMovementPossible() :
            fils.append(truc)
        return fils

    def profondeurDAbord(depart):
      enAttente = depart
      vus = []
      trouve = False
      while enAttente != [] && trouve == False :        #Tant que la liste n'est pas vide ou qu'on a pas trouvé l'état
        prochain = enAttente.popleft()                  #On récupère l'état en tête de liste dans la variable prochain
        vus.append(prochain)                            #On ajout prochain à la liste des éléments vus
        if testEtatBut(prochain) :                      #Si jsp quoi
          trouve == True                                #L'état est trouvé
          return(True, prochain)                        #On return Vraie t l'état
        else :                                          #Sinon
          for e in filsEtat(prochain) :                 #On parcours les états fils de l'état prochain
            if !(e in vus):                             #Si ils n'ont pas été vus
            enAttente.insert(0, e)                      #On les insert à l'indice 0 de la liste enAttente
      if trouve == False:                               #Si l'état n'a pas été trouvé
        return(False, depart)                           #On return Faux et la liste de départ

    main() :
    """