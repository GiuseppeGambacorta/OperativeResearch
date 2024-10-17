from pulp import LpProblem, LpVariable, LpMinimize, lpSum, LpStatus

# Creare il problema (in questo caso, minimizzazione, ma non influisce sulla soluzione del sistema)
prob = LpProblem("Sistema Lineare", LpMinimize)

# Definire le variabili
x = LpVariable("x")
y = LpVariable("y")
z = LpVariable("z")


# Definire la funzione obiettivo
prob += 0, "Funzione obiettivo fittizia"


# Definire i vincoli basati sulle equazioni del sistema
# imiti = mettendo entrambi i maggiori e minori
prob += 3*x + 3*z + y >= 0
prob += 2*z - 3*y >= 8
prob += 8*x + 12*y - z >= 2


prob += 3*x + 3*z + y <= 0
prob += 2*z - 3*y <= 8
prob += 8*x + 12*y - z <= 2

# Definire una funzione obiettivo fittizia (non influisce sulla soluzione del sistema)


# Risolvere il problema
prob.solve()

# Mostrare i risultati
print("Soluzione del sistema:")
print(f"x = {x.varValue}")
print(f"y = {y.varValue}")
print(f"z = {z.varValue}")

# Verificare lo stato della soluzione
print("Stato della soluzione:", LpStatus[prob.status])