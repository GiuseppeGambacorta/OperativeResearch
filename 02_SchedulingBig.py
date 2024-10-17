import matplotlib.pyplot as plt
from pulp import *


### QUI 1 E 32 SONO LE ATTIVITA' INIZIALI E FINALI, NON HANNO DURATA

# Creare il problema
prob = LpProblem("Complex Activity Scheduling", LpMinimize)

# Definire le attività e le loro durate
activities = {str(i): d for i, d in enumerate([0, 8, 4, 6, 3, 8, 5, 9, 2, 7, 9, 2, 6, 3, 9, 10, 6, 5, 3, 7, 2, 7, 2, 3, 3, 7, 8, 3, 7, 2, 2, 0], start=1)}

# Creare variabili per i tempi di inizio di ciascuna attività, mettendo un limite inferiore di 0
start_times = LpVariable.dicts("Start", activities.keys(), lowBound=0, cat='Continuous')

# Funzione obiettivo: minimizzare il tempo di fine dell'ultima attività

prob += start_times['32'] , "Minimize completion time"

# Definire le relazioni di precedenza
predecessors = {'2': ['1'], '3': ['1'], '4': ['1'], '5': ['4'], '6': ['2'], '7': ['3'], '8': ['3'], '9': ['4'], '10': ['4'], 
                '11': ['2'], '12': ['8'], '13': ['3'], '14': ['9', '12'], '15': ['2'], '16': ['10'], '17': ['13', '14'], 
                '18': ['13'], '19': ['8'], '20': ['5', '11', '18'], '21': ['16'], '22': ['17', '16', '18'], '23': ['20', '22'], 
                '24': ['19', '23'], '25': ['15', '10', '20'], '26': ['11'], '27': ['7', '8'], '28': ['21', '27'], '29': ['19'], 
                '30': ['6', '24', '25'], '31': ['26', '28'], '32': ['29', '30', '31']}

# Aggiungere vincoli per assicurare l'ordine corretto delle attività
for activity, preds in predecessors.items():
    for pred in preds:
        prob += start_times[pred] + activities[pred] <= start_times[activity]



# Risolvere il problema
prob.solve()

# Stampare lo stato della soluzione
print("Status:", LpStatus[prob.status])

# Ordinare le variabili in base al tempo di inizio
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
    if activity not in ['1', '32']:  # Ignorare le attività iniziali e finali per il grafico
        tasks.append(activity)
        start.append(start_times[activity].varValue)
        durations.append(duration)

# Creare il grafico Gantt
fig, ax = plt.subplots(figsize=(15, 10))  # Aumentato le dimensioni del grafico
ax.barh(tasks, durations, left=start, color='skyblue')
ax.set_xlabel('Tempo')
ax.set_ylabel('Attività')
ax.set_title('Diagramma di Gantt delle Attività')

plt.show()