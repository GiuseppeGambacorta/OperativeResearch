import matplotlib.pyplot as plt
from pulp import *


### HERE 1 AND 32 ARE THE INITIAL AND FINAL ACTIVITIES, THEY HAVE NO DURATION

# Create the problem
prob = LpProblem("Complex Activity Scheduling", LpMinimize)

# Define the activities and their durations
activities = {str(i): d for i, d in enumerate([0, 8, 4, 6, 3, 8, 5, 9, 2, 7, 9, 2, 6, 3, 9, 10, 6, 5, 3, 7, 2, 7, 2, 3, 3, 7, 8, 3, 7, 2, 2, 0], start=1)}

# Create variables for the start times of each activity, setting a lower bound of 0
start_times = LpVariable.dicts("Start", activities.keys(), lowBound=0, cat='Continuous')

# Objective function: minimize the completion time of the last activity
# Add a term to minimize the start times of all activities, this doesn't change much
prob += start_times['32'] + lpSum([start_times[act] for act in activities if act != '1' and act != '32']), "Minimize completion time"

# Define precedence relationships
predecessors = {'2': ['1'], '3': ['1'], '4': ['1'], '5': ['4'], '6': ['2'], '7': ['3'], '8': ['3'], '9': ['4'], '10': ['4'], 
                '11': ['2'], '12': ['8'], '13': ['3'], '14': ['9', '12'], '15': ['2'], '16': ['10'], '17': ['13', '14'], 
                '18': ['13'], '19': ['8'], '20': ['5', '11', '18'], '21': ['16'], '22': ['17', '16', '18'], '23': ['20', '22'], 
                '24': ['19', '23'], '25': ['15', '10', '20'], '26': ['11'], '27': ['7', '8'], '28': ['21', '27'], '29': ['19'], 
                '30': ['6', '24', '25'], '31': ['26', '28'], '32': ['29', '30', '31']}

# Add constraints to ensure the correct order of activities
for activity, preds in predecessors.items():
    for pred in preds:
        prob += start_times[pred] + activities[pred] <= start_times[activity]


# Solve the problem
prob.solve()

# Print the solution status
print("Status:", LpStatus[prob.status])

# Sort variables by start time
sorted_variables = sorted(prob.variables(), key=lambda v: v.varValue)
for v in sorted_variables:
    print(f"{v.name} = {v.varValue}")

# Print the minimum total time
print(f"Minimum total time: {value(prob.objective)}")

# Prepare data for the Gantt chart
tasks = []
start = []
durations = []
for activity, duration in activities.items():
    if activity not in ['1', '32']:  # Ignore initial and final activities for the chart
        tasks.append(activity)
        start.append(start_times[activity].varValue)
        durations.append(duration)

# Create the Gantt chart
fig, ax = plt.subplots(figsize=(15, 10))  # Increased the size of the chart
ax.barh(tasks, durations, left=start, color='skyblue')
ax.set_xlabel('Time')
ax.set_ylabel('Activities')
ax.set_title('Gantt Chart of Activities')

plt.show()
