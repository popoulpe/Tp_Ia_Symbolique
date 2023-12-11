import rumba as rmb
import algoResolution as algR

#penser a noter l'heuristique utilisée
#kevin.delcourt@irit.fr

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

print("Situation 1, But 1:\n")
temporaire= algR.IDAe(Situation1But1)
print("Réussite: ",temporaire[0], "\nRésultat: ", temporaire[1].AfficherRumba())