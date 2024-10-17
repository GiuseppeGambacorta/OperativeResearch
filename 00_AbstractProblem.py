from pulp import LpMinimize, LpProblem, LpVariable, lpSum, LpStatus

# Create the minimization problem
prob = LpProblem("Minimization", LpMinimize)

# Define the variables
x = LpVariable("x1", lowBound=None)  # No lower or upper bound
y = LpVariable("x2", lowBound=None)

# Define the objective function
prob += 2 * x + 3 * y , "Objective Function"

# Add constraints
prob += 1 * x + 4 * y  >= 4
prob += 4 * x + 5 * y  >= 10
prob += 4 * x + 3 * y  >= 8
prob += 3 * x   >= 2
prob += 6 * y   >= 2

# Solve the problem
prob.solve()

# Show the results
print(f"x1 = {x.varValue}, x2 = {y.varValue}")
print(f"Objective function value: {prob.objective.value()}")
print("Solution status:", LpStatus[prob.status])