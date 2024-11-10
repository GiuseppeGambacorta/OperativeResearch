from pulp import LpMinimize, LpProblem, LpVariable, lpSum, LpStatus

# Definition of the cities and the cost matrix
cities = ['A', 'B', 'C', 'D', 'E']
cost = {
    ('A', 'B'): 3,  ('A', 'C'): 4,  ('A', 'D'): 2,  ('A', 'E'): 7,
    ('B', 'A'): 3,  ('B', 'C'): 4,  ('B', 'D'): 6,  ('B', 'E'): 3,
    ('C', 'A'): 4,  ('C', 'B'): 4,  ('C', 'D'): 5,  ('C', 'E'): 8,
    ('D', 'A'): 2,  ('D', 'B'): 6,  ('D', 'C'): 5,  ('D', 'E'): 6,
    ('E', 'A'): 7,  ('E', 'B'): 3,  ('E', 'C'): 8,  ('E', 'D'): 6
}

# Create the problem
prob = LpProblem("Traveling_Salesman_Problem", LpMinimize)

# Definition of binary variables x[i,j]
x = LpVariable.dicts('x', cost.keys(), cat='Binary')

# Objective function: minimize total cost
prob += lpSum(cost[i, j] * x[(i, j)] for i, j in cost)

# Constraint 1: Each city has exactly one outgoing arc
for i in cities:
    prob += lpSum(x[(i, j)] for j in cities if (i, j) in x) == 1

# Constraint 2: Each city has exactly one incoming arc
for j in cities:
    prob += lpSum(x[(i, j)] for i in cities if (i, j) in x) == 1

# Auxiliary variables for the subtour elimination constraints (MTZ)
u = LpVariable.dicts('u', cities, lowBound=1, upBound=len(cities), cat='Continuous')

# Subtour elimination constraints (MTZ)
# u_i is before of u_j, and if the arc (i, j) is selected, then u_i + 1 <= u_j
# if u_i is not before of u_j and the arc (i, j) is selected, then u_i +1 <= u_j is impossible
for i, j in cost:
    if i != 'A' and j != 'A' and i != j:
        prob += u[i] - u[j] + len(cities) * x[(i, j)] <= len(cities) - 1

# Solve the problem
prob.solve()

# Display the optimal route
print("Solution status:", LpStatus[prob.status])


# Retrieve the route
route = []
current_city = 'A'
visited = set()
while True:
    visited.add(current_city)
    for j in cities:
        if (current_city, j) in x and x[(current_city, j)].varValue == 1:
            route.append((current_city, j))
            current_city = j
            break
    if current_city == 'A' or len(visited) == len(cities):
        break

# Print the found route
print("Optimal route:")
for i, j in route:
    print(f"{i} -> {j}")
    last = i
    return_route = j


print(f"Total cost of the route: {prob.objective.value()}")
print(f"Total cost of the route without return: {prob.objective.value()- cost[last,return_route]}")