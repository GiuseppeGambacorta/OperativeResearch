from pulp import LpMaximize, LpProblem, LpVariable, lpSum, LpStatus, LpBinary



graph = {
    0: [2, 6, 9],
    1: [4, 5, 9],
    2: [0, 9, 10],
    3: [4, 6, 7, 8, 9, 10],
    4: [1, 3, 5, 6, 7, 8, 9],
    5: [4, 6, 8, 10],
    6: [0, 1, 3, 4, 5],
    7: [3, 4, 9],
    8: [3, 4, 5],
    9: [0, 1, 2, 3, 4, 7],
    10: [2, 3, 5]
}

# Create the problem
prob = LpProblem("Graph coloring", LpMaximize)

# Define the binary variables for node
x = {}
for i in graph:
    x[i] = LpVariable(f'x_{i}', cat=LpBinary)


# Define the objective function. # Maximize the number of nodes 
prob += lpSum([x[i] for i in graph]), "Total_nodes"


# Constraint 1: two unconected nodes cannot be both in the clique
for node in graph:
    for othernode in graph:
        if node != othernode and othernode not in graph[node]:
            prob += x[node] + x[othernode] <= 1, f"NonAdjacent_{node}_{othernode}"




# Risolvi il problema
prob.solve()

# Stampa lo stato della soluzione
print("Stato della soluzione:", LpStatus[prob.status])

# Recupera i nodi che fanno parte della massima clique
clique_nodes = [i for i in graph if x[i].varValue == 1]

# Stampa i nodi della massima clique
print("Nodi nella massima clique:", clique_nodes)