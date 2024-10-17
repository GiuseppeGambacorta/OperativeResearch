from pulp import LpProblem, LpVariable, LpMinimize, lpSum, LpStatus

# Create the problem (in this case, minimization, but it does not affect the system solution)
prob = LpProblem("Linear System", LpMinimize)

# Define the variables
x = LpVariable("x")
y = LpVariable("y")
z = LpVariable("z")

# Define the objective function
prob += 0, "Dummy Objective Function"

# Define the constraints based on the system equations
prob += 3 * x + 3 * z + y >= 0
prob += 2 * z - 3 * y >= 8
prob += 8 * x + 12 * y - z >= 2

prob += 3 * x + 3 * z + y <= 0
prob += 2 * z - 3 * y <= 8
prob += 8 * x + 12 * y - z <= 2

# Solve the problem
prob.solve()

# Show the results
print("System solution:")
print(f"x = {x.varValue}")
print(f"y = {y.varValue}")
print(f"z = {z.varValue}")

# Check the solution status
print("Solution status:", LpStatus[prob.status])