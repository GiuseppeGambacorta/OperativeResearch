from pulp import LpMaximize, LpInteger, LpBinary, LpProblem, LpVariable,  LpStatus

# Create the maximization problem
prob = LpProblem("Maximization", LpMaximize)

# Define the variables
A = LpVariable("Number of desks", lowBound=0, cat=LpInteger)
B = LpVariable("Number of armadi", lowBound=0, cat=LpInteger)
C = LpVariable("Number of Chairs", lowBound=0, cat=LpInteger)

Y_A = LpVariable("Rent A", lowBound=0, cat=LpBinary)
Y_B = LpVariable("Rent B", lowBound=0, cat=LpBinary)
Y_C = LpVariable("Rent C", lowBound=0, cat=LpBinary)

priceA = 330
priceB = 620
priceC = 150

costProductionOfA = 82
costProductionOfB = 97
costProductionOfC = 28

TimeA = 16
TimeB = 29
TimeC = 10

WoodA = 10
WoodB = 15
WoodC = 3

CostRentTools_A = 120
CostRentTools_B = 130
CostRentTools_C = 70

MaxTime = 200
maxWood = 100

# Calculate M for each object, the maximum number of objects that can be produced
# A will always <= of the MaxNumber of possible objects A
M_A = min(MaxTime // TimeA, maxWood // WoodA)
M_B = min(MaxTime // TimeB, maxWood // WoodB)
M_C = min(MaxTime // TimeC, maxWood // WoodC)

# Define the objective function
prob += priceA * A + priceB * B + priceC * C - (costProductionOfA * A + costProductionOfB * B + costProductionOfC * C + CostRentTools_A * Y_A + CostRentTools_B * Y_B + CostRentTools_C * Y_C), "Objective Function"

# Add constraints
prob += TimeA * A + TimeB * B + TimeC * C <= MaxTime, "Time"
prob += WoodA * A + WoodB * B + WoodC * C <= maxWood, "Wood"
from pulp import LpMaximize, LpInteger, LpBinary, LpProblem, LpVariable, lpSum, LpStatus

# Create the maximization problem
prob = LpProblem("Maximization", LpMaximize)

# Define the variables
A = LpVariable("Number of desks", lowBound=0, cat=LpInteger)
B = LpVariable("Number of cabinets", lowBound=0, cat=LpInteger)
C = LpVariable("Number of chairs", lowBound=0, cat=LpInteger)

# Define the rent variables as binary (0 or 1), representing whether each object is rented or not
Rent_A = LpVariable("Rent desk", lowBound=0, cat=LpBinary)
Rent_B = LpVariable("Rent cabinet", lowBound=0, cat=LpBinary)
Rent_C = LpVariable("Rent chair", lowBound=0, cat=LpBinary)

priceA = 330
priceB = 620
priceC = 150

costProductionOfA = 82
costProductionOfB = 97
costProductionOfC = 28

TimeA = 16
TimeB = 29
TimeC = 10

WoodA = 10
WoodB = 15
WoodC = 3

CostRentTools_A = 120
CostRentTools_B = 130
CostRentTools_C = 70

MaxTime = 200
maxWood = 100

# Calculate M for each object, the maximum number of objects that can be produced
M_A = min(MaxTime // TimeA, maxWood // WoodA)
M_B = min(MaxTime // TimeB, maxWood // WoodB)
M_C = min(MaxTime // TimeC, maxWood // WoodC)

# Define the objective function
prob += priceA * A + priceB * B + priceC * C - (costProductionOfA * A + costProductionOfB * B + costProductionOfC * C + CostRentTools_A * Y_A + CostRentTools_B * Y_B + CostRentTools_C * Y_C), "Objective Function"

# Add constraints
prob += TimeA * A + TimeB * B + TimeC * C <= MaxTime, "Time"
prob += WoodA * A + WoodB * B + WoodC * C <= maxWood, "Wood"

#if i produce an object, i have to rent the tools, so if on the left side of the constraint 
# i have a number different from 0, Y_A must be 1
prob += A * (1 / M_A) <= Y_A, "Rent A" 
prob += B * (1 / M_B) <= Y_B, "Rent B"
prob += C * (1 / M_C) <= Y_C, "Rent C"



# Solve the problem with detailed logging
prob.solve()


# Show the results
print("Solution status:", LpStatus[prob.status])
print(f"Objective function value: {prob.objective.value()}")

# Print the values of the variables
for v in prob.variables(): 
    print(f"{v.name} = {v.varValue}")
