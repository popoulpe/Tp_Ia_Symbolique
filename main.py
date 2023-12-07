import rumba as rmb
import ProfondeurDabord as pda

#penser a noter l'heuristique utilisée
#kevin.delcourt@irit.fr
modeAlgo = ""
jeu = rmb.Rumba([[3,0,0,0],
                 [2,5,8,9],
                 [1,4,6,7]],
                 
                 [[0,0,3,0],
                 [2,5,8,9],
                 [1,4,6,7]])


if modeAlgo == "ProfDab":
    profDab = pda.ProfondeurDabord(jeu)
    print(profDab)
    print("\n\n\n\nresultat: ",profDab[0],profDab[1].rumba)