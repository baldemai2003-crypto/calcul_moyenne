n = int(input("combien de matieres ? :"))
total_points = 0
total_coef = 0
for i in range(n):
       note = float(input(f"notes de la matiere {i+1} :"))
       coef = float(input(f"coeficient de la matiere {i+1} :"))
       total_points += note * coef
       total_coef += coef
moyenne = total_points / total_coef
print(f"la moyenne est : {moyenne : .2f}/20")
