from pulp import LpMaximize, LpProblem, LpVariable, lpSum, LpStatus, PULP_CBC_CMD

# Create the maximization problem
prob = LpProblem("Knapsack", LpMaximize)

# Define the values and weights of the items
values = [3, 6, 2, 6, 7, 4, 5, 2]
weights = [2, 5, 3, 9, 1, 4, 7, 8]
max_weight = 21  # Maximum weight capacity of the knapsack

# Define the binary variables for each item (1 if the item is included, 0 otherwise)
x = [LpVariable(f"x{i+1}", cat='Binary') for i in range(len(values))]

# Define the objective function: maximize the total value of the selected items
prob += lpSum(values[i] * x[i] for i in range(len(values))), "Total Value"

# Add the weight constraint: the total weight of the selected items must not exceed max_weight
prob += lpSum(weights[i] * x[i] for i in range(len(values))) <= max_weight, "Total Weight"

# Solve the problem with detailed logging
prob.solve()

# Show the results
print("Solution status:", LpStatus[prob.status])
print(f"Total value of selected items: {prob.objective.value()}")

# Print the values of the variables
for v in prob.variables():
    print(f"{v.name} = {v.varValue}")

# Print the selected items
selected_items = [i+1 for i in range(len(values)) if x[i].varValue == 1]
print(f"Selected items: {selected_items}")

# Print the total weight of the selected items
total_weight = sum(weights[i] for i in range(len(values)) if x[i].varValue == 1)
print(f"Total weight of selected items: {total_weight}")