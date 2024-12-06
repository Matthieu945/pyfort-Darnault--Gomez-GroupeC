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
    if n <= 1 :
        return False
    for i in range (2, (n**2) + 1) :
        if n% i == 0 :
            return False
    return True


def premier_plus_proche(n) :
    while not est_premier(n) :
        n += 1
    return n

def epreuve_math_premier() :
    a = random.randint(10,20)
    print("Quel est le nombre premier le plus proche de ", a, "?")
    b = int(input("Votre réponse :"))
    if b == premier_plus_proche(a):
        print("Bravo ! Vous gagnez une clé.")
        return True
    else :
        print("Raté ! Vous ne gagnez pas de clé.")
        return False