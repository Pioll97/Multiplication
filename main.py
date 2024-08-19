import sys

def ListeTables():
    NbTable = int(input("Combien de tables voulez-vous ? : "))
    NbOpeTables = int(input("Combien d'opérations voulez-vous par table ? : "))
    for i in range(NbTable+1):
        t = i+1
        print(f"Table de {t} :")
        for o in range(NbOpeTables+1):
            p = t * o
            print(f"{o} * {t} = {p}")
        print()

def TableUnique():
    Table = int(input("Quel table voulez-vous ? : "))
    NbOpeTable = int(input("Combien d'opérations voulez-vous par table ? : "))
    print(f"Table de {Table} :")
    for i in range(NbOpeTable+1):
        p = Table * i
        print(f"{Table} * {i} = {p}")

def QuitterJeu():
    Quitter = input("Voulez-vous quitter ?\n oui\n non\n")
    if Quitter == "non":
        Jeu()
    else:
        exit

def Jeu():
    Demande = input("Quel voulez-vous faire : \n Une Liste de table - tapez a \n Une table unique - tapez b\n Quitter - tapez c\n")
    if Demande == "a":
        ListeTables()
        QuitterJeu()
    elif Demande == "b":
        TableUnique()
        QuitterJeu()
    elif Demande == "c":
        QuitterJeu()
    else:
        print("ERREUR : Veuillez saisir a ou b")
        QuitterJeu()

Jeu()
