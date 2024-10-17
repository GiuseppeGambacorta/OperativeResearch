from pulp import LpMaximize, LpProblem, LpVariable, lpSum, LpStatus

# Create the maximization problem
prob = LpProblem("Maximization", LpMaximize)

# Define the variables
A = LpVariable("A", lowBound=0)
B = LpVariable("B", lowBound=0)
C = LpVariable("C", lowBound=0)
D = LpVariable("D", lowBound=0)
E = LpVariable("E", lowBound=0)
F = LpVariable("F", lowBound=0)

# Define the objective function
prob += 0, "Objective Function"
demandA = 1000

# Add constraints
prob += 0.4 * C == E
prob += 0.6 * C + 0.4 * B == D
prob += 0.7 * D == F
prob += 0.3 * A + 0.5 * B == C
prob += 0.7 * A == B
prob += 0.2 * D + demandA == A

# Solve the problem
prob.solve()

# Show the results
print("Solution status:", LpStatus[prob.status])
print(f"Objective function value: {prob.objective.value()}")

# Print the values of the variables
for v in prob.variables(): 
    print(f"{v.name} = {v.varValue}")