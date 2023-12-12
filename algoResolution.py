import rumba as rmb

#algorithme de recherche profondeur bornée, prend en entrée le départ et le seuil
# retourne  0: programme termine, 1: rumba solution ?,2: vus, 3: totalAttente, 4: seuil prochaine recherche 
def PDE_IDA(depart=rmb.Rumba, seuil= 0):
    enAttente = [depart]
    vus=[]
    totalAttente = 1
    proSeuil =-1


    while (enAttente != []):
        temporaire = []

        enCours = enAttente.pop()
        vus.append(enCours.rumba)

        if enCours.isButAtteint():
            return (True, enCours, vus, totalAttente, proSeuil)
        
        for fromCol in range(rmb.NB_COLONNE):
            for toCol in range(rmb.NB_COLONNE):
                prochain = enCours.mouvPiece(fromCol, toCol)

                if prochain[0] and prochain[1]!=None and not(prochain[1].rumba in vus):

                    if prochain[1].heuristique <= seuil: 
                        temporaire.insert(len(temporaire)-1,prochain[1])
                        totalAttente+=1
                    elif prochain[1].heuristique<proSeuil or proSeuil<seuil:
                        proSeuil = prochain[1].heuristique
        enAttente=enAttente+temporaire
    return (False, depart, vus, totalAttente, proSeuil)

#algorithme IDA, prend en entrée le rumba de départ
#retourne 0: plan solution, 1: cout optimal, 2: la liste des Itérations, 3: La liste de toutes les branches développées
def IDAe (depart=rmb.Rumba):
    solution = [False, None, None, None, depart.calculHeuristique()]
    lstIterations = []

    while not solution[0]:
       print("Seuil pro", solution[4])
       solution = PDE_IDA(depart, solution[4])
       lstIterations.append(solution[3])
       lstIterations.append(len(solution[2]))

    return (solution[1].lstMvmnt, solution[1].heuristique, lstIterations, solution[2])
