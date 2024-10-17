from pulp import LpMaximize, LpProblem, LpVariable, lpSum, LpStatus

'''
Il problema riguarda il trasporto di minerale di ferro dalle miniere agli impianti
siderurgici. La Miniera 1 ha 800 tonnellate di minerale disponibili al giorno e la
Miniera 2 ha 300 tonnellate. I 3 impianti siderurgici richiedono rispettivamente 400,
500 e 200 tonnellate di minerale al giorno. Il costo di trasporto (cent/es) è indicato
nella tabella. L'obiettivo è minimizzare il costo totale del trasporto
'''


# Creare il problema di massimizzazione
prob = LpProblem("Massimizzazione", LpMaximize)

# Definire le variabili
# definiscimi le 6 variabili con LpVariable
# vincolo che siano tutti positivi
A = LpVariable("A", lowBound=0)
B = LpVariable("B", lowBound=0)
C = LpVariable("C", lowBound=0)
D = LpVariable("D", lowBound=0)
E = LpVariable("E", lowBound=0)
F = LpVariable("F", lowBound=0)



# Definire la funzione obiettivo
# devo minimizzare il costo totale del trasporto
prob += 0, "Funzione obiettivo"
demandA = 1000
# Aggiungere i vincoli
# qui non metto i loro coefficienti, il costo non influisce sui vincoli di trasporto
# le miniere devono rispettare i limiti di produzione
prob += 0.4*C == E
prob += 0.6*C + 0.4*B == D
prob +=  0.7*D == F
prob +=  0.3*A + 0.5*B == C
prob +=  0.7*A == B
prob +=  0.2*D+demandA == A #ho bisogno di A per produrre A



# Risolvere il problema
prob.solve()

# Mostrare i risultati
print("Stato della soluzione:", LpStatus[prob.status])
print(f"Valore della funzione obiettivo: {prob.objective.value()}")

# Stampare i valori delle variabili
for v in prob.variables(): 
    print(f"{v.name} = {v.varValue}")
