from pulp import LpMinimize, LpProblem, LpVariable, lpSum, LpStatus, PULP_CBC_CMD

# Define the graph using a dictionary of dictionaries
graph = {
    'A': {'B': 15, 'C': 13, 'D': 5},
    'B': {'H': 12},
    'C': {'B': 2, 'D': 18, 'F': 6},
    'D': {'E': 4, 'I': 99},
    'E': {'C': 3, 'D': 1, 'G': 9, 'I': 14},
    'F': {'B': 8, 'H': 17},
    'G': {'F': 16, 'H': 7, 'I': 10},
    'H': {},
    'I': {'H': 11}
}

# Create the minimization problem
prob = LpProblem("Shortest_Path", LpMinimize)

# Define the binary variables for each edge
edges = {}
for node in graph:
    for neighbor in graph[node]:
        edges[(node, neighbor)] = LpVariable(f"x_{node}_{neighbor}", cat='Binary')

# Define the objective function: minimize the total weight of the path
objective_function = 0
for node in graph:
    for neighbor in graph[node]:
        objective_function += graph[node][neighbor] * edges[(node, neighbor)]
prob += objective_function, "Total Weight"

# Add constraints to ensure the flow conservation
# Start node (A): flow out - flow in = 1
flow_out_A = 0
for neighbor in graph['A']:
    flow_out_A += edges[('A', neighbor)]
prob += flow_out_A == 1, "Flow_out_A"

flow_in_A = 0
for neighbor in graph:
    if 'A' in graph[neighbor]:
        flow_in_A += edges[(neighbor, 'A')]
prob += flow_in_A == 0, "Flow_in_A"

# End node (H): flow in - flow out = 1
flow_in_H = 0
for neighbor in graph:
    if 'H' in graph[neighbor]:
        flow_in_H += edges[(neighbor, 'H')]
prob += flow_in_H == 1, "Flow_in_H"

flow_out_H = 0
for neighbor in graph['H']:
    flow_out_H += edges[('H', neighbor)]
prob += flow_out_H == 0, "Flow_out_H"

# Intermediate nodes: flow in = flow out
for node in graph:
    if node not in ['A', 'H']:
        flow_in = 0
        for neighbor in graph:
            if node in graph[neighbor]:
                flow_in += edges[(neighbor, node)]
        flow_out = 0
        for neighbor in graph[node]:
            flow_out += edges[(node, neighbor)]
        prob += flow_in == flow_out, f"Flow_{node}"

# Solve the problem
prob.solve(PULP_CBC_CMD(msg=True))

# Show the results
print("Solution status:", LpStatus[prob.status])
print(f"Total weight of the shortest path: {prob.objective.value()}")

# Print the path
path = []
for edge in edges:
    if edges[edge].varValue == 1:
        path.append(edge)
        print(f"Edge {edge} is in the path")

print(f"Shortest path: {path}")