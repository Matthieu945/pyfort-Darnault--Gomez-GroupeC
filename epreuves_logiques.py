def suiv(joueur):
    if joueur == 0:
        joueur = 1
    else :
        joueur = 0
    return joueur

#création du plateau de jeux
def grille_vide():
   return [[" " for i in range(3)] for j in range(3)]

grille = grille_vide()

#affichage du tableau de jeux
def affiche_grille(grille, message):
    print(message)
    for i in range (len(grille)):
        for j in range (len(grille[i])):
            print(grille[i][j],end=" | ")
        print( )
    print("-"*13)

#position sur la grille
def demande_position():
    condition = False

    while condition == False:

        ligne = int(input("Entrée le numéro de la ligne que vous voulez selectionné (entre 1 et 3): "))
        collone = int(input("Entrée le numéro de la collone que vous voulez selectionné (entre 1 et 3): "))
        pos = (ligne, collone)

        if 1 <= ligne <=3 and 1 <= collone <= 3:
            condition = True
            print (pos)
        else:
            print ("La position n'existe pas.")

def init():
