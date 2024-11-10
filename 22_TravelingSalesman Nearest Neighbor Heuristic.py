# Definition of cities and the cost matrix
cities = ['A', 'B', 'C', 'D', 'E']
cost = {
    ('A', 'B'): 3,  ('A', 'C'): 4,  ('A', 'D'): 2,  ('A', 'E'): 7,
    ('B', 'A'): 3,  ('B', 'C'): 4,  ('B', 'D'): 6,  ('B', 'E'): 3,
    ('C', 'A'): 4,  ('C', 'B'): 4,  ('C', 'D'): 5,  ('C', 'E'): 8,
    ('D', 'A'): 2,  ('D', 'B'): 6,  ('D', 'C'): 5,  ('D', 'E'): 6,
    ('E', 'A'): 7,  ('E', 'B'): 3,  ('E', 'C'): 8,  ('E', 'D'): 6
}

# Implementation of the "nearest neighbor" heuristic method
def nearest_neighbor_heuristic(cities, cost, start):
    tour = [start]
    current_city = start
    unvisited = set(cities)
    unvisited.remove(start)
    
    while unvisited:
        # Find the nearest unvisited city
        nearest_city = None
        min_distance = float('inf')
        for city in unvisited:
            if (current_city, city) in cost and cost[(current_city, city)] < min_distance:
                min_distance = cost[(current_city, city)]
                nearest_city = city
        if nearest_city is None:
            print("No unvisited city found from the current node.")
            return None
        tour.append(nearest_city)
        unvisited.remove(nearest_city)
        current_city = nearest_city
    # We do not add the return to the starting city here
    return tour

# Use of the algorithm
start_city = 'A'
tour = nearest_neighbor_heuristic(cities, cost, start_city)

# Calculate the total cost without returning to A
total_cost_without_return = 0
for i in range(len(tour) - 1):
    total_cost_without_return += cost[(tour[i], tour[i+1])]

# Calculate the total cost with return to A
# Add the cost to return to the start
total_cost_with_return = total_cost_without_return + cost[(tour[-1], start_city)]

# Show the path and total costs
print("Path found without return to A:", " -> ".join(tour))
print(f"Path length without return to A: {total_cost_without_return}")

# Update the tour to include the return to A
tour_with_return = tour + [start_city]
print("\nPath found with return to A:", " -> ".join(tour_with_return))
print(f"Path length with return to A: {total_cost_with_return}")
