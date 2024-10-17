import matplotlib.pyplot as plt
from pulp import *


# S e T sono le attività iniziali e finali, non hanno durata, sono fittizie

# Creare il problema
prob = LpProblem("Activity Scheduling", LpMinimize)

# Definire le attività e le loro durate
activities = {
    'S': 0, 'A': 2, 'B': 3, 'C': 1, 
    'D': 4, 'E': 5, 'F': 1, 'T': 0
}



# Creare variabili per i tempi di inizio di ciascuna attività, mettendo un limite inferiore di 0
start_times = LpVariable.dicts("Start", activities.keys(), lowBound=0, cat='Continuous')


# Funzione obiettivo: minimizzare il tempo di fine dell'ultima attività (T)
prob += start_times['T'], "Minimize completion time"

# Aggiungere vincoli per assicurare l'ordine corretto delle attività

# tempo di inizio attività + sua durata <= tempo di inizio attività successiva 
prob += start_times['S'] + activities['S'] <= start_times['A']
prob += start_times['S'] + activities['S'] <= start_times['B']
prob += start_times['S'] + activities['S'] <= start_times['C']
prob += start_times['A'] + activities['A'] <= start_times['D']
prob += start_times['B'] + activities['B'] <= start_times['F']
prob += start_times['C'] + activities['C'] <= start_times['E']
prob += start_times['D'] + activities['D'] <= start_times['T']
prob += start_times['E'] + activities['E'] <= start_times['T']
prob += start_times['F'] + activities['F'] <= start_times['T']

# Risolvere il problema
prob.solve()

# Stampare lo stato della soluzione
print("Status:", LpStatus[prob.status])

# Ordino le variabili in base al tempo di inizio
sorted_variables = sorted(prob.variables(), key=lambda v: v.varValue)


for v in sorted_variables:
    print(f"{v.name} = {v.varValue}")

# Stampare il tempo totale minimo
print(f"Tempo totale minimo: {value(prob.objective)}")

# Preparare i dati per il grafico Gantt
tasks = []
start = []
durations = []

for activity, duration in activities.items():
    if activity != 'S' and activity != 'T':  # Ignorare le attività iniziali e finali per il grafico
        tasks.append(activity)
        start.append(start_times[activity].varValue)
        durations.append(duration)

# Creare il grafico Gantt
fig, ax = plt.subplots()

ax.barh(tasks, durations, left=start, color='skyblue')
ax.set_xlabel('Tempo')
ax.set_title('Diagramma di Gantt delle Attività')

plt.show()


