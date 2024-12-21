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

