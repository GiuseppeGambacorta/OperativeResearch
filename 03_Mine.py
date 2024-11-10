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
Mine1Transp1 = LpVariable("Mine1Transp1", lowBound=0)
Mine1Transp2 = LpVariable("Mine1Transp2", lowBound=0)
Mine1Transp3 = LpVariable("Mine1Transp3", lowBound=0)
Mine2Transp1 = LpVariable("Mine2Transp1", lowBound=0)
Mine2Transp2 = LpVariable("Mine2Transp2", lowBound=0)
Mine2Transp3 = LpVariable("Mine2Transp3", lowBound=0)

# Define the costs of the activities
activities = {
    Mine1Transp1: 11, Mine1Transp2: 8, Mine1Transp3: 2, 
    Mine2Transp1: 7, Mine2Transp2: 5, Mine2Transp3: 4, 
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
# mines must respect production limits
prob += Mine1Transp1 + Mine1Transp2 + Mine1Transp3 <= MaximumFirstMine
prob += Mine2Transp1 + Mine2Transp2 + Mine2Transp3 <= MaximumSecondMine

# plants must respect the demand
prob += Mine1Transp1 + Mine2Transp1 == MaximumTransportFirstPlant
prob += Mine1Transp2 + Mine2Transp2 == MaximumTransportSecondPlant
prob += Mine1Transp3 + Mine2Transp3 == MaximumTransportThirdPlant

# Solve the problem
prob.solve()

# Show the results
print("Solution status:", LpStatus[prob.status])
print(f"Objective function value: {prob.objective.value()}")

# Print the values of the variables
for v in prob.variables(): 
    print(f"{v.name} = {v.varValue}")