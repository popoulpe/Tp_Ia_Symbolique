import rumba as rmb
import algoResolution as algR

def AfficherIteration(lstIterations):
    rslt = ""
    for i in range(len(lstIterations)-1):
        rslt += "\n    Iteration numero "+ str(i)+ ": "+ str(lstIterations[i+0])+" noeuds crees et "+ str(lstIterations[i+1])+ " noeuds developpes"
    return rslt

def AfficherLstRumba(lstRumba):
    rslt = ""
    for i in range(len(lstRumba)-1):
        rslt += str(lstRumba[i])+"   "
    rslt += "\nBut atteint: "+rmb.AfficherMatriceSansCouleurs(lstRumba[i])
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
                            [[1,9,4,0],
                            [2,8,5,0],
                            [3,7,6,0]])
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
                            [4,5,6,0],
                            [7,8,9,0]])


resultat = input("Quel dispoition voulez vous ?\nSituation1But1: 1"+
                 "\nSituation1But2: 2\nSituation2But3: 3\nSituation2But4: 4"+
                 "\nSituation2But5: 5\nSituation2But6: 6\n")

match resultat:
    case "1":
        SituationJouee= Situation1But1
    case "2":
        SituationJouee= Situation1But2
    case "3":
        SituationJouee= Situation2But3
    case "4":
        SituationJouee= Situation2But4
    case "5":
        SituationJouee= Situation2But5
    case "6":
        SituationJouee= Situation2But6

resultat = input("Voulez vous le resultat dans un fichier txt (avec liste vus) ou dans le terminal (avec couleurs) ?"+
                 "\n txt:1\n terminal: 2\n")

if resultat == "1":
    toFolder = "\n"+ ("_"*200)
    toFolder += "\nJeu:"+str(rmb.AfficherMatriceSansCouleurs(SituationJouee.rumba))+"\nBut:"+str(rmb.AfficherMatriceSansCouleurs(SituationJouee.but))
    temporaire= algR.IDAe(SituationJouee)
    toFolder += "\nResultat: "+str(temporaire[0])+"\nCout opti (heuristique mal mis): "+str(temporaire[1])+"\nIterations: "+ str(len(temporaire[2]))+ AfficherIteration(temporaire[2])
    toFolder += "\n"+AfficherLstRumba(temporaire[3])

    with open('Return.txt', 'a') as f:
        f.write(toFolder)
else:
    print("\nJeu:", rmb.AfficherMatrice(SituationJouee.rumba), "\nBut:", rmb.AfficherMatrice(SituationJouee.but))
    temporaire= algR.IDAe(SituationJouee)
    print("\nResultat: ", temporaire[0], "\nCout opti (heuristique mal mis): ",
           temporaire[1], "\nIterations: ", len(temporaire[2]), AfficherIteration(temporaire[2]))