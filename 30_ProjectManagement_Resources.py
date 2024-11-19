import matplotlib.pyplot as plt
from pulp import *

# Create the problem
prob = LpProblem("Activity Scheduling", LpMinimize)


T = 20
t_values = []

total_people = 4
total_cost = 5


for i in range(1, T+1):
    t_values.append(i)

# Define the activities and their durations, S and T are the start and end activities, are fake
activities_lenght = {
    'S': 0, 'A': 2, 'B': 3, 'C': 1, 
    'D': 4, 'E': 5, 'F': 1, 'T': 0
}

activities_people = {
    'S': 0, 'A': 3, 'B': 2, 'C': 1, 
    'D': 3, 'E': 3, 'F': 1, 'T': 0
}

activities_cost = {
    'S': 0, 'A': 3, 'B': 1, 'C': 3, 
    'D': 4, 'E': 1, 'F': 1, 'T': 0
}


finish_times = {}
for activity in activities_lenght.keys():
    for t in t_values:
        finish_times[(activity, t)] = LpVariable(f"Finish_{activity}_{t}", 0, 1, LpBinary)



total_finish_time = 0

for t in t_values:
    total_finish_time += t * finish_times[('T', t)]

# Imposta la funzione obiettivo nel problema
prob += total_finish_time, "Total_Finish_Time"        


# Assicurarsi che ogni attività termini esattamente una volta
for activity in activities_lenght.keys():
    prob += lpSum([finish_times[(activity, t)] for t in t_values]) == 1, f"Only_one_finish_time_{activity}"



for t in t_values:
    prob += finish_times[('A', t)] * t <= finish_times[('D', t)] * t - activities_lenght['D'], f"Precedence_A_D_at_time_{t}"
    prob += finish_times[('B', t)] * t <= finish_times[('F', t)] * t - activities_lenght['F'], f"Precedence_B_F_at_time_{t}"
    prob += finish_times[('D', t)] * t <= finish_times[('E', t)] * t - activities_lenght['E'], f"Precedence_D_E_at_time_{t}"
    prob += finish_times[('C', t)] * t <= finish_times[('E', t)] * t - activities_lenght['E'], f"Precedence_C_E_at_time_{t}"
    prob += finish_times[('D', t)] * t <= finish_times[('T', t)] * t - activities_lenght['T'], f"Precedence_D_T_at_time_{t}"
    prob += finish_times[('E', t)] * t <= finish_times[('T', t)] * t - activities_lenght['T'], f"Precedence_E_T_at_time_{t}"
    prob += finish_times[('F', t)] * t <= finish_times[('T', t)] * t - activities_lenght['T'], f"Precedence_F_T_at_time_{t}"


for t in t_values:
    total_resources_at_t = 0
    for activity in activities_lenght.keys():
        total_resources_at_t += activities_people[activity] * finish_times[(activity, t)]
    prob += total_resources_at_t <= total_people, f"PersonConstraint_at_time_{t}"


for t in t_values:
    total_resources_at_t = 0
    for activity in activities_lenght.keys():
        total_resources_at_t += activities_cost[activity] * finish_times[(activity, t)]
    prob += total_resources_at_t <= total_cost, f"CostConstraint_at_time_{t}"


# Risolvi il problema
prob.solve()

# Stampa lo stato della soluzione
print(f"Status: {LpStatus[prob.status]}")

# Stampa i tempi di fine per ogni attività
for activity in activities_lenght.keys():
    for t in t_values:
        if value(finish_times[(activity, t)]) == 1:
            print(f"Activity {activity} finishes at time {t}")

# Stampa il valore della funzione obiettivo
print(f"Total Finish Time: {value(prob.objective)}")