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
        return NB_LIGNE
    
    #deplace la piece en haut de la colonne de "fromCol" a "toCol"
    #retourne True si possible et False si impossible
    def mouvPiece(self, fromCol, toCol):
        if self.isMouvPossible(fromCol, toCol):
            return False
        ligFromCol = self.getTop(fromCol)
        ligToCol = self.getTop(toCol)-1

        self.rumba[ligToCol][toCol] = self.rumba[ligFromCol][fromCol]
        self.top[toCol] = self.rumba[ligFromCol][fromCol]
        self.rumba[ligFromCol][fromCol] = 0
        self.top[fromCol] = self.rumba[self.getTop(fromCol)][fromCol]
        return True

    #retourne si un mouvement est possible 
    def isMouvPossible(self, fromCol, toCol) :
        return not((self.top[fromCol] == 0) or (self.rumba[toCol][0] != 0))

    def isButReached(self):
        return self.rumba == self.but
    

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