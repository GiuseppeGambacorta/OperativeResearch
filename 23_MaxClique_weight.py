from pulp import LpMaximize, LpProblem, LpVariable, lpSum, LpStatus, LpBinary

# Graph definition with node weights
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

# Define weights for each node (example weights)
node_weights = {
    0: 0, 
    1: 17, 
    2: 2,
    3: 3, 
    4: 4, 
    5: 5, 
    6: 6, 
    7: 7, 
    8: 9, 
    9: 9, 
    10: 10
}

# Create the problem
prob = LpProblem("Max Weighted Clique", LpMaximize)

# Define the binary variables for each node
x = {i: LpVariable(f'x_{i}', cat=LpBinary) for i in graph}

# Objective: Maximize the sum of the weights of the nodes in the clique
prob += lpSum([node_weights[i] * x[i] for i in graph]), "Maximize Weighted Clique"

# Constraint 1: two unconected nodes cannot be both in the clique
for node in graph:
    all_nodes = set(graph.keys())
    all_nodes.remove(node)
    for adjacent in graph[node]:
        if adjacent in all_nodes:
            all_nodes.remove(adjacent)
    for othernode in all_nodes:
        prob += x[node] + x[othernode] <= 1, f"Adjacent_{node}_{othernode}"

# Solve the problem
prob.solve()

# Output the status of the solution
print("Solution Status:", LpStatus[prob.status])

# Retrieve the nodes that are part of the maximum clique
clique_nodes = [i for i in graph if x[i].varValue == 1]

# Print the nodes of the maximum clique
print("Nodes in the Maximum Clique:", clique_nodes)

# Print the total weight of the clique
total_weight = sum([node_weights[i] for i in clique_nodes])
print(f"Total weight of the Maximum Clique: {total_weight}")
