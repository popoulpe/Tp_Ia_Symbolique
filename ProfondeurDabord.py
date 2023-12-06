import rumba as rmb

#probleme, les id des rumba ne sont pas egales meme si equivalentes

def ProfondeurDabord(depart=rmb.Rumba):
    enAttente = [depart]
    vus = []

    while (enAttente != []):
        print("attente: ", vus)
        enCours = enAttente.pop()
        vus.append(enCours)
        print("encours: ", enCours.rumba, " et but: ", enCours.but)
        if enCours.isButAtteint():
            return (True, enCours)
        
        for e in range(rmb.NB_COLONNE):
            for d in range(rmb.NB_COLONNE):
                prochain = enCours.mouvPiece(e,d)
                if prochain[0] and not(prochain[1].isIn(vus)) and prochain[1]!=None:
                    enAttente.insert(len(enAttente), prochain[1])
    
    return (False, depart)