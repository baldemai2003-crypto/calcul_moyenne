note1 = float(input("entrer la premiere note : "))
note2 = float(input("entrer la deuxieme note : "))
note3 = float(input("entrer la troisieme note : "))

moyenne = (note1 + note2 + note3) / 3
print(f"la moyenne est : {moyenne: .2f}/20")

if moyenne >= 10:
    print("resultat: moyenne obtenue")
else:
    print("resultat: moyenne non obtenue")


