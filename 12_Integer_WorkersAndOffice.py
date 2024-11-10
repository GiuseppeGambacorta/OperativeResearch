from pulp import LpMinimize, LpProblem, LpVariable, lpSum, LpStatus, PULP_CBC_CMD
from tabulate import tabulate

# Create the minimization problem
prob = LpProblem("Office_Assignment", LpMinimize)

# Define the values that each employee gives to each office,
# higher values indicate a worst fit
# 14 employees and 10 offices
values = [
    [1, 9, 3, 3, 4, 9, 8, 5, 8, 10],
    [8, 3, 9, 7, 3, 10, 10, 9, 1, 4],
    [8, 6, 3, 2, 5, 4, 7, 1, 4, 5],
    [10, 9, 10, 1, 1, 5, 10, 3, 9, 6],
    [2, 2, 2, 9, 1, 9, 4, 4, 6, 5],
    [2, 9, 10, 2, 4, 3, 6, 7, 9, 4],
    [7, 7, 2, 6, 9, 3, 5, 1, 3, 6],
    [1, 2, 5, 7, 7, 9, 3, 7, 3, 6],
    [3, 1, 9, 8, 2, 6, 7, 8, 3, 3],
    [2, 9, 5, 7, 4, 10, 4, 4, 8, 8],
    [1, 8, 3, 10, 9, 2, 4, 3, 5, 6],
    [9, 10, 9, 4, 7, 8, 5, 1, 6, 9],
    [7, 5, 4, 6, 6, 6, 7, 8, 2, 6],
    [8, 6, 8, 1, 4, 8, 5, 1, 5, 8]
]

num_employees = len(values)
num_offices = len(values[0])

# Define the binary variables for each employee-office combination
x = []
for employee in range(num_employees):
    row = []
    for office in range(num_offices):
        row.append(LpVariable(f"x_{employee+1}_{office+1}", cat='Binary'))
    x.append(row)

# Define the objective function: minimize the total value of the assignments
objective_function = 0
for employee in range(num_employees):
    for office in range(num_offices):
        objective_function += values[employee][office] * x[employee][office]
prob += objective_function, "Total Value"

# Add constraints to ensure each employee is assigned to exactly one office, row-wise
for employee in range(num_employees):
    constraint = 0
    for office in range(num_offices):
        constraint += x[employee][office]
    prob += constraint == 1, f"Employee_{employee+1}_assignment"

# Add constraints to ensure each office has at most one employee, column-wise
for office in range(num_offices):
    prob += lpSum(x[employee][office] for employee in range(num_employees)) <= 2, f"Office_{office+1}_Maxcapacity"
    prob += lpSum(x[employee][office] for employee in range(num_employees)) >= 1, f"Office_{office+1}_Mincapacity"

# Solve the problem with detailed logging
prob.solve()

# Show the results
print("Solution status:", LpStatus[prob.status])
print(f"Total value of assignments: {prob.objective.value()}")

# Print the assignments
assignments = []
for employee in range(num_employees):
    for office in range(num_offices):
        if x[employee][office].varValue == 1:
            assignments.append((employee+1, office+1))
            print(f"Employee {employee+1} is assigned to Office {office+1}")

print(f"Assignments: {assignments}")

# Create a table for the assignments
table = [["Employee/Office"] + [f"Office {office+1}" for office in range(num_offices)]]
for employee in range(num_employees):
    row = [f"Employee {employee+1}"]
    for office in range(num_offices):
        if x[employee][office].varValue == 1:
            row.append("X")
        else:
            row.append("")
    table.append(row)

# Print the table
print(tabulate(table, headers="firstrow", tablefmt="grid"))