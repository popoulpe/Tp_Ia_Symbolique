import rumba as rmb
import ProfondeurDabord as pda

#penser a noter l'heuristique utilisée
#kevin.delcourt@irit.fr

jeu = rmb.Rumba([[3,0,0,0],
                 [2,5,8,9],
                 [1,4,6,7]],
                 
                 [[0,0,3,0],
                 [2,5,8,9],
                 [1,4,6,7]])

print(jeu.rumba)
print(jeu.mouvPiece(0, 1))
print(jeu.rumba)
print(jeu.but)
print(jeu.isButAtteint())

profDab = pda.ProfondeurDabord(jeu)
print(profDab)
print(profDab[1].rumba)