from pulp import LpMinimize, LpProblem, LpVariable, lpSum, LpStatus, PULP_CBC_CMD
from itertools import combinations

# Define the edges and their weights
edges = [
    ('A', 'B', 3),
    ('A', 'D', 4),
    ('A', 'E', 4),
    ('B', 'C', 10),
    ('B', 'E', 2),
    ('B', 'F', 3),
    ('C', 'F', 6),
    ('C', 'G', 1),
    ('D', 'E', 5),
    ('D', 'H', 6),
    ('E', 'F', 11),
    ('E', 'H', 2),
    ('E', 'I', 1),
    ('F', 'G', 2),
    ('F', 'I', 3),
    ('F', 'J', 11),
    ('G', 'J', 8),
    ('H', 'I', 4),
    ('I', 'J', 7)
]

# Create the minimization problem
prob = LpProblem("Minimum_Spanning_Tree", LpMinimize)

# Define the binary variables for each edge
x = {(i, j): LpVariable(f"x_{i}_{j}", cat='Binary') for i, j, w in edges}

# Objective function: minimize total weight
prob += lpSum(w * x[(i, j)] for i, j, w in edges)

# Get all nodes
nodes = set()
for i, j, _ in edges:
    nodes.add(i)
    nodes.add(j)
N = len(nodes)

nodes_var = {node: LpVariable(f"node_{node}", cat='') for node in nodes}

# Constraint 1: Number of edges must be N-1
prob += lpSum(x[(i, j)] for i, j, _ in edges) == N - 1

# Constraint 2: No cycles (subtour elimination)
# Generate all possible subsets of nodes (size >= 2)
for r in range(2, len(nodes)):
    for subset in combinations(nodes, r):
        # Get all edges that have both endpoints in the subset
        subset_edges = [(i, j) for i, j, _ in edges 
                       if i in subset and j in subset]
        if subset_edges:  # Only add constraint if there are edges in the subset
            prob += lpSum(x[edge] for edge in subset_edges) <= len(subset) - 1




# Solve the problem
prob.solve()

# Show the results
print("Solution status:", LpStatus[prob.status])
print(f"Total weight of the minimum spanning tree: {prob.objective.value()}")

# Print the edges in the minimum spanning tree
mst_edges = []
for i, j, w in edges:
    if x[(i, j)].varValue == 1:
        mst_edges.append((i, j, w))
        print(f"Edge ({i}, {j}) with weight {w} is in the MST")
print(f"Minimum Spanning Tree edges: {mst_edges}")