from pulp import LpMinimize, LpProblem, LpVariable, lpSum, LpStatus, LpBinary

colors = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']

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
prob = LpProblem("Graph coloring", LpMinimize)

# Define the binary variables x[i,j]
x = {}
for i in graph:
    for j in colors:
        x[(i, j)] = LpVariable(f'x_{i}_{j}', cat=LpBinary)

# Define boolean variables for each color
y = {}
for j in colors:
    y[j] = LpVariable(f'y_{j}', cat=LpBinary)

# Define the objective function. # Minimize the total number of colors used and use the first colors of the array
prob += lpSum([(index + 1) * y[color] for index, color in enumerate(colors)]), "Total_Colors"

# Constraint 1: Each node has exactly one color
for i in graph:
    prob += lpSum([x[(i, j)] for j in colors]) == 1, f"Node_{i}_Color"

# Constraint 2: y[j] = 1 if color j is used by at least one node
for j in colors:
    for i in graph:
        prob += x[(i, j)] <= y[j], f"Color_{j}_Used_By_Node_{i}"

# Constraint 3: No adjacent nodes have the same color
for node in graph:
    for adjacent in graph[node]:
        for color in colors:
            prob += x[(node, color)] + x[(adjacent, color)] <= 1, f"Adjacent_{node}_{adjacent}_Color_{color}"


# Solve the problem
prob.solve()

# Print the solution status
print("Solution status:", LpStatus[prob.status])

# Print the colors assigned to each node
for i in graph:
    for j in colors:
        if x[(i, j)].varValue == 1:
            print(f"Node {i} is colored with color {j}")
            break

# Print the total number of colors used
total_colors_used = sum(y[j].varValue for j in colors)
print(f"Total number of colors used: {int(total_colors_used)}")
