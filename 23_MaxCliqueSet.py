from pulp import LpMaximize, LpProblem, LpVariable, lpSum, LpBinary, LpStatus

# Example graph in adjacency list format
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
prob = LpProblem("Maximum Independent Set", LpMaximize)

# Define the binary variables for each node
x = {v: LpVariable(f'x_{v}', cat=LpBinary) for v in graph}

# Objective: Maximize the size of the independent set
prob += lpSum([x[v] for v in graph]), "Maximize Independent Set Size"

# Constraints: For each edge (u, v), x_u + x_v <= 1
for u in graph:
    for v in graph[u]:
        if u < v:  # To avoid adding duplicate edges (u, v) and (v, u)
            prob += x[u] + x[v] <= 1, f"NoEdge_{u}_{v}"

# Solve the problem
prob.solve()

# Print the status of the solution
print("Status of the solution:", LpStatus[prob.status])

# Retrieve the nodes that are part of the maximum independent set
independent_set = [v for v in graph if x[v].varValue == 1]

# Print the nodes in the maximum independent set
print("Maximum Independent Set:", independent_set)
