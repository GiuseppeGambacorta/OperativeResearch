from pulp import LpMinimize, LpProblem, LpVariable, lpSum, LpStatus

'''
The problem involves transporting iron ore from mines to steel plants.
Mine 1 has 800 tons of ore available per day, and Mine 2 has 300 tons.
The 3 steel plants require 400, 500, and 200 tons of ore per day, respectively.
The transport cost (in cents per ton) is shown in the table.
The goal is to minimize the total transportation cost.
'''

# Create the minimization problem
prob = LpProblem("Minimization", LpMinimize)

# Define the variables
# define the 6 variables with LpVariable
# constraint that all are non-negative
x1_1 = LpVariable("X1_1", lowBound=0)
x1_2 = LpVariable("X1_2", lowBound=0)
x1_3 = LpVariable("X1_3", lowBound=0)
x2_1 = LpVariable("X2_1", lowBound=0)
x2_2 = LpVariable("X2_2", lowBound=0)
x2_3 = LpVariable("X2_3", lowBound=0)

# Define the costs of the activities
activities = {
    x1_1: 11, x1_2: 8, x1_3: 2, x2_1: 7, 
    x2_2: 5, x2_3: 4, 
}


MaximumFirstMine = 800
MaximumSecondMine = 300
MaximumTransportFirstPlant = 400
MaximumTransportSecondPlant = 500
MaximumTransportThirdPlant = 200

# Define the objective function
# I need to minimize the total transportation cost
prob += lpSum([activities[act] * act for act in activities]), "Objective Function"

# Add the constraints
# here I do not include their coefficients, the cost does not affect transport constraints
# mines must respect production limits

prob += x1_1 + x2_1 <= MaximumFirstMine
prob += x1_2 + x2_2 <= MaximumSecondMine

# plants must respect the demand
prob += x1_1 + x1_2 + x1_3 == MaximumTransportFirstPlant
prob += x2_1 + x2_2 + x2_3 == MaximumTransportSecondPlant
prob += x1_3 + x2_3 == MaximumTransportThirdPlant

# Solve the problem
prob.solve()

# Show the results
print("Solution status:", LpStatus[prob.status])
print(f"Objective function value: {prob.objective.value()}")

# Print the values of the variables
for v in prob.variables(): 
    print(f"{v.name} = {v.varValue}")
