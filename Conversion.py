from tkinter import CENTER


print("Bienvenue dans cet espace destiné à la conversion des chiffres en lettres")
print("Quelle valeur voulez-vous traduire?")

nombre = (input())
Solution = "La conversion de ce chiffre en lettre est : {}"

Les_unités_et_les_dizaines = {
    0 : "Zéro" ,
    1 : "Un" ,
    2 : "Deux" ,
    3 : "Trois" ,
    4 : "Quatre" ,
    5 : "Cinq" ,
    6 : "Six" ,
    7 : "Sept" ,
    8 : "Huit" ,
    9 : "Neuf" ,
    10 : "Dix" ,
    11 : "Onze" ,
    12 : "Douze" ,
    13 : "Treize" ,
    14 : "Quatorze" ,
    15 : "Quinze" ,
    16 : "Seize" ,
    17 : "Dix-sept" ,
    18 : "Dix-huit" ,
    19 : "Dix-neuf" ,
}

Les_dizaines_composées = {
    2 : "Vingt" ,
    3 : "Trente" ,
    4 : "Quarante" ,
    5 : "Cinquante" ,
    6 : "Soixante" ,
    7 : "Soixante-dix" ,
    8 : "Quatre-vingt" ,
    9 : "Quatre-vingt-dix"
}

Les_centaines = {
    1 : "Cent" ,
    2 : "Deux cent" ,
    3 : "Trois cent" ,
    4 : "Quatre cent" ,
    5 : "Cinq cent" ,
    6 : "Six cent" ,
    7 : "Sept cent" ,
    8 : "Huit cent" ,
    9 : "Neuf cent"
}


longueur_du_nombre = len (nombre)
if longueur_du_nombre == 1:
    print(Solution.format(Les_unités_et_les_dizaines.get(int(nombre))))

if longueur_du_nombre == 2 and int(nombre) < 20: 
    print(Solution.format(Les_unités_et_les_dizaines.get(int(nombre))))
if longueur_du_nombre == 2 and nombre[1] == 0:
    print(Solution.format(Les_dizaines_composées.get(int(nombre[0]))))
if longueur_du_nombre == 2:
    print(Solution.format(Les_dizaines_composées.get(int(nombre[0])) + " " + Les_unités_et_les_dizaines.get(int(nombre[1]))))

if longueur_du_nombre == 3 and int(nombre[1]) == 0 and int(nombre[2]) == 0:
    print(Solution.format(Les_centaines.get(int(nombre[0]))))
if longueur_du_nombre == 3 and int(nombre[1]) == 0:
    print(Solution.format(Les_centaines.get(int(nombre[0])) + " " + Les_unités_et_les_dizaines.get(int(nombre[2]))))
if longueur_du_nombre == 3 and int(nombre[1]) == 1:
    print(Solution.format(Les_centaines.get(int(nombre[0])) + " " + Les_unités_et_les_dizaines.get(int(nombre[2]))))
if longueur_du_nombre == 3 and int(nombre[1]) >= 2:
    print(Solution.format(Les_centaines.get(int(nombre[0])) + " " + Les_dizaines_composées.get(int(nombre[1])) + " " + Les_unités_et_les_dizaines.get(int(nombre[2]))))
