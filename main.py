import rumba as rmb
import algoResolution as algR

#penser a noter l'heuristique utilisée
#kevin.delcourt@irit.fr

def AfficherIteration(lstIterations):
    rslt = "\n"
    for i in range(len(lstIterations)-1):
        rslt += "    Iteration numero "+ str(i)+ ": "+ str(lstIterations[i+0])+" noeuds créés et "+ str(lstIterations[i+1])+ " noeuds développés"
    return rslt

def AfficherLstRumba(lstRumba):
    rslt = ""
    for i in range(len(lstRumba)):
        rslt += str(rmb.AfficherMatrice(lstRumba[i].rumba))
    return rslt

"""
Jaune: 1, 2, 3
Bleu:  4, 5, 6
Rouge: 7, 8, 9
"""

Situation1 =[[0,0,4,7],
             [2,0,5,8],
             [3,1,6,9]]

Situation2 =[[1,4,7,0],
             [2,5,8,0],
             [3,6,9,0]]

Situation1But1 =rmb.Rumba(Situation1,
                            [[1,0,4,7],
                            [2,0,5,8],
                            [3,0,6,9]])
Situation1But2 =rmb.Rumba(Situation1,
                            [[1,6,7,0],
                            [2,5,8,0],
                            [3,4,9,0]])
Situation2But3 =rmb.Rumba(Situation2,
                            [[7,8,1,0],
                            [2,4,5,0],
                            [3,6,9,0]])
Situation2But4 =rmb.Rumba(Situation2,
                            [[2,5,8,0],
                            [1,4,7,0],
                            [3,6,9,0]])
Situation2But5 =rmb.Rumba(Situation2,
                            [[8,0,5,0],
                            [2,4,7,0],
                            [3,6,9,1]])
Situation2But6 =rmb.Rumba(Situation2,
                            [[1,2,3,0],
                            [7,8,9,0],
                            [4,5,6,0]])
"""
print("Situation 1, But 1:\n", rmb.AfficherMatrice(Situation1But1.rumba))
temporaire= algR.IDAe(Situation1But1)
print(temporaire[2])
print("\nRésultat: ",temporaire[0],"\nCout opti: ", temporaire[1],
         "\nItérations: ", len(temporaire[2]), AfficherIteration(temporaire[2]),
            "\nListe des noeuds développés: ", AfficherLstRumba(temporaire[3]))
"""
print("Situation 1, But 2:\n", rmb.AfficherMatrice(Situation1But1.rumba))
temporaire= algR.IDAe(Situation1But2)
print(temporaire[2])
print("\nRésultat: ",temporaire[0],"\nCout opti: ", temporaire[1],
         "\nItérations: ", len(temporaire[2]), AfficherIteration(temporaire[2]),
            "\nListe des noeuds développés: ", AfficherLstRumba(temporaire[3]))
