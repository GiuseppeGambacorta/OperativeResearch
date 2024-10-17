from pulp import LpMinimize, LpProblem, LpVariable, lpSum, LpStatus

# Creare il problema di minimizzazione
prob = LpProblem("Minimizzazione", LpMinimize)

# Definire le variabili
x = LpVariable("x1", lowBound=None)  # Nessun limite inferiore o superiore
y = LpVariable("x2", lowBound=None)


# Definire la funzione obiettivo
prob += 2 * x + 3 * y , "Funzione obiettivo"

# Aggiungere i vincoli
prob += 1 * x + 4 * y  >= 4
prob += 4* x + 5 * y  >= 10
prob += 4* x + 3 * y  >= 8
prob += 3* x   >= 2
prob += 6* y   >= 2


# Risolvere il problema
prob.solve()

# Mostrare i risultati
print(f"x1 = {x.varValue}, x2 = {y.varValue}")
print(f"Valore della funzione obiettivo : {prob.objective.value()}")
print("Stato della soluzione:", LpStatus[prob.status])
