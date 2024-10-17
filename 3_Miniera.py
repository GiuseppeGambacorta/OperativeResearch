from pulp import LpMinimize, LpProblem, LpVariable, lpSum, LpStatus

'''
Il problema riguarda il trasporto di minerale di ferro dalle miniere agli impianti
siderurgici. La Miniera 1 ha 800 tonnellate di minerale disponibili al giorno e la
Miniera 2 ha 300 tonnellate. I 3 impianti siderurgici richiedono rispettivamente 400,
500 e 200 tonnellate di minerale al giorno. Il costo di trasporto (cent/es) è indicato
nella tabella. L'obiettivo è minimizzare il costo totale del trasporto
'''


# Creare il problema di minimizzazione
prob = LpProblem("Minimizzazione", LpMinimize)

# Definire le variabili
# definiscimi le 6 variabili con LpVariable
# vincolo che siano tutti positivi
x1_1 = LpVariable("X1_1", lowBound=0)
x1_2 = LpVariable("X1_2", lowBound=0)
x1_3 = LpVariable("X1_3", lowBound=0)
x2_1 = LpVariable("X2_1", lowBound=0)
x2_2 = LpVariable("X2_2", lowBound=0)
x2_3 = LpVariable("X2_3", lowBound=0)

# Definire i costi delle attività
activities = {
    x1_1: 11, x1_2: 8, x1_3: 2, x2_1: 7, 
    x2_2: 5, x2_3: 4, 
}

# Definire la funzione obiettivo
# devo minimizzare il costo totale del trasporto
prob += lpSum([activities[act] * act for act in activities]), "Funzione obiettivo"

# Aggiungere i vincoli
# qui non metto i loro coefficienti, il costo non influisce sui vincoli di trasporto
# le miniere devono rispettare i limiti di produzione
prob += lpSum([x1_1, x1_2, x1_3]) <= 800
prob += lpSum([x2_1, x2_2, x2_3]) <= 300

# l'approvigionamento degli impianti deve rispettare i limiti di richiesta
prob += lpSum([x1_1, x2_1]) == 400
prob += lpSum([x1_2, x2_2]) == 500
prob += lpSum([x1_3, x2_3]) == 200


# Risolvere il problema
prob.solve()

# Mostrare i risultati
print("Stato della soluzione:", LpStatus[prob.status])
print(f"Valore della funzione obiettivo: {prob.objective.value()}")

# Stampare i valori delle variabili
for v in prob.variables(): 
    print(f"{v.name} = {v.varValue}")
