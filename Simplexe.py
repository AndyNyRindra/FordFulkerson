from pulp import LpMaximize, LpMinimize, LpProblem, LpVariable, LpInteger, PULP_CBC_CMD, LpStatus

# Définir le problème
problem = LpProblem("Maximisation_Exemple", LpMaximize)

# Définir les variables de décision (variables en nombres entiers)
# x1 = LpVariable('x1', lowBound=0, cat=LpInteger)
x1 = LpVariable('x1', lowBound=0)
x2 = LpVariable('x2', lowBound=0)
x3 = LpVariable('x3', lowBound=0)
x4 = LpVariable('x4', lowBound=0)
x5 = LpVariable('x5', lowBound=0)
x6 = LpVariable('x6', lowBound=0)

# Définir la fonction objective
problem += 40 * x1 + 10 * x2 + 0 * x3 + 0 * x4 + 7 * x5 + 14* x6, "Fonction_Objet"
# problem += 5 * x1 + 4 * x2, "Fonction_Objet"

# Définir les contraintes
problem += x1 - x2 + 2 * x5 == 0, "Contrainte_1"
problem += -2 * x1 + x2 - 2*x5 == 0, "Contrainte_2"
problem += x1 + x3 + x5 - x6 == 3, "Contrainte_3"
problem += x2 + x3 + x4 + 2*x5 + x6 == 4, "Contrainte_4"

# Résoudre le problème avec PULP_CBC_CMD
problem.solve()

# Afficher les résultats
print(f"Status: {problem.status}, {LpStatus[problem.status]}")
print(f"x1 = {x1.varValue}")
print(f"x2 = {x2.varValue}")
print(f"x3 = {x3.varValue}")
print(f"x4 = {x4.varValue}")
print(f"x5 = {x5.varValue}")
print(f"x6 = {x6.varValue}")
print(f"Valeur de la fonction objectif = {problem.objective.value()}")
