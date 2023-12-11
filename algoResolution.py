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
        print("enCours: ", enCours.rumba, "but: ", enCours.but, "vu: ", len(vus))
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
    
    while (enAttente != [] and continu):
        enCours = enAttente.pop()
        vus.append(enCours)

        print("enCours: ", enCours.rumba, "but: ", enCours.but, "nb_heur", enCours.heuristique, "vu: ", len(vus))
        if enCours.isButAtteint():
            return (True, enCours, vus, prochainSeuil)

        for e in range(rmb.NB_COLONNE):
            for d in range(rmb.NB_COLONNE):
                prochain = enCours.mouvPiece(e,d)
                if prochain[0] and prochain[1]!=None and not(prochain[1].isIn(vus)) and (prochain[1].heuristique <= seuil):
                    temporaire = PDE_IDA(prochain[1], seuil, vus)
                    vus.append(temporaire[2])
                    print("ici ?")
                    if temporaire[0]:
                        return (True, temporaire[1], vus, prochainSeuil)

                elif prochain[1].heuristique < prochainSeuil or prochainSeuil< seuil:
                    prochainSeuil = prochain[1].heuristique
    return (False, depart, vus, prochainSeuil)

def IDAe (depart=rmb.Rumba):
    #0: programme termine, 1: rumba solution ?,2: vus, inutile ici, 3: seuil prochaine recherche 
    solution = [False, None, None, depart.heuristique]
    lstIterations = [solution]

    while not solution[0]:
       print("seuil: ", solution[3])
       solution = PDE_IDA(depart, solution[3])

    print ("ici",solution[1].rumba)
    return (solution[1].lstMvmnt,solution[1].heuristique, solution[1])
       