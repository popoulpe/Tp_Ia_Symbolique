from collection import deque
from dataclass import dataclass as dc

@dataclass
class Rumba:
    rumba : [][]

    def __init__(self, ligne, colonne):
        self.rumba = self.get_rumba(ligne, colonne)

    def get_rumba(self, ligne, colonne):
        num = 1
        matrice = [[None for i_colonne in range(colonne)] for i_ligne in range(ligne)]
        for i_ligne in range(len(matrice)):
            for i_colonne in range(len(matrice[i_ligne])-1):
                matrice[i_ligne][i_colonne] = num
                num += 1
        return matrice

    def isTopPile

    def topPile()

    def isMovementPossible()

    #def testEtatBut(etat) :                            #testEtatBut(etat) ; {prédicat caractérisant les buts}

    def filsEtat(etat):                                 #filsEtat(etat) ; {retourne la liste des fils d'un état}
        fils = []
        truc =
        if :
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
