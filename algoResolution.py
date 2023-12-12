import rumba as rmb

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
                    print("prochain heurisitque: ", prochain[1].heuristique, " et seuil: ", seuil, " et proSeuil: ", prochainSeuil)
                    testSeuil = prochain[1].heuristique
                    if testSeuil <= seuil:
                        temporaire = PDE_IDA(prochain[1], seuil, vus)               #probleme ici, en gros il faut reussir a faire le transfer de prochain seuil
                        if temporaire[4] < testSeuil or testSeuil< seuil:           #(ce que j'ai essayé est surement faux)
                            testSeuil = temporaire[4]
                        nbAttente += temporaire[3]
                        if temporaire[0]:
                            return (True, temporaire[1], vus, nbAttente, prochainSeuil)
                    if testSeuil < prochainSeuil or prochainSeuil< seuil:
                        prochainSeuil = testSeuil
    return (False, depart, vus, nbAttente, prochainSeuil)

def IDAe (depart=rmb.Rumba):
    #0: programme termine, 1: rumba solution ?,2: vus, 3: nbEnAttente, 4: seuil prochaine recherche 
    solution = [False, None, None, None, depart.calculHeuristique()]
    lstIterations = []

    while not solution[0]:
       print("Seuil pro", solution[4])
       solution = PDE_IDA(depart, solution[4])
       lstIterations.append(solution[3])
       lstIterations.append(len(solution[2]))

    return (solution[1].lstMvmnt, solution[1].heuristique, lstIterations, solution[2])
