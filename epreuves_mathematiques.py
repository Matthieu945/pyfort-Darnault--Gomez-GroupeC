#Épreuve factorielle

def factorielle(n) :
    for i in range (1, n) :
        n *= i
    return n

import random

def epreuve_math_factorielle() :
    n = random.randint(1,10)
    print("Calculer la factorielle de", n, ".")
    a = int(input("Votre réponse :"))
    if a == factorielle(n) :
        print("Bravo ! Vous gagnez une clé.")
        return True
    else :
        print("Raté ! Vous ne gagnez pas de clé.")
        return False

#Épreuve d'équation linéaire

def resoudre_equation_lineaire() :
    a = random.randint(1, 10)
    b = random.randint(1, 10)
    x = round(-b/a, 2)
    return a, b, x

def epreuve_math_equation() :
    a, b, x = resoudre_equation_lineaire()
    print("Résoudre cette équation : {}x + {} = 0".format(a, b))
    c = float(input("x = "))
    if c == x :
        print("Bravo ! Vous gagnez une clé.")
        return True
    else :
        print("Raté ! Vous ne gagnez pas de clé.")
        return False

#Épreuve des nombres premiers

def est_premier(n) :
    n = int(input("saisir une valeur : "))
    for i in range (2, n**2) :
        if n% i == 0 :
            print("n'est pas premier")
    else :
        print("est premier")

def premier_plus_proche(n) :
    for i in range (2, n**2) :
        if n% i == 0 :
            print("1")
