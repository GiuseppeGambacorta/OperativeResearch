import matplotlib.pyplot as plt
from pulp import *

# Create the problem
prob = LpProblem("Activity Scheduling", LpMinimize)

# Define the activities and their durations, S and T are the start and end activities, are fake
activities = {
    'S': 0, 'A': 2, 'B': 3, 'C': 1, 
    'D': 4, 'E': 5, 'F': 1, 'T': 0
}

# Create variables for the start times of each activity, setting a lower bound of 0
start_times = LpVariable.dicts("Start", activities.keys(), lowBound=0, cat='Continuous')

# Objective function: minimize the completion time of the last activity (T)
# Add a term to minimize the start times of all activities
prob += start_times['T'] + 0.01 * lpSum([start_times[act] for act in activities if act != 'S' and act != 'T']), "Minimize completion time and start times"

# Add constraints to ensure the correct order of activities

# start time of activity + its duration <= start time of the next activity
prob += start_times['S'] + activities['S'] <= start_times['A']
prob += start_times['S'] + activities['S'] <= start_times['B']
prob += start_times['S'] + activities['S'] <= start_times['C']
prob += start_times['A'] + activities['A'] <= start_times['D']
prob += start_times['B'] + activities['B'] <= start_times['F']
prob += start_times['D'] + activities['D'] <= start_times['E']
prob += start_times['C'] + activities['C'] <= start_times['E']
prob += start_times['D'] + activities['D'] <= start_times['T']
prob += start_times['E'] + activities['E'] <= start_times['T']
prob += start_times['F'] + activities['F'] <= start_times['T']

# Solve the problem
prob.solve()

# Print the solution status
print("Status:", LpStatus[prob.status])

# Sort variables by start time
sorted_variables = sorted(prob.variables(), key=lambda v: v.varValue)

for v in sorted_variables:
    print(f"{v.name} = {v.varValue}")

# Print the minimum total time
print(f"Minimum total time: {value(sorted_variables[-1].varValue)}") ##ignore the result of the problem, but check the start of T

# Prepare data for the Gantt chart
tasks = []
start = []
durations = []

for activity, duration in activities.items():
    if activity != 'S' and activity != 'T':  # Ignore initial and final activities for the chart
        tasks.append(activity)
        start.append(start_times[activity].varValue)
        durations.append(duration)

# Create the Gantt chart
fig, ax = plt.subplots()

ax.barh(tasks, durations, left=start, color='skyblue')
ax.set_xlabel('Time')
ax.set_title('Gantt Chart of Activities')

plt.show()
