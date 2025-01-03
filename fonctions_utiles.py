def introduction():
    print("Bonjour à vous, chers joueurs et joueuses !\n"
        "Bienvenue sur le fort pour jouer à ce jeu si mythique qu'est Fort Boyard !\n"
        "Lors de cette aventure avec votre équipe, vous devrez réussir plusieurs épreuves\n"
        "afin de récolter un objectif de trois clés pour accéder à la salle du trésor !\n"
        "Vous allez maintenant composer votre équipe.\n"
        "\n")
    input("Appuyer sur 'Entrée' pour composer votre équipe.")

def composer_equipe() :
    nombre_joueurs = int(input("Veuillez saisir le nombre de joueurs dans votre équipe : "))
    while nombre_joueurs <= 0 or nombre_joueurs > 3:
        print("Erreur. Votre équipe doit comporter entre 1 et 3 joueurs.")
        nombre_joueurs = int(input("Veuillez saisir le nombre de joueurs dans votre équipe : "))





    equipe = []

composer_equipe()