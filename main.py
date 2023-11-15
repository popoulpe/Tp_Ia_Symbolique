#def testEtatBut(etat) :

#def filsEtat(etat):

#def ajouterTete(e,liste):


def profondeurDAbord(depart):
  enAttente = depart
  vus = []
  trouve = False
  while enAttente != [] && trouve == False :
    prochain = pop.enAttente
    vus = vus.append(prochain)
    if testEtatBut(prochain) :
      trouve == True
      return(True, prochain)
    else :
      for e in filsEtat(prochain) :
        if !(e in vus):
        enAttente = ajouterTete(e, enAttente)
  if trouve == False:
    return(False, depart)
