mot = input("veuillez saisir un mot :")
n = int(input("Veuillez saisir l'index de la lettre a supprimer :"))
print(mot[:n]+mot[n+1:])


