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


def ProfondeurDabordBornee(depart=rmb.Rumba, seuil= 0):
    enAttente = [depart]
    vus = []
    position =0
    
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

        if position>=seuil:
            for i in range(len(temporaire)):
                if temporaire[i].isButAtteint():
                    return (True, temporaire[i])
                vus.append(temporaire[i])
        else:
            enAttente=enAttente+temporaire
            position +=1
    
    return (False, depart)


def PDE_IDA(depart=rmb.Rumba, seuil= 0, vus=[]):
    enAttente = [depart]
    continu = True
    prochainSeuil = -1
    nbAttente = 1
    
    while (enAttente != [] and continu):
        enCours = enAttente.pop()
        vus.append(enCours)

        if enCours.isButAtteint():
            return (True, enCours, vus, nbAttente, prochainSeuil)

        for e in range(rmb.NB_COLONNE):
            for d in range(rmb.NB_COLONNE):
                prochain = enCours.mouvPiece(e,d)
                if prochain[0] and prochain[1]!=None and not(prochain[1].isIn(vus)): 
                    print(prochain[1].rumba)
                    if prochain[1].heuristique <= seuil:
                        temporaire = PDE_IDA(prochain[1], seuil, vus)

                        nbAttente += temporaire[3]
                        if temporaire[0]:
                            return (True, temporaire[1], vus, nbAttente, prochainSeuil)
                    elif prochain[1].heuristique < prochainSeuil or prochainSeuil< seuil:
                        prochainSeuil = prochain[1].heuristique
    return (False, depart, vus, nbAttente, prochainSeuil)

def IDAe (depart=rmb.Rumba):
    #0: programme termine, 1: rumba solution ?,2: vus, 3: nbEnAttente, 4: seuil prochaine recherche 
    solution = [False, None, None, None, 6]
    lstIterations = []

    while not solution[0]:
       solution = PDE_IDA(depart, solution[4])
       lstIterations.append(solution[3])
       lstIterations.append(len(solution[2]))

    return (solution[1].lstMvmnt, solution[1].heuristique, lstIterations, solution[2])

