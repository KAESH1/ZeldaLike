import pygame
from Fonction import *
from constantes import *
from mapgrid import *

def dBox(num, T):
    coord = [0,0]
    k=0
    for i in range(len(T)):
        for j in range(len(T[i])):
            if T[i][j] == 4:
                k+=1
                if k == num:
                    coord[0] = j
                    coord[1] = i
                    return coord


papi = pnj(fenetre,image = pygame.image.load("Source/PNJ/USE/Papi_stand_bas.png") ,x= dBox(1,Home_grid)[0]*64, y = dBox(1,Home_grid)[1]*64,text = ["Salut fiston, bien dormi ? Moi pas trop...", "J'ai perdu le collier de perle que je comptais offrir à ta mère pour son anniversaire..."," La dernière fois que je l'ai vu je crois que je trainais aux alentours de l'auberge"], inclinaison = 3)

armurier = pnj(fenetre,image = pygame.image.load("Source/Map/warp.png") ,x= dBox(1,Armurerie_grid)[0]*64, y = dBox(1,Armurerie_grid)[1]*64,text = ["J'ai en effet acheté le collier hier, mais il n'est malheuresemtn déjà plus en ma possessoin","Je l'ai offert à ma nièce , elle a beau être soldate elle raffole de ce genre de babiole","A cette heure elle doit surement être en train de monter la guarde devant la grotte"], inclinaison = 3)

epiciere = pnj(fenetre,image = pygame.image.load("Source/Map/warp.png") ,x= dBox(1,Boutique_grid)[0]*64, y = dBox(1,Boutique_grid)[1]*64,text = ["Hein ? un collier ? en perle ? je ne vois pas de quoi tu parles...", "*Si Betty apprend que j'ai déjà vendu le collier à Smith à coté j'ai peur de ce qu'il m'attend"], inclinaison = 3)

aubergiste = pnj(fenetre,image = pygame.image.load("Source/Map/warp.png") ,x= dBox(1,Auberge_grid)[0]*64, y = dBox(1,Auberge_grid)[1]*64,text = ["Un collier en perle ? J'en ai effectivement trouvé un il y'a de cela quelque jour ","Je l'ai emmener dans le magasin au sud-est de la ville pour connaitre son prix", "Il devrait encore y être"], inclinaison = 3)

niece = pnj(fenetre,image = pygame.image.load("Source/PNJ/USE/solider_stand_bas.png") ,x= dBox(1,Village_grid)[0]*64, y = dBox(1,Village_grid)[1]*64,text = ["C'était ton collier ! Oh non... Qu'est ce que je vais faire...","Pour tout te dire hier en allant patrouiller dans la grotte, le collier est tomber lors d'un combat", "Si tu y tient vraiment je peux te laisser passer..."], inclinaison = 3)

soldat2 = pnj(fenetre,image = pygame.image.load("Source/PNJ/USE/solider_stand_bas.png") ,x= (dBox(2,Village_grid)[0]*64)+15, y = dBox(2,Village_grid)[1]*64,text = ["Un enfant de 8 ans dans une grotte pleine de monstres...","...Je refléchis trop ! Qu'est ce qu'il pourrait bien lui arriver de pire",], inclinaison = 3)



pnj_liste[0][0] = papi
pnj_liste[3][0] = aubergiste
pnj_liste[4][0] = armurier
pnj_liste[5][0] = epiciere

pnj_liste[1][0] = niece
pnj_liste[1][1] = soldat2
