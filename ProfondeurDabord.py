import rumba as rmb

def ProfondeurDabord(depart=rmb.Rumba):
    enAttente = [depart]
    vus = []
    
    while (enAttente != []):
        temporaire = []
        enCours = enAttente.pop()
        vus.append(enCours)
        if enCours.isButAtteint():
            return (True, enCours)
        for e in range(rmb.NB_COLONNE):
            for d in range(rmb.NB_COLONNE):
                prochain = enCours.mouvPiece(e,d)
                if prochain[0] and not(prochain[1].isIn(vus)) and prochain[1]!=None:
                    temporaire.insert(len(temporaire)-1,prochain[1])
        enAttente=enAttente+temporaire
    
    return (False, depart)